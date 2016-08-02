from django.shortcuts import render

from django.core import serializers
from  django.http import HttpResponse
from django.utils import timezone
import datetime
from wordproject.models import WordRecord


def word_json(request):
    words = WordRecord.objects.all()
    data = serializers.serialize("json", words)
    return HttpResponse(data, content_type='application/json')
	
def word_json_update(request, year, month, day):
    first_date = datetime.date(int(year), int(month), int(day))
    last_date = timezone.now()
    words = WordRecord.objects.filter(dateUpdated__range=(first_date, last_date))
    data = serializers.serialize("json", words)
    return HttpResponse(data, content_type='application/json')
