from pathlib import Path
from django.urls import path
from .views import *
from testapp import views
urlpatterns = [

path('api/v1/register/',RegistrationAPI.as_view(),name='register'),
path('api/v1/login/',UserLoginAPI.as_view(),name='login'),
path('api/v1/changePassword/',UserChangePasswordAPI.as_view(),name='changePassword'),
path('api/v1/logout/',views.Logout,name='logout'),


# path('api/v1/posts/',views.Posts.as_view(),name='posts'),
# path('api/v1/posts/<int:pk>',views.Posts.as_view(),name='posts'),



path('api/v1/post_by_id/<int:pk>', views.PostByIdAPI.as_view(), name='post_by_id'),
path('api/v1/profile_view/<int:pk>', views.ProfileView.as_view(), name='profile_view'),




path('api/v1/create_posts/',views.Posts.as_view(),name='create_posts'),
path('api/v1/delete_posts/<int:pk>',views.Posts.as_view(),name='delete_posts'),
path('api/v1/show_posts/',views.Posts.as_view(),name='show_posts'),
path('api/v1/update_posts/<int:pk>', views.Posts.as_view(), name='update_posts'),


# # path('logout/',views.LogoutAPI.as_view(),name='logout'),
# path('api/v1/userlogout/',views.userlogout,name='userlogout'),
]
# path('api/v1/home/',views.home,name='home'),
# path('api/v1/signup/',views.signup,name='signup'),
# path('api/v1/login1/',views.login,name='login1'),