from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('coffee_voting/', include('coffee_voting.urls')),
    path('admin/', admin.site.urls),
    path('',  RedirectView.as_view(url='/coffee_voting/')),
]