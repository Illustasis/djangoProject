from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('API/System/', include(('System.urls', 'System'))),
    path('API/book/', include(('book.urls', 'book'))),

]
