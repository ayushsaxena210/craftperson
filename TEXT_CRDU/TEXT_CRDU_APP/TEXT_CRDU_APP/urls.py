"""TEXT_CRDU_APP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from CRDU_Funtions.views import Homepage, add_word, update_word, dlt_word
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [

    path('', Homepage, name="Homepage"),
    path('admin', admin.site.urls),
    path('add_word/', add_word, name="add_word"),
    path('add_word/<str:word>/', add_word, name="add_word"),
    path('del/<str:word_id>/', dlt_word, name="dlt_word"),
    path('update/<str:pre_word_id>/<str:new_word>/', update_word, name="update_word"),

]
              #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#urlpatterns += staticfiles_urlpatterns()
