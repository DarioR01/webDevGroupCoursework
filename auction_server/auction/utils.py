from typing import Dict
from auction.models import Item, User

from django.contrib.auth import authenticate

def get_user(id:int):
    user: User = User.objects.filter(pk=id).get()
    return user

def get_item(id:int):
    item: Item = Item.objects.filter(id=id).get()
    return item

def build_get_item_body(item: Item):
    owner: User = get_user(item.owner.id)
    owner = owner.to_dict()

    # if there is a bidder, get details of highest bidder
    highest_bidder: User
    try:
        highest_bidder= get_user(item.highest_bidder.id)
        highest_bidder = highest_bidder.to_dict()
    except: 
        highest_bidder = {}


    # construct payload object with info about item, bidderm owner
    body : Dict[str][any] = {
        "id": item.id,
        "title": item.title,
        "description": item.description,
        "price": item.price,
        "highest_bidder": highest_bidder,
        "owner": owner
    }
    return body

# b = Item(
#                 title = "test item",
#                 description = "this is a test item",
#                 price = 0,
#                 owner = user
#             )

#         b.save()