from shop.settings import EMAIL_HOST_PAASWORD, EMAIL_HOST_USER, EMAIL_HOST, EMAIL_PORT_SSL
from rest_framework.response import Response
from email.message import EmailMessage
from rest_framework import generics
from users.models import User
from .serializers import *
from .models import *
from rest_framework import permissions
import smtplib


class UserCreateAPI(generics.CreateAPIView):
    """
        Create user
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = UserSerializer(data=self.request.data)
        if user.is_valid():
            user.save()
            order = {'paid': False}
            data = OrderSerializer(data=order)
            if data.is_valid():
                data.save()
                data.instance.created = user.instance.last_login
                data.instance.updated = user.instance.last_login
                data.instance.customer_id = user.instance.id
                data.instance.paid = False
                data.save()
                return Response({'message': 'کاربر با موفقیت ساخته شد'})

            else:
                return Response(data.errors)

        else:
            return Response(user.errors)


class UserAdminAPI(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = User.objects.filter(is_admin=True)


class UserListAPI(generics.ListAPIView):
    """
        Show list of User
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = User.objects.all()


class UserViewAPI(generics.RetrieveAPIView):
    """
        View User with User ID
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = User.objects.all()
    lookup_field = 'id'


class UserUpdateAPI(generics.RetrieveUpdateAPIView):
    """
        Update User with User ID
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = User.objects.all()
    lookup_field = 'id'


class UserDestroyAPI(generics.DestroyAPIView):
    """
        Destroy User with User ID
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = User.objects.all()
    lookup_field = 'id'


class UserViewEmailAPI(generics.RetrieveAPIView):
    """
        View User with User ID
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = User.objects.all()
    lookup_field = 'email'


class UserUpdateEmailAPI(generics.RetrieveUpdateAPIView):
    """
        Update User with User ID
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = User.objects.all()
    lookup_field = 'email'


class UserDestroyEmailAPI(generics.DestroyAPIView):
    """
        Destroy User with User ID
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = User.objects.all()
    lookup_field = 'email'


class ProductCategoryCreateAPI(generics.CreateAPIView):
    """
        Create Product Category
    """
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]


class ProductCategoryListAPI(generics.ListAPIView):
    """
        Show list of Product Categories
    """
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = ProductCategory.objects.all()


class ProductCategoryViewAPI(generics.RetrieveAPIView):
    """
        View Product Category with Product Category ID
    """
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = ProductCategory.objects.all()
    lookup_field = 'id'


class ProductCategoryUpdateAPI(generics.RetrieveUpdateAPIView):
    """
        Update Product Category with Product Category ID
    """
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = ProductCategory.objects.all()
    lookup_field = 'id'


class ProductCategoryDestroyAPI(generics.DestroyAPIView):
    """
        Destroy Product Category with Product Category ID
    """
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = ProductCategory.objects.all()
    lookup_field = 'id'


class ProductCategorySlugViewAPI(generics.RetrieveAPIView):
    """
        View Product Category with Product Category Slug
    """
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = ProductCategory.objects.all()
    lookup_field = 'slug'


class ProductCategoryUpdateSlugAPI(generics.RetrieveUpdateAPIView):
    """
        Update Product Category with Product Category Slug
    """
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = ProductCategory.objects.all()

    lookup_field = 'slug'


class ProductCategoryDestroySlugAPI(generics.DestroyAPIView):
    """
        Destroy Product Category with Product Category Slug
    """
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = ProductCategory.objects.all()
    lookup_field = 'slug'


class ArticleCategoryCreateAPI(generics.CreateAPIView):
    """
        Create Article Category
    """
    serializer_class = ArticleCategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]


class ArticleCategoryListAPI(generics.ListAPIView):
    """
        Show list of Product Categories
    """
    serializer_class = ArticleCategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = ArticleCategory.objects.all()


class ArticleCategoryViewAPI(generics.RetrieveAPIView):
    """
        View Article Category with Article Category ID
    """
    serializer_class = ArticleCategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = ArticleCategory.objects.all()
    lookup_field = 'id'


