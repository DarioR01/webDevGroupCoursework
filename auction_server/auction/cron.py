from .models import Item, User
from typing import List, AnyStr
from django.core.mail import send_mail
import datetime
from django.conf import settings

def send_emails():
    items: List = Item.objects.all()
    for item in items:
        item_dict: Item = item.to_dict()
        if (item_dict["final_date"] < datetime.date.today()): 
            if item.getSent():
                continue
            try:
                user: User = item_dict["highest_bidder"]
                if user:
                    user: User = user.to_dict()
                    item_title: AnyStr = item_dict["title"]
                    text = f"You won the bid for the item , go purchase {item_title} now!!!"
                    send_mail(
                        'You won the bid',
                        text,
                        settings.EMAIL_HOST_USER,
                        [user['email']],
                        fail_silently=False,
                    )
                    item.email_sent = True
                    item.save()
            except:
                continue
        continue
        