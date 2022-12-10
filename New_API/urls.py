from django.urls import path
from New_API import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('Person',views.PersonRoot)
router.register('Address',views.AddressRoot)


