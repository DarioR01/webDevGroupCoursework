from django.db import models
import datetime

class User(models.Model):
    email           = models.EmailField(max_length=254, editable=True)
    name            = models.CharField(max_length=30, editable=True)
    surname         = models.CharField(max_length=30, editable=True)
    image           = models.ImageField(upload_to='./uploads', editable=True)
    date_of_birth   = models.DateField(default=datetime.date.today, editable=True)
    password        = models.CharField(max_length=50, editable=True)

    def __str__(self):
        return f'{self.id}, {self.name}'

    
    def to_dict(self):
        return {
            'id'            : self.id,
            'email'         : self.email,
            'name'          : self.name,
            'surname'       : self.surname,
            'image'         : self.image,
            'date_of_birth' : self.date_of_birth,
            'password'      : self.password,
        }