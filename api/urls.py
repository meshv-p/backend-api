from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register('notes', views.getNotes , basename="getNotes")
router.register('user', views.List) 
# router.register('addnote', views.addnote) 
# router.register('get',views.getdata)
# router.register(r'data',views.getdata)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('api/note',views.Notes),
    # path('UserLoggedin/',views.UserLoggedin,name="userLoggedin")
]

