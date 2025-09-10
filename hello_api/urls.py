from django.contrib import admin
from django.urls import path
from api.views import HelloWorld

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HelloWorld.as_view()),   # Root path
    path('hello/', HelloWorld.as_view()),
]
