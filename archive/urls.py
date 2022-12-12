from django.urls import path,include
import archive.views
from django.conf.urls import url

urlpatterns = [
    path('',archive.views.get_root),
    path('hello_world',archive.views.hello_world),
    path('content',archive.views.article_content),
    path('classification',archive.views.get_index_page),
    path('upload',archive.views.get_upload_file),
    url(r'^search/$',archive.views.search,name='search'),
    url(r'^uploadFile/$',archive.views.upload_file),
    url(r'^FileUploads/$',archive.views.get_upload_file)
]