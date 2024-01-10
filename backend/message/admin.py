from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Rating, UserMessage

# Register your models here.


# @admin.register(Rating)
# class RatingAdmin(admin.ModelAdmin):
#     list_display = ('rating_value',)


@admin.register(UserMessage)
class UserMessageAdmin(admin.ModelAdmin):
    list_display = ('object_id', 'show_id', 'name', 'message', 'rating')
    list_filter = ('show_id', 'name', 'rating')
    search_fields = ('show_id', 'name', 'message', 'rating__rating_value')
