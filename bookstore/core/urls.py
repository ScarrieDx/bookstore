from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('books.urls')),
    re_path(r'^', include ('homepage.urls'))
    ]
   


