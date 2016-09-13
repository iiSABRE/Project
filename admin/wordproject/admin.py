from django.contrib import admin

from .models import WordRecord, Sound, SoundPair, WordPair


# Might want to rename this but it allows us to assign the wordPairs in the words I think.
class WordCustom(admin.StackedInline):
    model = WordPair
    fk_name = 'translation'


class WordRecordAdmin(admin.ModelAdmin):
    inlines = [WordCustom]
    list_display = ['word', 'language' , 'Translation_Language', 'Translation', 'dateCreated', 'dateUpdated', 'publish']
    search_fields = ('word', 'language')
    list_filter = ('language',)
	
    def Translation_Language(self, obj):
         b = WordPair.objects.filter(original=obj.id).values('translation')
         c = WordRecord.objects.filter(id=b)
         if c: 
             return c[0].language
         else:
             return "-"	
	
    def Translation(self, obj):
         b = WordPair.objects.filter(original=obj.id).values('translation')
         c = WordRecord.objects.filter(id=b)
         if c: 
             return c[0].word
         else:
             return "-"		 


class SoundAdmin(admin.ModelAdmin):
    list_display = ['blob']


class SoundPairAdmin(admin.ModelAdmin):
    list_display = ['wordpair', 'sound']


admin.site.register(WordRecord, WordRecordAdmin)
admin.site.register(Sound, SoundAdmin)
admin.site.register(SoundPair, SoundPairAdmin)
