
from django.conf.urls import url
from users import views
# SET THE NAMESPACE!
app_name = 'users'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^about/$',views.about,name='about'),
    url(r'^profile/$',views.profile,name='profile'),

    
    #path('register/', include(('users.urls','users'),namespace="users")),
    #path('user_login/', include(('users.urls','users'),namespace="users")),
]