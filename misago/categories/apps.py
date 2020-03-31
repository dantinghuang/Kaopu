from django.apps import AppConfig


class MisagoCategoriesConfig(AppConfig):
    name = "misago.categories"
    label = "misago_categories"
    verbose_name = "Kaopu Categories"

    def ready(self):
        from . import signals as _
