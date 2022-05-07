from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib import admin

urlpatterns = [
    url(r'^admin', admin.site.urls),
    url('^$',views.image,name = 'image'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^detail/(\d+)', views.details , name='detail'),
    url(r'^location/(\d+)', views.location, name='location'),


]
## new static route that references the location to the upload files
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)