from django.http import Http404
from wordproject.models import WordRecord
from wordproject.models import WordPair
from wordproject.models import Sound
from wordproject.models import SoundPair
from rest_framework import status
from rest_framework.response import Response
from wordproject.serializers import WordRecordSerializer
from wordproject.serializers import WordPairSerializer
from wordproject.serializers import SoundPairSerializer
from wordproject.serializers import SoundSerializer
from rest_framework.views import APIView
from rest_framework import generics
from datetime import date
from itertools import chain


class WordRecordList(APIView):
    def get(self, request, format=None):
        wordRecords = WordRecord.objects.all()
        wordPairs = WordPair.objects.all()
        sound = Sound.objects.all()
        soundPairs = SoundPair.objects.all()

        # serializing queryset objects
        wordRecordSerializer = WordRecordSerializer(wordRecords, many=True)
        wordPairSerializer = WordPairSerializer(wordPairs, many=True)
        soundSerializer = SoundSerializer(sound, many=True)
        soundPairSerializer = SoundPairSerializer(soundPairs, many=True)

        # returning serialized data
        return Response({
            'WordRecord': wordRecordSerializer.data,
            'WordPair': wordPairSerializer.data,
            'Sound': soundSerializer.data,
            'SoundPair': soundPairSerializer.data,
        })


class WordRecordDetail(APIView):
    def get_object(self, id):
        try:
            return WordRecord.objects.get(id=id)
        except WordRecord.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        wordRecord = self.get_object(id)
        serializer = WordRecordSerializer(wordRecord)
        return Response(serializer.data)


class WordRecordFilteredList(generics.ListAPIView):
    serializer_class = WordRecordSerializer

    def get_queryset(self):
        """self.kwargs gets the field from the url"""
        ew = self.kwargs['englishWord']
        querySet = WordRecord.objects.filter(englishWord=ew)
        return querySet


class WordRecordQueryParamList(generics.ListAPIView):
    # user must supply the last sync date
    def get_queryset(self):
        """pulling terms out from the query parameters"""
        searchYear = self.request.query_params.get('afterYear', None)
        # if no year param provided, return 404
        if searchYear is None:
            raise Http404

        searchMonth = self.request.query_params.get('afterMonth', None)
        # if no month param provided, default to January
        if searchMonth is None:
            searchMonth = 1

        searchDate = self.request.query_params.get('afterDate', None)
        # if no Date param provided, default to 1st of the month
        if searchDate is None:
            searchDate = 1

        userSearchDate = date(int(searchYear), int(searchMonth), int(searchDate))

        query1 = WordRecord.objects.filter(dateUpdated__gt=userSearchDate)
        query2 = WordPair.objects.filter(dateUpdated__gt=userSearchDate)

        serializer1 = WordRecordSerializer(query1, many=true)

        querySet = chain(query1, query2)
        return Response({
            'wordrecord': query1.data,
        })


class WordPairList(generics.ListAPIView):
    serializer_class = WordPairSerializer

    def get_queryset(self):
        """self.kwargs gets the field from the url"""
        querySet = WordPair.objects.all()
        return querySet
