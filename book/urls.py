from django.urls import path
from .views import *

urlpatterns = [
    path('detail', detail),
    path('hot_article', hot_article),
    path('new_article', new_article),

]