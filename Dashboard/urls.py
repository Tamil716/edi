from django.urls import path
from . import views

urlpatterns = [
    path('Dashboard/', views.index),
    path('blog/', views.blog_list),
    path('blog/<int:id>/', views.blog_detail),
    path('blog/<int:id>/edit', views.blog_update),
    path('blog/<int:id>/delete', views.blog_delete),
    path('blog-create/', views.blog_create),
    path('',views.about),
    path('EDI/',views.edi),
    path('Multiple-EDI/',views.multiple_edi),
    path('Multiple-EDI-EOB/',views.multiple_edi_eob),
    path('Multiple-Line-Item/',views.multiple_line_item),
    path('Multiple-Line-Item-EOB/',views.multiple_line_item_eob),
    path('Contact/',views.contact)
]