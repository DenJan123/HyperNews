from django.conf import settings
import json
from django import forms


def read_json_data():
    with open(settings.NEWS_JSON_PATH, 'r') as afile:
        data = json.load(afile)
    return data


def save_json_data(data):
    with open(settings.NEWS_JSON_PATH, 'w') as afile:
        json.dump(data, afile)





class NewsCreateForm(forms.Form):
    title = forms.CharField(max_length=100)
    text = forms.CharField(max_length=1024)
    # link = forms.IntegerField(widget=forms.HiddenInput)
    # created = forms.DateField(widget=forms.HiddenInput)



def append_to_file(news_form, file_path):
    with open(file_path, 'a') as afile:
        afile.write('')
