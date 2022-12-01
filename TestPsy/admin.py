from django.contrib import admin
from . import models


class QuestsAdmin(admin.ModelAdmin):
    list_display = ('text', 'factor', 'number')


admin.site.register(models.Quests, QuestsAdmin)
admin.site.register(models.Answers)
admin.site.register(models.Results)

from django.contrib import admin

# Register your models here.
