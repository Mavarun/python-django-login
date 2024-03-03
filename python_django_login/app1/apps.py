# from django.apps import AppConfig


# class App1Config(AppConfig):
#     name = 'app1'
from django.apps import AppConfig
from django.db.models.signals import post_migrate


def create_groups(sender, **kwargs):
    from django.contrib.auth.models import Group

    app_label = sender.label  # Retrieve the app label using the sender object

    if app_label == 'app1':
        # Create 'patient' group if it doesn't exist
        patient_group, created = Group.objects.get_or_create(name='patient')

        # Create 'doctor' group if it doesn't exist
        doctor_group, created = Group.objects.get_or_create(name='doctor')


class App1Config(AppConfig):
    name = 'app1'

    def ready(self):
        post_migrate.connect(create_groups, sender=self)