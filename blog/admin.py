from django.contrib import admin
from .models import Topic,Article,Comment

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ("id","name","created_at")
    search_fields = ("name",)
    # Python tuple из одного элемента пишется с запятой: ("name",)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "author", "created_at")
    search_fields = ("title", "content", "author__username", "topics__name")
    list_filter = ("topics", "created_at")

    # def short_content(self, obj):
    #     return obj.content[:50] + "..." if len(obj.content) > 50 else obj.content

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "article", "created_at")
    search_fields = ("text", "author__username", "article__title")
    list_filter = ("created_at",)
