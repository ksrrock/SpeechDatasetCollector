from django.http.response import HttpResponse
from app.forms import AudioForm
from django.shortcuts import redirect, render
from app.models import Dataset



def index(request):
    if request.method=='POST':
        transcript=request.POST.get('transcript')
        print(transcript)
        audio=request.FILES.get('audio')
        print(type(audio))
        obj=Dataset.objects.get(transcript=transcript)
        obj.audio=audio
        obj.save()
        return redirect('index')
    data_list=Dataset.objects.all()
    context={"data":data_list}
    return render(request,"app/index.html",context=context)


