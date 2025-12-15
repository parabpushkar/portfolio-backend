from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet
from .views import ContactCreateView

router = DefaultRouter()
router.register('projects', ProjectViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("contact/", ContactCreateView.as_view(), name="contact-create"),
]
