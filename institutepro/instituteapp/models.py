from django.db import models
from multiselectfield import MultiSelectField

class coursesdata(models.Model):
    course_name=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    start_data=models.DateField(max_length=100)
    start_time=models.TimeField(max_length=100)
    trainer_name=models.CharField(max_length=100)
    trainer_exp=models.CharField(max_length=100)
    content=models.FileField(upload_to='contents',max_length=100)
class feedback(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    date=models.DateTimeField(auto_now_add=True)
    feedback=models.CharField(max_length=200)

class contactdata(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)
    courses_choices=(
        ('python','python'),
        ('django','django'),
        ('ui','ui'),
        ('restapi','restapi'),
        ('flask','flask'),
        ('mysql','mysql')
    )
    courses=MultiSelectField(max_length=200,choices=courses_choices)
    trainers_choices=(
        ('narayana','narayana'),
        ('mahesh','mahesh'),
        ('mohanreddy','mohanreddy'),
        ('srinivas','srinivas'),
        ('wilison','wilison')
    )
    trainers=MultiSelectField(max_length=200,choices=trainers_choices)
    location_choices=(
        ('hyd','hyd'),
        ('bang','bang'),
        ('pune','pune'),
        ('delhi','delhi'),
        ('chennai','chennai')
    )
    locations=MultiSelectField(max_length=200,choices=location_choices)
    shifts_choices=(
        ('morning','morning'),
        ('afternoon','afternoon'),
        ('evening','evening'),
        ('night','night')
    )
    shifts=MultiSelectField(max_length=100,choices=shifts_choices)
    gender=models.CharField(max_length=100)
    start_date=models.DateField(max_length=100)
# Create your models here.
