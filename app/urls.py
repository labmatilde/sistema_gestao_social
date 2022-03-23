"""app URL Configuration

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

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sgfinaceiro/', include('sgfinaceiro.urls')),
    path('sgproduto/', include('sgproduto.urls')),
    path('sgprojeto/', include('sgprojeto.urls')),
    path('sgfamilia/', include('sgfamilia.urls')),
    path('sgdominios/', include('sgdominios.urls')),
    path('sgarmazenagem/', include('sgarmazenagem.urls')),
    path('sgkit/', include('sgkit.urls')),
    path('sgpessoa/', include('sgpessoa.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# TODO remover depois o debug tool bar
if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
    path('__debug__/', include('debug_toolbar.urls')),
    ] + urlpatterns