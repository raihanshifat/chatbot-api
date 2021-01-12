from django.urls import path,include
from . import views
app_name='api'

urlpatterns = [
    path('api',views.collect_response,name='collect_response'),
]