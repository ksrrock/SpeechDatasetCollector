
from django.shortcuts import redirect, render
from app.models import Dataset
from django.contrib import messages


def index(request):
    if request.method=='POST':
        transcript=request.POST.get('transcript')
        print(transcript)
        audio=request.FILES.get('audio')
        extension=str(audio.name)
        if extension.endswith('flac')==False:
            messages.error(request,'Invalid file format(Audio must of type .flac)')
            return redirect('index')
        else:
            obj=Dataset.objects.get(transcript=transcript)
            obj.audio=audio
            obj.save()
            messages.success(request, 'File upload successful')
            return redirect('index')
    data_list=Dataset.objects.all().order_by('id')
    count=0
    for item in data_list:
        if item.audio:
            pass
        else:
            count+=1
    data_list=data_list[:100]
    count=len(data_list)
    context={"data":data_list, "count" : count}
    return render(request,"app/index.html",context=context)


def next_index(request):
    if request.method=='POST':
        transcript=request.POST.get('transcript')
        print(transcript)
        audio=request.FILES.get('audio')
        extension=str(audio.name)
        if extension.endswith('flac')==False:
            messages.error(request,'Invalid file format(Audio must of type .flac)')
            return redirect('index')
        else:
            obj=Dataset.objects.get(transcript=transcript)
            obj.audio=audio
            obj.save()
            messages.success(request, 'File upload successful')
            return redirect('secondindex')
    data_list=Dataset.objects.all().order_by('id')
    data_list=data_list[100:200]
    count=0
    for item in data_list:
        if item.audio:
            pass
        else:
            count+=1

    context={"data":data_list, "count" : count}
    return render(request,"app/next_index.html",context=context)


def next_next_index(request):
    if request.method=='POST':
        transcript=request.POST.get('transcript')
        print(transcript)
        audio=request.FILES.get('audio')
        extension=str(audio.name)
        if extension.endswith('flac')==False:
            messages.error(request,'Invalid file format(Audio must of type .flac)')
            return redirect('index')
        else:
            obj=Dataset.objects.get(transcript=transcript)
            obj.audio=audio
            obj.save()
            messages.success(request, 'File upload successful')
            return redirect('secondindex')
    data_list=Dataset.objects.all().order_by('id')
    data_list=data_list[200:]
    count=0
    for item in data_list:
        if item.audio:
            pass
        else:
            count+=1

    context={"data":data_list, "count" : count}
    return render(request,"app/next_next_index.html",context=context)