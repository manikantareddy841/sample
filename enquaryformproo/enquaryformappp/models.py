from django.db import models
from multiselectfield import MultiSelectField
class enquarydata(models.Model):
    name=models.CharField(max_length=60)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=60)
    courses_choices=(
        ('python','python'),
        ('django','django'),
        ('ui','ui'),
        ('restapi','restapi')

    )
    courses=MultiSelectField(choices=courses_choices,max_length=200)
    trainers_choices=(
        ('mani','mani'),
        ('chinna','chinna'),
        ('siva','siva')

    )
    trainers=MultiSelectField(choices=trainers_choices,max_length=200)
    location_choices=(
        ('srnagar','srnagar'),
        ('madhapur','madhapur'),
        ('kphb','kphb')
    )
    locations=MultiSelectField(choices=location_choices,max_length=200)
    gender=models.CharField(max_length=60)
    start_date=models.DateField(max_length=100)

# Create your models here.
