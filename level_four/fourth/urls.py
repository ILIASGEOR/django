from fourth import views
from django.urls import path

# SET THE NAMESPACE!
app_name = 'fourth'

urlpatterns = [
    path('relative/',views.relative,name="relative"),
    path('other/',views.other,name="other"),
]