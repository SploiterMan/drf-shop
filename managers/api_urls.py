from django.urls import path
from . import api_views

urlpatterns = [
    # Users
    path('user/list/', api_views.UserListAPI.as_view(), name='UserList'),
    path('user/admin/list/', api_views.UserAdminAPI.as_view(), name='UserAdminList'),
    path('user/create/', api_views.UserCreateAPI.as_view(), name='UserCreate'),
    path('user/update/<int:id>/', api_views.UserUpdateAPI.as_view(), name='UserUpdate'),
    path('user/destroy/<int:id>/', api_views.UserDestroyAPI.as_view(), name='UserDestroy'),
    path('user/<int:id>/', api_views.UserViewAPI.as_view(), name='UserView'),
    # Users with Email
    path('user/update/<str:email>/', api_views.UserUpdateEmailAPI.as_view(), name='UserUpdateEmail'),
    path('user/destroy/<str:email>/', api_views.UserDestroyEmailAPI.as_view(), name='UserDestroyEmail'),
    path('user/<str:email>/', api_views.UserViewEmailAPI.as_view(), name='UserViewEmail'),
    # Product categories with ID
    path('category/product/list/', api_views.ProductCategoryListAPI.as_view(), name='ProductCategoryList'),
    path('category/product/create/', api_views.ProductCategoryCreateAPI.as_view(), name='ProductCategoryCreate'),
    path('category/product/update/<int:id>/', api_views.ProductCategoryUpdateAPI.as_view(), name='ProductCategoryUpdate'),
    path('category/product/destroy/<int:id>/', api_views.ProductCategoryDestroyAPI.as_view(), name='ProductCategoryDestroy'),
    path('category/product/<int:id>/', api_views.ProductCategoryViewAPI.as_view(), name='ProductCategoryView'),
    # product categories with Slug
    path('category/product/update/<slug:slug>/', api_views.ProductCategoryUpdateSlugAPI.as_view(), name='ProductCategoryUpdateSlug'),
    path('category/product/destroy/<slug:slug>/', api_views.ProductCategoryDestroySlugAPI.as_view(), name='ProductCategoryDestroySlug'),
    path('category/product/<slug:slug>/', api_views.ProductCategorySlugViewAPI.as_view(), name='ProductCategorySlugView'),
    # products with ID
    path('product/list/', api_views.ProductsListAPI.as_view(), name='ProductsList'),
    path('product/filter/', api_views.ProductFilterAPI.as_view(), name='ProductFilter'),
    path('product/list/true/', api_views.ProductsListAPI.as_view(), name='ProductsList'),
    path('product/create/', api_views.ProductCreateAPI.as_view(), name='ProductCreate'),
    path('product/update/<int:id>/', api_views.ProductUpdateAPI.as_view(), name='ProductUpdate'),
    path('product/destroy/<int:id>/', api_views.ProductDestroyAPI.as_view(), name='ProductDestroy'),
    path('product/<int:id>/', api_views.ProductViewAPI.as_view(), name='ProductView'),
    # product with Slug
    path('product/update/<slug:slug>/', api_views.ProductUpdateSlugAPI.as_view(), name='ProductUpdateSlug'),
    path('product/destroy/<slug:slug>/', api_views.ProductDestroySlugAPI.as_view(), name='ProductDestroySlug'),
    path('product/<slug:slug>/', api_views.ProductViewSlugAPI.as_view(), name='ProductViewSlug'),
    # articles with ID
    path('article/list/', api_views.ArticleListAPI.as_view(), name='ArticleList'),
    path('article/create/', api_views.ArticleCreateAPI.as_view(), name='ArticleCreate'),
    path('article/list/status/', api_views.ArticleStatusAPI.as_view(), name='ArticleStatus'),
    path('article/update/<int:id>/', api_views.ArticleUpdateAPI.as_view(), name='ArticleUpdate'),
    path('article/destroy/<int:id>/', api_views.ArticleDestroyAPI.as_view(), name='ArticleDestroy'),
    path('article/<int:id>/', api_views.ArticleViewAPI.as_view(), name='ArticleView'),
    # article with Slug
    path('article/update/<slug:slug>/', api_views.ArticleUpdateSlugAPI.as_view(), name='ArticleUpdateSlug'),
    path('article/destroy/<slug:slug>/', api_views.ArticleDestroySlugAPI.as_view(), name='ArticleDestroySlug'),
    path('article/<slug:slug>/', api_views.ArticleViewSlugAPI.as_view(), name='ArticleViewSlug'),
    # order
    path('order/list/', api_views.OrderListAPI.as_view(), name='OrderList'),
    path('order/create/', api_views.OrderCreateAPI.as_view(), name='OrderCreate'),
    path('order/update/<int:id>/', api_views.OrderUpdateAPI.as_view(), name='OrderUpdate'),
    path('order/destroy/<int:id>/', api_views.OrderDestroyAPI.as_view(), name='OrderDestroy'),
    path('order/<int:id>/', api_views.OrderViewAPI.as_view(), name='OrderView'),
    # order item
    path('orderitem/list/', api_views.OrderItemListAPI.as_view(), name='OrdersItemList'),
    path('orderitem/filter/<int:id>/', api_views.OrderItemFilterAPI.as_view(), name='OrderItemFilter'),
    path('orderitem/create/', api_views.OrderItemCreateAPI.as_view(), name='OrderItemCreate'),
    path('orderitem/update/<int:id>/', api_views.OrderItemUpdateAPI.as_view(), name='OrderItemUpdate'),
    path('orderitem/destroy/<int:id>/', api_views.OrderItemDestroyAPI.as_view(), name='OrderItemDestroy'),
    path('orderitem/<int:id>/', api_views.OrderItemViewAPI.as_view(), name='OrderItemView'),
    # emails
    path('email/create/', api_views.EmailCreateAPI.as_view(), name='EmailCreate'),
    ]
