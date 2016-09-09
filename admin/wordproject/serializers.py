from rest_framework import serializers
from wordproject.models import WordRecord
from wordproject.models import WordPair
from wordproject.models import Sound
from wordproject.models import SoundPair


class WordRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordRecord
        fields = ('id', 'word', 'language', 'description', 'dateCreated', 'dateUpdated', 'publish')


class WordPairSerializer(serializers.ModelSerializer):
    translation_word = WordRecordSerializer(many=True, read_only=True)
    original_word = WordRecordSerializer(many=True, read_only=True)

    class Meta:
        model = WordPair
        fields = ('id', 'original', 'translation', 'original_word', 'translation_word')


class SoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sound
        fields = ('blob')


class SoundPairSerializer(serializers.ModelSerializer):
    class Meta:
        model = SoundPair
        fields = ('wordpair', 'sound')
