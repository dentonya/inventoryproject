"""inventoryproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include
from user import views as user_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('dashboard.urls')),
    url(r'^register/', user_view.register, name='user-register'),
    url(r'^profile/', user_view.profile, name='user-profile'),
    url(r'^profile/update', user_view.profile_update, name='user-profile-update'),
    url(r'', auth_views.LoginView.as_view(template_name='user/login.html'), name='user-login'),
    url(r'^password/reset/', auth_views.PasswordChangeView.as_view(template_name='user/password_reset.html'), name='user-password-reset'),
    url(r'^logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user-logout'),
    url(r'^password/reset/done', auth_views.PasswordResetDoneView.as_view(template_name='user/password_reset_done.html'), name='user-password-reset-done'),
    url(r'^password/reset/confirm', auth_views.PasswordResetConfirmView.as_view(template_name='user/password_reset_confirm.html'), name='user-password-reset-confirm'),
    url(r'^password/reset/complete', auth_views.PasswordResetCompleteView.as_view(template_name='user/password_reset_complete.html'), name='user-password-reset-complete'),






] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
