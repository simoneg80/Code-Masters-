from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    # about page below

    path('about/', views.about, name='about'),

    # shop page below
    path('guides/', views.guides_index, name='index'),

    #Detail page
    path('guides/<int:guide_id>', views.guides_detail, name='detail'),
    
    path('guides/<int:guide_id>/create_order/', views.create_order, name='create_order'),

    # Step 3: Orders paths below
    path('orders/', views.OrderList.as_view(), name='orders_index'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='orders_detail'),
    path('orders/create/', views.OrderCreate.as_view(), name='orders_create'),
    path('orders/<int:pk>/update/', views.OrderUpdate.as_view(), name='orders_update'),
    path('orders/<int:pk>/delete/', views.OrderDelete.as_view(), name='orders_delete'),

    #comment add path
    path('guides/<int:guide_id>/add_comment', views.add_comment, name='add_comment'),
    path('comments/<int:guide_id>/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    path('comments/<int:guide_id>/<int:pk>/update/', views.update_comment, name='update_comment'),
    path('comments/<int:guide_id>/<int:pk>/edit/', views.edit_comment, name='edit_comment')


    # #signup path
    # path('accounts/signup/', views.signup, name='signup'),

    

]
