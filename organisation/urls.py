from django.urls import path
from organisation import views

urlpatterns = [
    path('', views.organisation, name="organisation"),
    path('add/', views.addorg, name="addorg"),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('activated/', views.activated, name='activated'),
]
