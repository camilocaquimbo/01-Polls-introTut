from django.contrib import admin
from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
  model = Choice
  extra = 3

class QuestionAdmin(admin.ModelAdmin):
    #fields = ['pub_date', 'question_text' ]

    fieldsets = (
        (None, {
            'fields': ['question_text'],
        }),
        ('Date information - Ingrese fecha', {
            'fields': ['pub_date'], 'classes': ['collapse']
        }),
    )
    inlines = [ChoiceInLine]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date'] #filter
    search_fields = ['question_text', 'pub_date']


admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)
