from django.contrib          import admin
from django.urls             import path,include
from django.conf.urls.static import static
from django.conf             import settings

urlpatterns = [
    path('admin/', admin.site.urls),

    # local apps calling
    path('',                    include('question_app.urls')        ),
    path('accounts/',           include('django.contrib.auth.urls') ),
    path('analysis/',            include('users.urls') ),

   # for accessing media file urls.
]+ static( settings.MEDIA_URL , document_root=settings.MEDIA_ROOT )

