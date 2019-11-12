from django.contrib import admin

# Register your models here.
from .models import ProInfo, TaskInfo, EventInfo
from django.utils import timezone


class TaskInfoInline(admin.TabularInline):
    model = TaskInfo
    ordering = ('task_status', 'task_mtime' )
    extra = 0


class EventInfoInline(admin.TabularInline):
    model   = EventInfo
    extra   = 0


@admin.register(ProInfo)
class ProInfoAdmin(admin.ModelAdmin):
    inlines     = (EventInfoInline,)
    list_display    = ('pro_name', 'pro_link')


@admin.register(EventInfo)
class EventInfoAdmin(admin.ModelAdmin):
    inlines         = (TaskInfoInline,)
#    list_filter     = ('get_event_status', )
    list_display    = ('pro', 'event_name', 'get_event_status')
    search_fields   = ('event_name', )


@admin.register(TaskInfo)
class TaskInfoAdmin(admin.ModelAdmin):
    ordering       = ('task_status', 'task_mtime' )
    list_filter    = ('task_status', 'task_mtime')
    list_display   = ('task_id', 'task_name', 'task_status', 'task_mtime', 'task_note')
    list_editable  = ('task_status', 'task_note')
    search_fields  = ('task_name',)
    date_hierarchy = ('task_mtime')


