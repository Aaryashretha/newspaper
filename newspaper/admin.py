from django.contrib import admin

from newspaper.models import Category, Post, Tag,Contact,UserProfile,Comment,Newsletter
admin.site.register(Tag)
admin.site.register(Category)
# admin.site.register(Post)
admin.site.register(Contact)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Newsletter)

class PostAdmin(admin.ModelAdmin):
    list_display = ["title" ,"author" ,"category"]
    date_hierarchy = "published_at"

admin.site.register(Post, PostAdmin)