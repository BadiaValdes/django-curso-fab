from django.urls import path, re_path
from .views import index
from .view_folder import store, forms_obj3, video_game

app_name = "st_mvc"

urlpatterns = [
    path('', index, name='index'),
    path('store/create', store.CreateStoreView.as_view(), name='store_create'),
    path('store', store.StoreListView.as_view(), name='store_list'),
    re_path('store/update/(?P<pk>[0-9a-f]{32})', store.UpdateStoreView.as_view(), name='store_update'),
    path('store/delete/<pk>', store.StoreDeleteView.as_view(), name='store_delete'),
    path('store/delete_modal/<pk>', store.delete_element, name='store_delete_modal'),

    # URL - FORMS
    path('forms', forms_obj3.form_index, name='forms'),
    path('forms/basico', forms_obj3.form_basico, name='form_basico'),
    path('forms/class', forms_obj3.form_by_parameter, name='form_by_class'),
    path('forms/model', forms_obj3.form_class_model, name='form_by_model'),

    # URL - GENERIC VIEW
    path('generic', video_game.index_video_game, name='generic'),
    path('generic/list', video_game.VideoGameList.as_view(), name='generic_list'),
    path('generic/create', video_game.VideoGameCreate.as_view(), name='generic_create'),
    re_path('generic/update/(?P<pk>[0-9a-f]{32})', video_game.VideoGameUpdate.as_view(), name='generic_update'),
    re_path('generic/delete/(?P<pk>[0-9a-f]{32})', video_game.VideoGameDelete.as_view(), name='generic_delete'),
    re_path('generic/detail/(?P<pk>[0-9a-f]{32})', video_game.VideoGameDetail.as_view(), name='generic_detail'),

]
