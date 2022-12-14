from datetime import date, datetime
import json
import re
from types import SimpleNamespace
from typing import Dict, List

from auction.models import Item, User, Question
from django.db.models import Q
from django.utils.dateparse import parse_datetime

from django.http import HttpRequest, HttpResponseBadRequest, JsonResponse


def get_user(user_id:int):
    user: User = User.objects.filter(pk=user_id).get()
    return user

def get_item(item_id:int):
    item: Item = Item.objects.filter(id=item_id).get()
    return item

def get_question_for_item(item:Item, question_id: int):
    question: Question = Question.objects.filter(item = item, id = question_id).get()
    return question

def get_all_questions_for_item(id:int):
    item: Item = Item.objects.filter(id=id).get()
    questions: List = Question.objects.all().filter(item = item)
    return questions

def get_list_of_items(request: HttpRequest):
    #if in the request is present a filter key, get list of filtered items
    try: 
        # filter items using the filter key if contained in title or description
        filter_keyword: str = request.GET.get('filter')
        if filter_keyword:
            items: List = Item.objects.filter(
                Q(title__contains=filter_keyword) |
                Q(description__contains=filter_keyword)
        )
        else:
            items: List = Item.objects.all()
    except:
        return HttpResponseBadRequest("Could not retrieve the items for the home page")

    items_serialised: Dict [any][any] = {}
    for item in items:
        serialised_item: dict[str, str | int | User | List] = serialise_item(item)
        items_serialised.update({item.id: serialised_item})

    return items_serialised

def update_item_highest_bidder_and_price(request: HttpRequest, item: Item):
    #get user id from the session
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
    return JsonResponse(serialised_item)

def updated_profile_page(request: HttpRequest):
    #get user id from the session
    session_data = request.session
    uid: int = session_data.get('_auth_user_id')

    data: SimpleNamespace = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))

    # get values from request to update user object
    try: 
        name: str = data.name
        surname: str = data.surname
        email: str = data.email
        date_of_birth: int = data.date_of_birth
    except:
        return HttpResponseBadRequest("Could not update the user. check that the request contains the email, date of birth and image.")

    try: 
        user: User = get_user(uid)
    except:
        return HttpResponseBadRequest("Could not update the user. the user could not accessed")

    user.name = name
    user.surname = surname
    user.email = email
    user.date_of_birth = date_of_birth
    user.save()
    
    serialised_user: dict[str, str | date] = serialise_user(user)
    return JsonResponse(serialised_user)
    
def post_question_for_item(request: HttpRequest, item: Item):
    #get user id from the session
    session_data = request.session
    uid: int = session_data.get('_auth_user_id')

    data: SimpleNamespace = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))

    # get values from request to populate question object
    try: 
        question: str = data.question
        user_id: int = uid
    except:
        return HttpResponseBadRequest("Could not post question. Check that the request contains the question and the user_id asking the question")

    # owner must exist, because it's obtained from item and not request. Owner for item is checked on item's creation
    owner_id: int = item.owner.id
    owner: User = get_user(owner_id)

    try: 
        user: User = get_user(user_id)
    except:
        return HttpResponseBadRequest("Could not post question. User asking question could not be accessed")

    # create question object
    question: Question = create_new_question(question, owner, user, item)

    serialised_question = serialise_question(question)
    return JsonResponse(serialised_question)

def post_new_item(request: HttpRequest):
    #get user id from the session
    session_data = request.session
    owner_id: int = session_data.get('_auth_user_id')

    data: SimpleNamespace = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))

    # get values from request to update item object
    try:
        title: str = data.title
        description: str = data.description
        price: int = data.price
        final_date: str = data.final_date
    except:
        return HttpResponseBadRequest("Could not post item. check that the request contains the title, descpription, a final date and price")
    
    #parse string JSON date to datetime date for model
    final_date = convert_string_date_to_date(final_date)
    
    #validate future date
    if not is_valid_final_date(final_date):
        return HttpResponseBadRequest("Invalid date. Expiration date for an item must be future date")

    item: Item = create_new_item(title, description, price, final_date, owner_id)
    serialised_item: dict[str, str | int | User | List] = serialise_item(item)
    return JsonResponse(serialised_item)
    
def post_answer_for_question(request: HttpRequest, item_id: int, question_id: int):
    #get user id from the session
    session_data = request.session
    uid: int = session_data.get('_auth_user_id')

    data: SimpleNamespace = json.loads(request.body, object_hook=lambda d: SimpleNamespace(**d))
    
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
    return JsonResponse(serialised_question)

def serialise_user(user: User):
    #build JSON serialisable user object
    serialised_user : Dict[str][any] = {
        "email": user.email,
        "name": user.name,
        "surname": user.surname,
        "date_of_birth": user.date_of_birth,
    }
    return serialised_user

def serialise_item(item: Item):
    #get owner fields
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
        "finale_date": item.final_date,
        "highest_bidder": highest_bidder,
        "owner": owner,
        "questions": questions
    }
    return serialised_item

def serialise_question(question: Question):
    #get objects owner, user from foreign keys
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
    #build list of JSON serialised item objects
    questions_serialised: Dict [any][any] = {}
    for q in questions:
        question = serialise_question(q)
        questions_serialised.update({q.id: question})

    return questions_serialised

def build_response_body_for_get_item(item: Item):
    # build JSON serialisable item object
    serialised_item = serialise_item(item)
    return JsonResponse(serialised_item)

def build_response_body_for_get_user(request):
    #get user id from the session
    session_data = request.session
    uid: int = session_data.get('_auth_user_id')

    user: User = get_user(uid)

    #build JSON serialisable user object
    serialised_user = serialise_user(user)
    return JsonResponse(serialised_user)

def create_new_question(question: str, owner: User, user: User, item: Item, answer: str = None):
    #create new uestion object
    question: Question = Question(
        question = question,
        answer = answer,
        owner = owner,
        user = user,
        item = item            
    )
    question.save()
    return question

def create_new_item(title, description, price, final_date, owner_id):
    #get owner 
    owner: User = get_user(owner_id)

    #create new item object
    item: Item = Item(
        title = title,
        description = description,
        price = price,
        owner = owner,
        final_date = final_date
    )
    item.save()

    return item

def convert_string_date_to_date(string_date: str):
    #yyyy-mm-dd 
    regex = r"^(?:(?:1[6-9]|[2-9]\d)?\d{2})(?:(?:(\/|-|\.)(?:0?[13578]|1[02])\1(?:31))|(?:(\/|-|\.)(?:0?[13-9]|1[0-2])\2(?:29|30)))$|^(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00)))(\/|-|\.)0?2\3(?:29)$|^(?:(?:1[6-9]|[2-9]\d)?\d{2})(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:0?[1-9]|1\d|2[0-8])$"

    #parse date from string as it comes in JSON request to datetime for model
    if re.match(regex, string_date):
        date = parse_datetime(string_date)
        return date

def is_valid_final_date(date):
    # check if date argument is a future date, returns boolean
    return date > datetime.now()