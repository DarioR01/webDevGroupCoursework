import json
from types import SimpleNamespace
from typing import Dict, List
from auction.models import Item, User, Question

from django.http import HttpRequest, HttpResponseBadRequest


def get_user(id:int):
    user: User = User.objects.filter(pk=id).get()
    return user

def get_item(id:int):
    item: Item = Item.objects.filter(id=id).get()
    return item

def get_question_for_item(id:int):
    item: Item = Item.objects.filter(id=id).get()

    questions: List = Question.objects.all().filter(item = item)

    return questions

def post_question_for_item(request: HttpRequest, item: Item):
    data: SimpleNamespace = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))

    # get values from request to populate question object
    try: 
        question: str = data.question
        user_id: int = data.user_id
    except:
        return HttpResponseBadRequest("Could not post question. Check that the request contains the question and the user_id asking the question")


    # get values to create new question object

    # owner must exist, because it's obtained from item and not request. Owner for item is checked on item's creation
    owner_id: int = item.owner.id
    owner: User = get_user(owner_id)

    try: 
        user: User = get_user(user_id)
    except:
        return HttpResponseBadRequest("Could not post question. User asking question could not be accessed")

    # create question object
    question: Question = create_new_question(question, owner, user, item)

def serialise_item(item: Item):
    owner: User = get_user(item.owner.id)
    owner = owner.to_dict()

    # if there is a bidder, get details of highest bidder
    highest_bidder: User
    try:
        highest_bidder= get_user(item.highest_bidder.id)
        highest_bidder = highest_bidder.to_dict()
    except: 
        highest_bidder = {}

    # if there is are questions for the item, get details of questions
    questions: List
    try:
        questions = get_question_for_item(item.id)
        serialised_quesitons = serialise_quesitons(questions)
    except: 
        questions = {}

    serialised_item : Dict[str][any] = {
        "id": item.id,
        "title": item.title,
        "description": item.description,
        "price": item.price,
        "highest_bidder": highest_bidder,
        "owner": owner,
        "questions": serialised_quesitons
    }
    return serialised_item

def serialise_quesitons(questions: List):
    questions_serialised: Dict [any][any] = {}

    # each question has foreign key of user that posted and user that asked
    # item should not be returned as an object, because questions are retrieved as part of items, never alone
    # no need to return item within question when question is within item
    for q in questions:
        owner: User = q.owner.to_dict()
        user: User = q.user.to_dict()
        item_id: int = q.item.id


        question: Dict[str][any] = {
            "id": q.id,
            'question'   : q.question,
            'owner'      : owner,
            'user'       : user,
            'item_id'    : item_id
        }
        
        # if there is an answer for a question, then it should be returned
        if q.answer: 
            question.update({"answer": q.answer})

        questions_serialised.update({q.id: question})

    return questions_serialised

def build_response_body_for_get_item(item: Item):
    serialised_item = serialise_item(item)
    return serialised_item
   

def create_new_question(question: str, owner: User, user: User, item: Item, answer: str = None):
    question: Question = Question(
        question = question,
        answer = answer,
        owner = owner,
        user = user,
        item = item            
    )

    question.save()

    return question

# b = Item(
#                 title = "test item",
#                 description = "this is a test item",
#                 price = 0,
#                 owner = user
#             )

#         b.save()