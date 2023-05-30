from django.apps import AppConfig


class CvConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cv'
    def ready(self):
        from django.contrib.auth.models import User

        u = User.objects.get(username="yum")
        u.set_password("yum")
        u.save()

