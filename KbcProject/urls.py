from django.contrib          import admin
from django.urls             import path,include
from django.conf.urls.static import static
from django.conf             import settings


urlpatterns = [
    path('admin/', admin.site.urls),

    # local apps calling
    path('',          include('question_app.urls')        ),
    path('accounts/', include('django.contrib.auth.urls') ),
    path('users/',    include('users.urls') ),

   # for accessing media file urls.
]+ static( settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )

handler404 = 'users.views.error_404_view' #new 
handler500 = 'users.views.error_500_view' #new 

