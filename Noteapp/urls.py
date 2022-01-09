from django.urls import path , include
from . import views
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name="index" ),
    path('<int:id>/delete/',views.delete,name="home" ),
    path('api/', include('api.urls')),
    path('login/',views.loginUser,name='login'),
    path('signup/',views.createUser,name='SignUp'),
    path('logout/',views.logout_view,name='logout'),
    # path('UserLoggedin/',views.UserLoggedin,name='UserLoggedin')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns =+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
