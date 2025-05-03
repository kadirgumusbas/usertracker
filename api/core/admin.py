from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'created_at',)
    fields = ('title', 'body', 'user', 'created_at',)
    search_fields = ('title', 'body',)
    list_display_links = ('title',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

    class Meta:
        model = Post


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id','post', 'name', 'created_at',)
    fields = ('name','post', 'body','created_at',)
    search_fields = ('name', 'body',)
    list_filter = ('created_at',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at',)

    class Meta:
        model = Comment

class AlbumAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'user', 'created_at',)
    list_display_links = ('title',)
    fields = ('title', 'user', 'created_at',)
    readonly_fields = ('created_at', )

    class Meta:
        model = Album

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'album','title', 'image', 'created_at',)
    list_display_links = ('title',)
    fields = ('album', 'title', 'image', 'created_at',)
    readonly_fields = ('created_at',)

    class Meta:
        model = Photo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created_at', )
    fields = ('title', 'user', 'created_at', 'completed',)
    readonly_fields = ('created_at', )

    class Meta:
        model = Todo

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['name', 'username', 'email', 'name', 'phone', 'website', 'is_staff']

    fieldsets = UserAdmin.fieldsets + (
        ('Ek Alanlar', {
            'fields': ('name', 'phone', 'website', 'address', 'company')
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Ek Alanlar', {
            'fields': ('name', 'phone', 'website', 'address', 'company')
        }),
    )

admin.site.register(Address)
admin.site.register(Geo)
admin.site.register(Company)
admin.site.register(Todo, TodoAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Photo, PhotoAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