class ArticleCategoryUpdateAPI(generics.RetrieveUpdateAPIView):
    """
        Update Article Category with Article Category ID
    """
    serializer_class = ArticleCategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = ArticleCategory.objects.all()
    lookup_field = 'id'


class ArticleCategoryDestroyAPI(generics.DestroyAPIView):
    """
        Destroy Article Category with Article Category ID
    """
    serializer_class = ArticleCategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = ArticleCategory.objects.all()
    lookup_field = 'id'


class ArticleCategoryViewSlugAPI(generics.RetrieveAPIView):
    """
        View Article Category with Article Category Slug
    """
    serializer_class = ArticleCategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = ArticleCategory.objects.all()
    lookup_field = 'slug'


class ArticleCategoryUpdateSlugAPI(generics.RetrieveUpdateAPIView):
    """
        Update Article Category with Article Category Slug
    """
    serializer_class = ArticleCategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = ArticleCategory.objects.all()
    lookup_field = 'slug'


class ArticleCategoryDestroySlugAPI(generics.DestroyAPIView):
    """
        Destroy Article Category with Article Category Slug
    """
    serializer_class = ArticleCategorySerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = ArticleCategory.objects.all()

    lookup_field = 'slug'


class ProductCreateAPI(generics.CreateAPIView):
    """
        Create Product
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Products.objects.all()


class ProductsListAPI(generics.ListAPIView):
    """
        Show list of Products
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Products.objects.all()


class ProductStatusAPI(generics.ListAPIView):
    """
        List of Products ( status = True )
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Products.objects.filter(status='available')


class ProductGroupSpecialAPI(generics.ListAPIView):
    """
        List of Products ( group = Special , status = True )
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Products.objects.filter(group='special', status='available')


class ProductGroupSpecialFalseAPI(generics.ListAPIView):
    """
        List of Products ( group = Special , status = False )
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Products.objects.filter(group='special', status='available')


class ProductGroupNormalAPI(generics.ListAPIView):
    """
        List of Products ( group = Normal , status = True )
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Products.objects.filter(group='normal', status='available')


class ProductGroupNormalFalseAPI(generics.ListAPIView):
    """
        List of Products ( group = Normal , status = False )
    """

    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Products.objects.filter(group='normal', status='unavailable')


class ProductViewAPI(generics.RetrieveAPIView):
    """
        View Product API with Product ID
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Products.objects.all()
    lookup_field = 'id'


class ProductUpdateAPI(generics.RetrieveUpdateAPIView):
    """
        Update Product with Product ID
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Products.objects.all()
    lookup_field = 'id'


class ProductDestroyAPI(generics.DestroyAPIView):
    """
        Destroy Product with Product ID
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Products.objects.all()
    lookup_field = 'id'


class ProductViewSlugAPI(generics.RetrieveAPIView):
    """
        View Product with Product Slug
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Products.objects.all()
    lookup_field = 'slug'


class ProductUpdateSlugAPI(generics.RetrieveUpdateAPIView):
    """
        Update Product with Product Slug
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Products.objects.all()
    lookup_field = 'slug'


class ProductDestroySlugAPI(generics.DestroyAPIView):
    """
        Destroy Product with Product Slug
    """
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Products.objects.all()
    lookup_field = 'slug'


class ArticleCreateAPI(generics.CreateAPIView):
    """
        Create Article
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]


class ArticleListAPI(generics.ListAPIView):
    """
        Show list of Articles
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Article.objects.all()


class ArticleStatusAPI(generics.ListAPIView):
    """
        List of Articles ( status = True )
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Article.objects.filter(status='published')


class ArticleViewAPI(generics.RetrieveAPIView):
    """
        View Article with Article ID
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Article.objects.all()
    lookup_field = 'id'


class ArticleUpdateAPI(generics.RetrieveUpdateAPIView):
    """
        Update Article with Article ID
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Article.objects.all()
    lookup_field = 'id'


