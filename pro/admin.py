from django.contrib import admin

# Register your models here.
from .models import ProInfo, TaskInfo, EventInfo
from django.utils import timezone
from .models import FINISHJOB, MIDDLEPRI
from django.contrib import messages


class TaskInfoInline(admin.TabularInline):
	model = TaskInfo
	ordering = ('task_status', 'task_mtime' )
	fieldsets = [(None, {'fields':['task_name','task_dealer', 'task_status', 'task_mtime', 'task_note']})]
	extra = 0


class EventInfoInline(admin.TabularInline):
	model   = EventInfo
	extra   = 0


@admin.register(ProInfo)
class ProInfoAdmin(admin.ModelAdmin):
	inlines	 = (EventInfoInline,)
	list_display	= ('pro_name', 'province', 'pro_ctime', 'pro_link', 'get_event_status')
	search_fields   = ('pro_name', )
	list_filter		= ('province', )


@admin.register(EventInfo)
class EventInfoAdmin(admin.ModelAdmin):
	inlines		 = (TaskInfoInline,)
	list_display	= ('pro', 'event_name', 'event_ctime', 'event_priority', 'get_task_status')
	search_fields   = ('event_name',)
	list_filter     = ('pro', 'event_priority',)
	ordering		= ('event_priority', 'pro', 'event_ctime')
	list_editable   = ('event_priority', )


@admin.register(TaskInfo)
class TaskInfoAdmin(admin.ModelAdmin):
	ordering	   = ('task_status', 'task_id' )
	list_filter	   = ('task_id__pro', 'task_id', 'task_status', 'task_dealer', 'task_mtime')
	list_display   = ('get_pro_name', 'task_id', 'task_dealer', 'task_name', 'task_status', 'task_mtime', 'task_note')
	list_editable  = ('task_status', )
	search_fields  = ('task_name',)
	date_hierarchy = ('task_mtime')

	def save_model(self, request, obj, form, change):
		if '/add/' in request.META['PATH_INFO']:
			obj.task_dealer_id = request.user.num
		elif not request.user.is_superuser or not obj.task_dealer_id == request.user.num:
			messages.error(request, "you cannot change other staff task message!")
			messages.set_level(request, messages.ERROR)
			return
		obj.save()

