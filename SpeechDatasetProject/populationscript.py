import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SpeechDatasetProject.settings")

import django
django.setup()

from django.core.management import call_command
from essential_generators import DocumentGenerator
from app.models import Dataset

gen=DocumentGenerator()

N=10
punc = '''!()-[]{};:-'"\,<>./?@#$%^&*_~'''
def preprocess(s):
    for ele in s:
        if ele in punc:
            s = s.replace(ele, "")
    
    s=s.upper()
    result = ''.join([i for i in s if not i.isdigit()])
    return result
        

for i in range(N):
    s=gen.sentence()
    s=preprocess(s)
    if len(s)>50:
        data=Dataset(transcript=s)
        data.save()