class ArticleDestroyAPI(generics.DestroyAPIView):
    """
        Destroy Article with Article ID
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Article.objects.all()
    lookup_field = 'id'


class ArticleViewSlugAPI(generics.RetrieveAPIView):
    """
        View Article with Article Slug
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Article.objects.all()
    lookup_field = 'slug'


class ArticleUpdateSlugAPI(generics.RetrieveUpdateAPIView):
    """
        Update Article with Article Slug
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def get_queryset(self):
        return Article.objects.all()

    lookup_field = 'slug'


class ArticleDestroySlugAPI(generics.DestroyAPIView):
    """
        Destroy Article with Article Slug
    """
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Article.objects.all()
    lookup_field = 'slug'


class OrderCreateAPI(generics.CreateAPIView):
    """
        Create Order
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]


class OrderUserAPI(generics.ListAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        slam = self.request.query_params.get('id')
        print(slam)
        return Order.objects.filter(customer_id=self.request.user.id).all()


class OrderPaidAPI(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(paid=True)


class OrderAdd(generics.CreateAPIView):
    serializer_class = OrderItemSerializer

    def create(self, request, *args, **kwargs):
        OrderItem.objects.create(
            order=Order.objects.filter(customer_id=self.request.user.id).first(),
            product=self.request.query_params.get()
            )


class OrderUserAdd(generics.CreateAPIView):
    """
        Add Order Item to User Order by User
    """
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def perform_create(self, serializer):
        customer = self.request.user.id
        order = Order.objects.filter(customer_id=customer).first()
        product = Products.objects.filter(id=self.request.query_params.get('product_id')).first()
        quantity = self.request.query_params('quantity')
        OrderItem.objects.create(order=order, product_id=product, quantity=quantity)


class OrderListAPI(generics.ListAPIView):
    """
        Show list of Orders
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Order.objects.all()


class OrderViewAPI(generics.RetrieveAPIView):
    """
        View Order with Order ID
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Order.objects.all()

    lookup_field = 'id'


class OrderUpdateAPI(generics.RetrieveUpdateAPIView):
    """
        Update Order with Order ID
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Order.objects.all()

    lookup_field = 'id'


class OrderDestroyAPI(generics.DestroyAPIView):
    """
        Destroy Order with Order ID
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = Order.objects.all()

    lookup_field = 'id'


class OrderItemCreateAPI(generics.CreateAPIView):
    """
        Create Order Item
    """
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]


class OrderItemListAPI(generics.ListAPIView):
    """
        Show list of Order Item
    """
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = OrderItem.objects.all()


class OrderItemFilterAPI(generics.ListAPIView):
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        return OrderItem.objects.filter(order__customer_id=self.request.query_params.get('id')).all()


class OrderItemViewAPI(generics.RetrieveAPIView):
    """
        View Order Item with Order Item ID
    """
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = OrderItem.objects.all()

    lookup_field = 'id'


class OrderItemUpdateAPI(generics.RetrieveUpdateAPIView):
    """
        Update Order Item with Order Item ID
    """
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = OrderItem.objects.all()

    lookup_field = 'id'


class OrderItemDestroyAPI(generics.DestroyAPIView):
    """
        Destroy Order Item with Order Item ID
    """
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    queryset = OrderItem.objects.all()

    lookup_field = 'id'


class EmailCreateAPI(generics.CreateAPIView):
    """
        Create Email Message for send
    """
    serializer_class = EmailSerializer
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data['customer']).first()
        msg = EmailMessage()
        msg['Subject'] = f"{self.request.data['subject']}"
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = f'{user.email}'
        msg.set_content(f'{self.request.data["message"]}')
        with smtplib.SMTP_SSL(EMAIL_HOST, EMAIL_PORT_SSL) as server:
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PAASWORD)
            server.send_message(msg)
            return Response({'messages': 'ایمیل ارسال شد'})