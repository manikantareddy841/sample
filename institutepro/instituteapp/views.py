from django.shortcuts import render
from .models import coursesdata,feedback,contactdata
from .forms import feedbackform,contactform
from django.http.response import HttpResponse

def home(request):
    return render(request,'instituteapp/home.html')
def contacts(request):
    if request.method=='POST':
        cform=contactform(request.POST)
        if cform.is_valid():
            name=cform.cleaned_data.get('name')
            mobile=cform.cleaned_data.get('mobile')
            email=cform.cleaned_data.get('email')
            courses=cform.cleaned_data.get('courses')
            trainers=cform.cleaned_data.get('trainers')
            locations=cform.cleaned_data.get('locations')
            shifts=cform.cleaned_data.get('shifts')
            gender=cform.cleaned_data.get('gender')
            start_date=cform.cleaned_data.get('start_date')
            data=contactdata(
                name=name,
                mobile=mobile,
                email=email,
                courses=courses,
                trainers=trainers,
                locations=locations,
                shifts=shifts,
                gender=gender,
                start_date=start_date
            )
            data.save()
            cform=contactform()
            context={'cform':cform}
            return render(request,'instituteapp/contact.html',context)
    else:
        cform=contactform()
        context={'cform':cform}
        return render(request,'instituteapp/contact.html',context)

# Create your views here.
def services(request):
    courses=coursesdata.objects.all()
    context={'courses':courses}
    return render(request,'instituteapp/services.html',context)

def feedbacking(request):
    if request.method=='POST':
        fform=feedbackform(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            rating=request.POST.get('rating')
            feed=request.POST.get('feedback')
            data=feedback(
                name=name,
                rating=rating,
                feedback=feed
            )
            data.save()
            fform=feedbackform()
            feedbacks=feedback.objects.all()
            return render(request,'instituteapp/feedback.html',{'fform':fform,'feedbacks':feedbacks})
    else:
        fform=feedbackform()
        feedbacks=feedback.objects.all()
        return render(request,'instituteapp/feedback.html',{'fform':fform,'feedbacks':feedbacks})
def gallery(request):
    return render(request,'instituteapp/gallery.html')