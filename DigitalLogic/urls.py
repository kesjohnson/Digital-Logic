from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('Launch/', include('Launcher.urls')),
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
]

# urlpatterns += staticfiles_urlpatterns()