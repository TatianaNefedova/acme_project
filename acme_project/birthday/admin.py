from django.contrib import admin

from .models import Birthday, Tag


class BirthdayAdmin(admin.ModelAdmin):
    model = Birthday


class TagAdmin(admin.ModelAdmin):
    model = Tag


admin.site.register(Birthday, BirthdayAdmin)
admin.site.register(Tag, TagAdmin)
