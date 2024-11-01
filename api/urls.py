from django.urls import path
from .views.resident_view import (
    GetResidentsView,
    PaginateResidentsView,
    FindResidentView,
    CreateResidentView,
    DeleteResidentView,
    UpdateResidentView,
    VerifyResidentView,
    GenerateDummyResidentsView,
)

from .views.auth_view import (
    LoginView,
    AdminRegisterView,
    ResidentRegisterView,
    GenerateAdminAccountView,
)

from .views.department_view import (
    GetDepartmentsView,
    GenerateDepartmentsView,
    GetAvailableCountView,
    CreateDepartmentView,
    DeleteDepartmentView,
    UpdateDepartmentView,
    SetToAvailable,
)

from .views.alert_view import (
    ListAlertsView,
    CreateAlertView,
    DeleteAlertView,
    FindAlertView,
    SendSmsView,
    SendEmailView
)

urlpatterns = [
    path('account/generate', GenerateAdminAccountView.as_view(), name='generate-admin'), # post
    path('residents/generate/<int:count>', GenerateDummyResidentsView.as_view(), name='generate-residents'),  # post
    
    path('residents', GetResidentsView.as_view(), name='get-residents'),  # get
    path('residents/paginate', PaginateResidentsView.as_view(), name='paginate-residents'),  # get
    path('residents/<uuid:pk>', FindResidentView.as_view(), name='find-resident'), # get/id
    path('residents/create', CreateResidentView.as_view(), name='create-resident'), # post
    path('residents/delete/<uuid:pk>', DeleteResidentView.as_view(), name='delete-resident'), # delete
    path('residents/update/<uuid:pk>', UpdateResidentView.as_view(), name='update-resident'), # put/patch
    path('residents/verify/<uuid:pk>', VerifyResidentView.as_view(), name='verify-resident'), # patch
    
    path('auth/login', LoginView.as_view(), name='admin-login'), # post
    path('auth/register/admin', AdminRegisterView.as_view(), name='admin-register'), # post
    path('auth/register/resident', ResidentRegisterView.as_view(), name='resident-register'), # post
    
    path('departments', GetDepartmentsView.as_view(), name='get-departments'),
    path('departments/generate', GenerateDepartmentsView.as_view(), name='generate-departments'), # post
    path('departments/create', CreateDepartmentView.as_view(), name='create-department'), # post
    path('departments/delete/<uuid:pk>', DeleteDepartmentView.as_view(), name='delete-department'), # delete
    path('departments/update/<uuid:pk>', UpdateDepartmentView.as_view(), name='update-department'), # put/patch
    path('departments/available-count', GetAvailableCountView.as_view(), name='get-available'), # get
    path('departments/set-available/<uuid:pk>', SetToAvailable.as_view(), name='set-available'), # post
    
    path('alerts', ListAlertsView.as_view(), name='list-alert'), # get
    path('alerts/delete/<uuid:pk>', DeleteAlertView.as_view(), name='delete-alert'), # delete
    path('alerts/<uuid:pk>', FindAlertView.as_view(), name='find-alert'), # get
    path('send-alert', CreateAlertView.as_view(), name='send-alert'), # post
    path('send-sms', SendSmsView.as_view(), name='send-sms'), # post
    
    # not working yet
    path('send-email', SendEmailView.as_view(), name='send-sms'), # post
]

#test
