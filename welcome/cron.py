from .models import Item, User
from typing import List, AnyStr
from django.core.mail import send_mail
import datetime
from django.conf import settings
import pytz

def send_emails():
    items: List = Item.objects.all()
    utc=pytz.UTC
    for item in items:
        item_dict: Item = item.to_dict()
        final_date = item_dict["final_date"] 
        today = utc.localize(datetime.datetime.today())

        if (final_date < today): 
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
        