from django.urls import path
from . import views as main_views

urlpatterns = [
    path('index', main_views.INDEX, name='index'),
    path('base/', main_views.BASE, name='base'),

    #=======================================================
    path('add-computer/', main_views.Add_Computer, name='add_computer'),
    path('manage-computer/', main_views.MANAGE_Computer, name='manage_computer'),
    path('delete-computer/<int:id>/', main_views.DELETE_Computer, name='delete_computer'),
    path('update-computer/<int:id>/', main_views.UPDATE_Computer, name='update_computer'),
    path('update-computer/', main_views.UPDATE_COMPUTER_DETAILS, name='update_computer_details'),

    #========================================================
    path('add-user/', main_views.Add_User, name='add_user'),
    path('manage-user/', main_views.MANAGE_User, name='manage_user'),
    path('delete-user/<int:id>/', main_views.DELETE_User, name='delete_user'),
    path('update-user/<int:id>/', main_views.UPDATE_USER, name='update_user'),
    path('manage-old-user/', main_views.Manage_Old_USER, name='manage_old_user'),
    path('view-old-user/<int:id>/', main_views.VIEW_Old_USER, name='view_old_user'),
    path('search/', main_views.Search, name='search'),
    path('between-date-report/', main_views.Between_Date_Report, name='between_date_report'),
    path('total-users/', main_views.TotalUser, name='total_users'),
]
