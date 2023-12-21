from main import views 
from django.contrib import admin
from django.urls import path

from django.urls import path,include
from django.contrib import admin
from django.urls import path,include

from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='xsure'),
    path('raj',views.index1,name='xsure1'),
    path('index',views.indexfinal,name='final'),
    path('indexking',views.indexking,name='king'),
    path('test',views.test1,name='test'),
    path('test2',views.test2,name='test2'),
    path('test3',views.test3,name='test3'),
    path('otp',views.otp_ver,name='otp'),
    path('about',views.about,name='about'),
    path('veri',views.veri,name='veri'),
    path('preview/<str:title>/', views.preview, name='preview'),
    path('download/<str:title>/', views.download, name='download'),
    # path('clientsignup/',views.clientsignup,name='clientsignup'), 
    
    path('prof_login',views.prof_login,name='prof_login'),
    path('prof_otp',views.prof_otp,name='prof_otp'),
    path('prof_dash/<str:username>/',views.prof_dash,name='prof_dash')
     
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
