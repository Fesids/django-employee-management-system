
from django.contrib import admin
from django.urls import path, include
from accounts.views import HomePage


urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("", HomePage.as_view(), name="home"),

    # api
    path('api/', include("api.urls")),
    path("", include("rest_framework.urls"))

]
