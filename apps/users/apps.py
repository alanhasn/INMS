from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.users'


    # import the signals module
    def ready(self):
        import apps.users.signals.profile_signals

