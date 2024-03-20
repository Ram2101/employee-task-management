from django.core.mail import send_mail
from django.contrib import admin
from .models import Task

def send_task_update_email(request, obj):
    subject = 'Task Updated'
    message = f'Hello {obj.user.get_full_name()},\n\nYour task "{obj.title}" has been updated.'
    send_mail(
        subject=subject,
        message=message,
        from_email=request.user.email,
        recipient_list=[obj.user.email],
        fail_silently=False,
    )


def approve_tasks(modeladmin, request, queryset):
    for task in queryset:
        task.status = 'approved'
        task.save()
        subject = 'Task Approved'
        message = f'Hello {task.user.get_full_name()},\n\nYour task "{task.title}" has been approved.'
        send_mail(
            subject=subject,
            message=message,
            from_email='ugsabariugs@gmail.com',
            recipient_list=[task.email],
            fail_silently=False,
        )
approve_tasks.short_description = 'Approve tasks'

def reject_tasks(modeladmin, request, queryset):
    for task in queryset:
        task.status = 'rejected'
        task.save()
        subject = 'Task Rejected'
        message = f'Hello {task.user.get_full_name()},\n\nYour task "{task.title}" has been rejected.'
        send_mail(
            subject=subject,
            message=message,
            from_email=request.user.email,
            recipient_list=[task.user.email],
            fail_silently=False,
        )
reject_tasks.short_description = 'Reject tasks'



# Register your models here.

from .models import Task

admin.site.register(Task)
def approve_tasks(modeladmin, request, queryset):
    for task in queryset:
        task.status = 'approved'
        task.save()
approve_tasks.short_description = 'Approve tasks'

def reject_tasks(modeladmin, request, queryset):
    for task in queryset:
        task.status = 'rejected'
        task.save()
reject_tasks.short_description = 'Reject tasks'

class TaskAdmin(admin.ModelAdmin):
    list_editable = ('status',)
    actions = [approve_tasks, reject_tasks]
    
    