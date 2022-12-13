import json
from types import SimpleNamespace
from typing import Dict, List
from auction.models import Item, User, Question
from django.db.models import Q

from django.http import HttpRequest, HttpResponseBadRequest


def get_user(id:int):
    user: User = User.objects.filter(pk=id).get()
    return user

def get_item(id:int):
    item: Item = Item.objects.filter(id=id).get()
    return item

def get_question_for_item(item:Item, question_id: int):
    question: Question = Question.objects.filter(item = item, id = question_id).get()
    return question

def get_all_questions_for_item(id:int):
    item: Item = Item.objects.filter(id=id).get()
    questions: List = Question.objects.all().filter(item = item)
    return questions

def get_list_of_items(request: HttpRequest):
    try: 
        data: SimpleNamespace = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))
        filter_keyword: str = data.filter
        items: List = Item.objects.filter(
            Q(title__contains=filter_keyword) |
            Q(description__contains=filter_keyword)
        )
    except:
        items: List = Item.objects.all()

    items_serialised: Dict [any][any] = {}
    for item in items:
        serialised_item: dict[str, str | int | User | List] = serialise_item(item)
        items_serialised.update({item.id: serialised_item})

    return items_serialised

def update_item_highest_bidder_and_price(request: HttpRequest, item: Item):
    session_data = request.session
    uid: int = session_data.get('_auth_user_id')
    data: SimpleNamespace = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))

    # get values from request to update item object
    try: 
        highest_bidder_id: int = uid
        price: int = data.price
    except:
        return HttpResponseBadRequest("Could not update item. Check that the request contains the highest_bidder id and a price")
    
    #find the user corresponding to the highest bidder
    try: 
        highest_bidder: User = get_user(highest_bidder_id)
    except:
        return HttpResponseBadRequest("Could not bid on item. User bidding on item could not be accessed")

    #update the highest bidder in the item with the highest bidder found above and the price
    item.highest_bidder = highest_bidder
    item.price = price
    item.save()

    serialised_item: dict[str, str | int | User | List] = serialise_item(item)
    return serialised_item

def updated_profile_page(request: HttpRequest):
    session_data = request.session
    uid: int = session_data.get('_auth_user_id')
    data: SimpleNamespace = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))
    try: 
        user_id: int = uid
        email: str = data.email
        date_of_birth: int = data.date_of_birth
    except:
        return HttpResponseBadRequest("Could not update the user. check that the request contains the email, date of birth and image.")

    try: 
        user: User = get_user(user_id)
    except:
        return HttpResponseBadRequest("Could not update the user. the user could not accessed")

    user.email = email
    user.date_of_birth = date_of_birth
    user.save()
    
    return user

def post_question_for_item(request: HttpRequest, item: Item):
    session_data = request.session
    uid: int = session_data.get('_auth_user_id')
    data: SimpleNamespace = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))

    # get values from request to populate question object
    try: 
        question: str = data.question
        user_id: int = uid
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

def post_answer_for_question(request: HttpRequest, item_id: int, question_id: int):
    data: SimpleNamespace = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))
    session_data = request.session
    uid: int = session_data.get('_auth_user_id')
    # get values from request to update question object
    try: 
        answer: str = data.answer
    except:
        return HttpResponseBadRequest("Could not update question. Check that the request contains the answer")

    #check that item passed in url is an item and can be retrieved
    try:
        item: Item = get_item(item_id)
    except: 
        return HttpResponseBadRequest("No item found")

    #check that question passed in url is a question for that item and can be retrieved
    try:
        question: Question = get_question_for_item(item, question_id)
    except:
        return HttpResponseBadRequest("No question found")
 
    question.answer = answer
    question.save()

    serialised_question = serialise_question(question)
    return serialised_question

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
        questions = get_all_questions_for_item(item.id)
        questions = build_questions_list(questions)
    except: 
        questions = {}

    serialised_item : Dict[str][any] = {
        "id": item.id,
        "title": item.title,
        "description": item.description,
        "price": item.price,
        "highest_bidder": highest_bidder,
        "owner": owner,
        "questions": questions
    }
    return serialised_item

def serialise_question(question: Question):
    # each question has foreign key of user that posted and user that asked
    # item should not be returned as an object, because questions are retrieved as part of items, never alone
    # no need to return item within question when question is within item
    owner: User = question.owner.to_dict()
    user: User = question.user.to_dict()
    item_id: int = question.item.id


    question_object: Dict[str][any] = {
        "id": question.id,
        'question'   : question.question,
        'answer'     : "",
        'owner'      : owner,
        'user'       : user,
        'item_id'    : item_id
    }
    
    # if there is an answer for a question, then it should be returned
    if question.answer: 
        question_object['answer'] = question.answer

    return question_object

def build_questions_list(questions: List):
    questions_serialised: Dict [any][any] = {}
    for q in questions:
        question = serialise_question(q)
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