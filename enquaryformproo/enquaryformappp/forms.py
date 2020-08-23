from django import forms
from multiselectfield import MultiSelectFormField
class enquaryform(forms.Form):
    name=forms.CharField(
        label='Enter your name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )
    mobile=forms.IntegerField(
        label="Enter your mobilr number",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'your mobile number'
            }
        )
    )
    email=forms.EmailField(
        label="Enter your email address",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your email field'
            }
        )
    )
    courses_choices=(
        ('python','python'),
        ('django','django'),
        ('ui','ui'),
        ('restapi','restapi')

    )
    courses=MultiSelectFormField(choices=courses_choices,label="select required courses")

    trainers_choices=(
        ('mani','mani'),
        ('chinna','chinna'),
        ('siva','siva')

    )
    trainers=MultiSelectFormField(choices=trainers_choices,label="select required trainer")

    location_choices=(
        ('srnagar','srnagar'),
        ('madhapur','madhapur'),
        ('kphb','kphb')
    )
    locations=MultiSelectFormField(choices=location_choices,label='select required location')

    gender_choices=(
        ('male','male'),
        ('female','female')
    )
    gender=forms.ChoiceField(
        choices=gender_choices,
        widget=forms.RadioSelect()
    )
    start_date=forms.DateField(
        widget=forms.SelectDateWidget()
    )

