from django.urls import path
from app.views.admin import AdminView
from app.views.users import UserView
from app.views.user_second_view import SecondUserView


# Admin 
urlpatterns = [
    # API: Add an advisor
    path('admin/advisor/', AdminView.as_view(), name='admin-advisor'), 
]

# Users
urlpatterns += [
    # API: Can register as a user
    path('user/register/', UserView.as_view(), name='user-register'),
    path('user/login/', SecondUserView.as_view({'post': 'user_login'}), name='login'),
    path('user/<int:user_id>/advisor/', SecondUserView.as_view({'get': 'get_list_advisor'}), name="get_list_advisor"),
    path("user/<int:user_id>/advisor/<int:advisor_id>/", SecondUserView.as_view({'post': 'calls_booking'}), name="calls_booking"),
    path("user/<int:user_id>/advisor/booking/", SecondUserView.as_view({'get': 'booked_calls'}), name="")
]