
from django.shortcuts import redirect, render
from app.models import Dataset
from django.contrib import messages


def index(request):
    if request.method=='POST':
        transcript=request.POST.get('transcript')
        print(transcript)
        audio=request.FILES.get('audio')
        print(type(audio))
        obj=Dataset.objects.get(transcript=transcript)
        obj.audio=audio
        obj.save()
        messages.success(request, 'File upload successful')
        return redirect('index')
    data_list=Dataset.objects.all()
    context={"data":data_list}
    return render(request,"app/index.html",context=context)


