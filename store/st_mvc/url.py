from django.urls import path, re_path
from .views import index
from .view_folder import store

app_name = "st_mvc"

urlpatterns = [
    path('', index, name='index'),
    path('store/create', store.CreateStoreView.as_view(), name='store_create'),
    path('store', store.StoreListView.as_view(), name='store_list'),
    re_path('store/update/(?P<pk>[0-9a-f]{32})', store.UpdateStoreView.as_view(), name='store_update'),
    path('store/delete/<pk>', store.StoreDeleteView.as_view(), name='store_delete'),
    path('store/delete_modal/<pk>', store.delete_element, name='store_delete_modal'),

]
