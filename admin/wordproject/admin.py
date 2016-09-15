from django.contrib import admin
from django.utils.html import linebreaks

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
         b = WordPair.objects.filter(translation=obj.id)
         if b:
            #for wordpair in b:
               #c = WordRecord.objects.filter(word = wordpair.translation)
               return b
         else:
               return "-"
    Translation_Language.allow_tags = True
	
    def Translation(self, obj):
         b = WordPair.objects.filter(translation=obj.id)
		 c = WordPair.objects.values_list('original')
         if c:
            #for wordpair in b:
               #return linebreaks(wordpair.original)
			   return c
         else:
               return "-"
    Translation.allow_tags = True	 


class SoundAdmin(admin.ModelAdmin):
    list_display = ['blob']


class SoundPairAdmin(admin.ModelAdmin):
    list_display = ['wordpair', 'sound']


admin.site.register(WordRecord, WordRecordAdmin)
admin.site.register(Sound, SoundAdmin)
admin.site.register(SoundPair, SoundPairAdmin)
