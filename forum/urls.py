from django.urls import path, include
from forum2 import views
from django.conf.urls.static import static
from django.conf import settings
from users.views import Register


app_name ='forum'
urlpatterns = [
    #Страничка главная
    path('',views.home, name='home'),
    #Страница с формой для нового вопроса
    path('', include('django.contrib.auth.urls')),
    path('register/', Register.as_view(), name='register'),
    path('not_work/',views.not_work,name='not_work')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)