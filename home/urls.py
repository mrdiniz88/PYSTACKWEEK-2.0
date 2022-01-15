from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('building/<str:id>', views.building, name="building"),
    path('schedule_visit', views.schedule_visit, name="schedule_visit"),
    path('scheduling', views.scheduling, name="scheduling"),
    path('cancel_scheduling/<str:id>', views.cancel_scheduling, name="cancel_scheduling")

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)