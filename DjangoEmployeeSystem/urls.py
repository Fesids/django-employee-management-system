
from django.contrib import admin
from django.urls import path, include
from accounts.views import HomePage
from rest_framework_simplejwt import views as jwt_views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/", include("accounts.urls")),
    path("", HomePage.as_view(), name="home"),
    path("employee_profile/", include("employee_profile.urls")),

    # api
    path('api/', include("api.urls")),
    path("token", jwt_views.TokenObtainPairView.as_view()),

    path("", include("rest_framework.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(
    url_name="schema"), name="swagger-ui")

]
