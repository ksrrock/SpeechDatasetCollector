import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SpeechDatasetProject.settings")

import django
django.setup()

from app.models import Dataset
from essential_generators import DocumentGenerator
gen=DocumentGenerator()


punc = '''!()-[]{};:-'"\,<>./?@#$%^&*_~'''
def preprocess(s):
    for ele in s:
        if ele in punc:
            s = s.replace(ele, "")
    
    s=s.upper()
    result = ''.join([i for i in s if not i.isdigit()])
    return result
        

def solve(N):
    for i in range(N):
        s=gen.sentence()
        s=preprocess(s)
        if len(s)>30 and len(s)<70:
            data=Dataset(transcript=s)
            data.save()

solve(200)
dataset_list=Dataset.objects.all()

for item in dataset_list:
    item.transcript=item.transcript.lower()
    item.save()

for item in dataset_list:
    if item.audio:
        print(item.transcript)