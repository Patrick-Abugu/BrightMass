from django.contrib import admin
from .models import Post, Feedback

class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "user", "date", )
    list_filter = ("date", )
    search_field = ["title", "body"]
    prepopulated_field = {"slug": ('title')}

'''class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("subject", "email")
    list_filter =("date",)
    search_field = ["subject", "email"]
admin.site.register(Feedback, FeedbackAdmin)'''
admin.site.register(Post,PostAdmin,)
