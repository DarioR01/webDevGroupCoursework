from auction.models import Item, User

from django.contrib.auth import authenticate

def get_user(id:int):
    user: User = User.objects.filter(pk=id).get()
    return user

def get_item(id:int):
    item: Item = Item.objects.filter(id=id).get()
    return item



# b = Item(
#                 title = "test item",
#                 description = "this is a test item",
#                 price = 0,
#                 owner = user
#             )

#         b.save()