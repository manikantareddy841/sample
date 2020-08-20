from django import forms
from multiselectfield import MultiSelectFormField
class feedbackform(forms.Form):
    name=forms.CharField(
        label='Enter your name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your name'
            }
        )
    )
    rating = forms.IntegerField(
        label='Enter your rating',
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your rating'
            }
        )
    )
    feedback = forms.CharField(
        label='Enter your feedback',
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your feedback'
            }
        )
    )
class contactform(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )
    mobile = forms.IntegerField(
        label="Enter your moble number",
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your mobile name'
            }
        )
    )
    email = forms.EmailField(
        label="Enter your mail id",
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'your mail'
            }
        )
    )
    courses_choices = (
        ('python', 'python'),
        ('django', 'django'),
        ('ui', 'ui'),
        ('restapi', 'restapi'),
        ('flask', 'flask'),
        ('mysql', 'mysql')
    )
    courses = MultiSelectFormField(max_length=200, choices=courses_choices)

    trainers_choices = (
        ('narayana', 'narayana'),
        ('mahesh', 'mahesh'),
        ('mohanreddy', 'mohanreddy'),
        ('srinivas', 'srinivas'),
        ('wilison', 'wilison')
    )
    trainers = MultiSelectFormField(max_length=200, choices=trainers_choices)
    location_choices = (
        ('hyd', 'hyd'),
        ('bang', 'bang'),
        ('pune', 'pune'),
        ('delhi', 'delhi'),
        ('chennai', 'chennai')
    )
    locations = MultiSelectFormField(max_length=200, choices=location_choices)
    shifts_choices = (
        ('morning', 'morning'),
        ('afternoon', 'afternoon'),
        ('evening', 'evening'),
        ('night', 'night')
    )
    shifts = MultiSelectFormField(max_length=100, choices=shifts_choices)
    gender_choices=(
        ('male','male'),
        ('female','female')
    )
    gender=forms.ChoiceField(
        widget=forms.RadioSelect(),choices=gender_choices,
        label='select your gender'
    )
    start_date=forms.DateField(
        widget=forms.SelectDateWidget()
    )



