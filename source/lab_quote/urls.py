from django.urls import path
from lab_quote.views import IndexView


app_name = 'lab_quote'

urlpatterns = [
    path('', IndexView.as_view(), name='index')
]