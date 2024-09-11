# myapp/apps.py
from django.apps import AppConfig

class MyappConfig(AppConfig):
    name = 'myapp'

    def ready(self):
        # Import the signals so they are registered when the app is ready
        import myapp.signals
