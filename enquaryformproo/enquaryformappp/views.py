from django.shortcuts import render
from .models import enquarydata
from .forms import enquaryform
from django.http.response import HttpResponse

#this is view function for enquary form
def enquiryform_view(request):
    if request.method=='POST':
        #eform
        eform=enquaryform(request.POST)
        if eform.is_valid():
            name=eform.cleaned_data.get('name')
            mobile=eform.cleaned_data.get('mobile')
            email=eform.cleaned_data.get('email')
            courses=eform.cleaned_data.get('courses')
            trainers=eform.cleaned_data.get('trainers')
            locations=eform.cleaned_data.get('locations')
            gender=eform.cleaned_data.get('gender')
            start_date=eform.cleaned_data.get('start_date')

            data=enquarydata(
                name=name,
                mobile=mobile,
                email=email,
                courses=courses,
                trainers=trainers,
                locations=locations,
                gender=gender,
                start_date=start_date
            )
            data.save()
            eform=enquaryform()
            return render(request,'enquiryform.html',{'eform':eform})
        else:
            eform=enquaryform()
            return render(request,'enquiryform.html',{'eform':eform})
    else:
        eform=enquaryform()
        return render(request,'enquiryform.html',{'eform':eform})

# Create your views here.
#def   nbxxjhd