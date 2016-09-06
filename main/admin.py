from django.contrib import admin
from .models import Review
from .models import AboutMe
from .models import Story
from .models import News
from .models import Email


def make_confirmed(model, request, queryset):
    print(queryset)
    queryset.update(confirmed=True)
make_confirmed.short_description = "Подтвердить выбранные Отзывы"


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("confirmed", "is_answered", "user_name", "user_town", "user_text", "created_date", "to_main")
    readonly_fields = ("user_name", "user_town", "user_text", "created_date")
    actions = [make_confirmed]
    list_filter = ("confirmed", )
    def is_answered(self, obj):
        return ("Нет", "Да")[True if len(obj.answer_text) else False]
    is_answered.short_description = "Написан ответ"


class AboutMeAdmin(admin.ModelAdmin):
    list_display = ("user_field", "user_data")


class StoryAdmin(admin.ModelAdmin):
    list_display = ("story_year", "story_text")


class NewsAdmin(admin.ModelAdmin):
    list_display = ("news_name", "news_date", "news_image")


admin.site.register(Review, ReviewAdmin)
admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Story, StoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Email)
