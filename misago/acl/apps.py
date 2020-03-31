from django.apps import AppConfig

from .providers import providers


class MisagoACLsConfig(AppConfig):
    name = "misago.acl"
    label = "misago_acl"
    verbose_name = "Kaopu ACL framework"

    def ready(self):
        providers.load()
