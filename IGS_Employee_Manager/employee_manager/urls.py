from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from . import views

router = DefaultRouter()
router.register(r"departments", views.DepartmentViewSet)
router.register(r"employees", views.EmployeeViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("api/token-auth/", obtain_auth_token, name="token_auth"),
    path("employee_list/", views.employee_list, name="employee_list"),
]
