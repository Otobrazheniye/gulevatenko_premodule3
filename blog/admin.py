from django.contrib import admin
from.models import Topic,Article,Comment

@admin.register(Topic)
class Topic(admin.ModelAdmin):
    list_display = ("id","name","created_at")
    search_fields = ("name",)
    #Python tuple из одного элемента пишется c , - ("name",)
    
