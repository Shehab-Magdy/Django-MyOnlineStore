from django.urls import path
from .views import category, product, home, adminindex
from django.conf.urls import url
from django.conf.urls.static import static

app_name = 'center'
 
urlpatterns = [
path('',home.Index, name='center.home'),
url(r'home/(?P<cat_id>\d+)/$',home.Index, name='center_home_cat'),
path('adminindex/',adminindex.admin_index, name='admin_index'),
path('category',category.index, name ='Category_List'),
url(r'^category/(?P<cat_id>\d+)/$',category.show, name = 'category.show'),
url(r'^category/(?P<cat_id>\d+)/delete/$',category.delete, name = 'category_del'),
path('category/create',category.create, name = 'category_addnew'),
#path('category/save',category.save, name = 'category_save'),
url(r'^category/(?P<cat_id>\d+)/update/$',category.update, name = 'category_update'),
#url(r'^category/(?P<cat_id>\d+)/save/$',category.saveupdate, name = 'category_saveupdate'),
path('product',product.index, name ='Product_List'),
url(r'^product/(?P<prod_id>\d+)/$',product.show, name = 'product_show'),
url(r'^product/(?P<prod_id>\d+)/delete/$',product.delete, name = 'product_del'),
path('product/create',product.create, name = 'product_addnew'),
#path('product/save',product.create, name = 'product_save'),
url(r'^product/(?P<prod_id>\d+)/update/$',product.update, name = 'product_update'),
#url(r'^product/(?P<prod_id>\d+)/save/$',product.update, name = 'product_saveupdate'),
]