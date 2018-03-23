# create a model admin class, then pass it as the second argument to admin.site.register() –
# any time you need to change the admin options for a model.

from django.contrib import admin

from .models import Question,Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3
    # By default, provide enough fields for 3 choices.
    # each time you come back to the “Change” page for an already-created object,
    # you get another three extra slots

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information',
           {'fields': ['pub_date'],'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text','pub_date','was_published_recently')
    list_filter = ['pub_date']
     # adds a “Filter” sidebar that lets people filter the change list
     # by the pub_date field
    search_fields = ['question_text']
     # dds a search box at the top of the change list
# Choice objects are edited on the Question admin page.

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)
