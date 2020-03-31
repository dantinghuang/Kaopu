from django.conf.urls import url

from .. import admin
from .views import auth, index

urlpatterns = [
    # "misago:admin:index" link symbolises "root" of Kaopu admin links space
    # any request with path that falls below this one is assumed to be directed
    # at Kaopu Admin and will be checked by Kaopu Admin Middleware
    url(r"^$", index.admin_index, name="index"),
    url(r"^logout/$", auth.logout, name="logout"),
]

# Discover admin and register patterns
admin.discover_misago_admin()
urlpatterns += admin.urlpatterns()
