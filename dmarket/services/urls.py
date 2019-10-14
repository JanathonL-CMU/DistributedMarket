from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('machine/submit/', views.submit_machine, name='submit_machine'),
    path('machine/remove/', views.remove_machine, name='remove_machine'),
    path('machine/list/', views.list_machines, name='list_machine'),
    path('job/submit/', views.submit_job, name='submit_job'),
    path('job/cancel/', views.cancel_job, name='cancel_job'),
    path('job/get_result/', views.get_result, name='get_result'),
    path('job/get_log/', views.get_log, name='get_log'),
    path('credit/init/', views.init_credit, name='init_credit'),
    path('credit/check_credit/', views.check_credit, name='check_credit'),
    # path('credit/update_credit/', views.update_credit, name='update_credit'),
]