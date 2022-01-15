from django.contrib import admin
from .models import DayVisit, Timetable, Building, City, Image, Visits

@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ('street', 'value', 'rooms', 'size', 'city', 'kind')
    list_editable = ('value', 'kind')
    list_filter = ('city', 'kind')


admin.site.register(DayVisit)
admin.site.register(Timetable)
admin.site.register(Image)
admin.site.register(City)
admin.site.register(Visits)