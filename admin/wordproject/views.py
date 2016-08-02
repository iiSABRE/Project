from django.shortcuts import render

from django.core import serializers
from  django.http import HttpResponse
from django.utils import timezone
from django.utils import timezone
from wordproject.models import WordRecord


def word_json(request):
    words = WordRecord.objects.all()
    data = serializers.serialize("json", words)
    return HttpResponse(data, content_type='application/json')
	
def word_json_update(request):
    first = datetime.date(2016,1,1)
	last = timezone.now()
    words = WordRecord.objects.filter(dateCreated__range=(first, last)
    data = serializers.serialize("json", words)
    return HttpResponse(data, content_type='application/json')
