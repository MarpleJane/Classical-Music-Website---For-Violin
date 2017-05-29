from django.contrib import admin

# Register your models here.
from garrett import models

class singerSongs(admin.ModelAdmin):
    list_display = ('songName', 'singerID')


class commentAdmin(admin.ModelAdmin):
    list_display = ('songID', 'account', 'body')

admin.site.register(models.users)
admin.site.register(models.authors)
admin.site.register(models.songs, singerSongs)
admin.site.register(models.commentPost, commentAdmin)
