from django.contrib import admin

# Register your models here.
from .models import TaskInfo, EventInfo
from datetime import datetime


class TaskInfoInline(admin.TabularInline):
	model = TaskInfo
	ordering = ('task_status', 'task_mtime' )
	extra = 0


@admin.register(EventInfo)
class EventInfoAdmin(admin.ModelAdmin):
	list_display = ('event_name', 'event_status')
	search_fields = ('event_name', )
	list_filter = ('event_status', )
	inlines = [TaskInfoInline]


@admin.register(TaskInfo)
class TaskInfoAdmin(admin.ModelAdmin):
	ordering       = ('task_status', 'task_mtime' )
	list_filter    = ('task_status', 'task_mtime')
	list_display   = ('task_id', 'task_name', 'task_status', 'task_mtime', 'task_note')
	list_editable  = ('task_status', 'task_note')
	search_fields  = ('task_name',)
	date_hierarchy = ('task_mtime')

	def save_model(self, request, obj, form, change):
		obj.task_atime = datetime.now()
		obj.save()

