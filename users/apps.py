from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'
    def ready(ready):
        import users.signals