from .views import EmployeeViewSet, SalaryViewSet, DepartmentViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("employees", EmployeeViewSet)
router.register("salaries", SalaryViewSet)
router.register("departments", DepartmentViewSet)

urlpatterns = router.urls