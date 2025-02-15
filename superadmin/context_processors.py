from superadmin.models import notifications



def notif(request):
    n = notifications.objects.all()
    total_unread = notifications.objects.filter(true=False).count()  # Count False values
    return {'n': n, 'total_unread': total_unread}