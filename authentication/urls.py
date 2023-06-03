from django.urls import path

from authentication import views

app_name = 'authentication'

urlpatterns = [
    path("", views.login_view, name='login_view')

]
