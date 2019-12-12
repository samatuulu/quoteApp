from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from api import views
from api.views import LogoutView, RateUPView, RateDownView

router = routers.DefaultRouter()
router.register(r'quote', views.QuoteViewset)

app_name = 'api'

urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('quote/<int:pk>/rate-up/', RateUPView.as_view(), name='rate_up'),
    path('quote/<int:pk>/rate-down/', RateDownView.as_view(), name='rate_down')
]