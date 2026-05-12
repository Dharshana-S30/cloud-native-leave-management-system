from django.urls import path
from .views import employee_dashboard, manager_dashboard, apply_leave, my_leaves
from .views import apply_leave, manager_leaves, update_status

urlpatterns = [
    path('employee/', employee_dashboard, name='employee_dashboard'),
    path('manager/', manager_dashboard, name='manager_dashboard'),
    path('apply/', apply_leave, name='apply_leave'),
    path('my-leaves/', my_leaves, name='my_leaves'),
    path('manager-leaves/', manager_leaves, name='manager_leaves'),
path('update-status/<int:id>/<str:status>/', update_status, name='update_status'),
]