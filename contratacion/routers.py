from rest_framework import routers
from contratacionApp.viewsets import CurrentContractViewSet, PrivateContractViewSet

router = routers.DefaultRouter()

router.register(r'currentContract', CurrentContractViewSet)
router.register(r'privateContract', PrivateContractViewSet)