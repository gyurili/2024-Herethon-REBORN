from .models import Notification

def create_notification(user, notification_type, message, post=None):
    Notification.objects.create(user=user, notification_type=notification_type, message=message, post=post)