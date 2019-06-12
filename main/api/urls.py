from django.urls import path
from rest_framework.routers import DefaultRouter
from api.views import OrganizationView, DepartmentView, EmployeeView, StatusView

router = DefaultRouter()
router.register('organization', OrganizationView, base_name='organization')
router.register('department', DepartmentView, base_name='department')
router.register('employee', EmployeeView, base_name='employee')
router.register('status', StatusView, base_name='status')
urlpatterns = router.urls
