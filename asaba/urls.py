from django.contrib import admin
from django.urls import path, include

from feedback import views
from users import views as userViews
from django.contrib.auth import views as defaultViews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', userViews.register, name='register'),
    path('profile/', userViews.profile, name='profile'),
    path('user/', defaultViews.LoginView.as_view(template_name='users/html/users.html'), name='user'),
    path('exit/', defaultViews.LogoutView.as_view(template_name='users/html/exit.html'), name='exit'),
    path('pass-reset/', defaultViews.PasswordResetView.as_view(template_name='users/html/pass_reset.html'),
         name='pass-reset'),
    path('password_reset_complete/', defaultViews.PasswordResetCompleteView.as_view(template_name='users/html/password_reset_complete.html'),
         name='password_reset_complete'),
    path('password_reset_confirm/<uidb64>/<token>/',
         defaultViews.PasswordResetConfirmView.as_view(template_name='users/html/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password_reset_done',
         defaultViews.PasswordResetDoneView.as_view(template_name='users/html/password_reset_done.html'),
         name='password_reset_done'),
    path('', include('blog.urls')),
    path('call-back/', views.contactView, name='call-back'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
