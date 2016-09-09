from django.db import models


# Change models 23/08/2016

class WordRecord(models.Model):
    word = models.CharField(max_length=100, default='')
    language = models.CharField(max_length=100, default='')
    description = models.TextField(null=True, blank=True, max_length=200)
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return self.word


class WordPair(models.Model):
    original = models.ForeignKey('WordRecord', on_delete=models.CASCADE, related_name='original_word')
    translation = models.ForeignKey('WordRecord', on_delete=models.CASCADE, related_name='translation_word')
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.original.word


class Sound(models.Model):
    blob = models.FileField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)


class SoundPair(models.Model):
    wordpair = models.ForeignKey('WordPair', on_delete=models.CASCADE, )
    sound = models.ForeignKey('Sound', on_delete=models.CASCADE, )
    dateCreated = models.DateTimeField(auto_now_add=True)
    dateUpdated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.wordpair.original


class Meta:
    ordering = ('word',)
