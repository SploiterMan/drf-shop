from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import generics
from managers.serializers import *
from users.models import User
from .serializers import *


class UserDetailAPI(generics.ListAPIView):
    """
        Show User Detail for User with ID
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsUserOrIsAdmin]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id).first()

    lookup_field = 'id'


class UserDetailEmailAPI(generics.ListAPIView):
    """
        Show User Detail for User with ID
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsUserOrIsAdmin]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id).first()

    lookup_field = 'email'


class UserUpdateAPI(generics.RetrieveUpdateAPIView):
    """
        Update User for User with ID
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsUserOrIsAdmin, ]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id).first()

    lookup_field = 'id'


class UserUpdateEmailAPI(generics.RetrieveUpdateAPIView):
    """
        Update User for User with email
    """
    serializer_class = UserSerializer
    permission_classes = [permissions.IsUserOrIsAdmin, ]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id).first()

    lookup_field = 'email'


class UserCreateAPI(generics.CreateAPIView):
    """
        Create User and Order for User
    """
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        user = UserSerializer(data=self.request.data)
        if user.is_valid():
            user.save()
            user.instance.is_active = True
            user.instance.is_active = True
            user.save()
            Order.objects.create(customer_id=user.instance.id, paid=False, created=user.instance.last_login, updated=user.instance.last_login)
            return Response({'message': 'ساخته شد'})

        else:
            return Response(user.errors)


class OrderViewAPI(generics.RetrieveAPIView):
    """
        View Order with ID
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsUserOrIsAdmin]

    def get_queryset(self):
        return Order.objects.filter(customer_id=self.request.user.id).all()

    lookup_field = 'id'


class OrderCreateUserAPI(generics.CreateAPIView):
    """
        Create Order
    """
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def create(self, request, *args, **kwargs):
        data = OrderSerializer(data=self.request.data)
        if data.is_valid():
            data.save()
            data.instance.customer = self.request.user
            data.save()
            return Response({'message': 'با موفقیت ساخته شد'})
        else:
            return Response(data.errors)


class OrderItemCreateAPI(generics.CreateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def create(self, request, *args, **kwargs):
        data = OrderItemSerializer(data=self.request.data)
        if data.is_valid():
            data.save()
            data.instance.order = Order.objects.filter(customer_id=self.request.user.id)
            data.instance.price = data.instance.product.price
        else:
            return Response(data.errors)


class OrderItemListAPI(generics.ListAPIView):
    """
        List of User Order Item with User ID
    """
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return OrderItem.objects.filter(order__customer_id=self.request.user.id)


class OrderItemViewAPI(generics.RetrieveAPIView):
    """
        View Order Item with ID
    """
    serializer_class = OrderItemSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return OrderItem.objects.filter(order__customer_id=self.request.user.id)

    lookup_field = 'id'


class ProductCategoryListAPI(generics.ListAPIView):
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return ProductCategory.objects.all()


class ProductCategoryViewAPI(generics.RetrieveAPIView):
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return ProductCategory.objects.all()

    lookup_field = 'id'


class ProductCategoryViewSlugAPI(generics.RetrieveAPIView):
    serializer_class = ProductCategorySerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return ProductCategory.objects.all()

    lookup_field = 'slug'


class ProductViewAPI(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return Products.objects.filter(status='available')

    lookup_field = 'id'


class ProductViewSlugAPI(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return Products.objects.filter(status='available')

    lookup_field = 'slug'


class ProductListAPI(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return Products.objects.filter(status='available')


class ProductSpecialListAPI(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return Products.objects.filter(status='available', group='special')


class ProductNormalListAPI(generics.ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return Products.objects.filter(status='available', group='normal')


class ArticleViewAPI(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return Article.objects.filter(status='published')

    lookup_field = 'id'


class ArticleViewSlugAPI(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return Article.objects.filter(status='published')

    lookup_field = 'slug'


class ArticleListAPI(generics.ListAPIView):
    serializer_class = ArticleSerializer
    permission_classes = [permissions.IsAuthenticated, ]

    def get_queryset(self):
        return Article.objects.filter(status='published')
