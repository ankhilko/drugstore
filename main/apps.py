from django.apps import AppConfig


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.SmallAutoField'   # поменяли на смол
    name = 'main'
    verbose_name = 'store'



