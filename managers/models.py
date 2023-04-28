from extensions.DateJalali import django_jalali
from datetime import timezone
from django.db import models
from users.models import *


class ProductCategory(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, verbose_name="عنوان")
    slug = models.SlugField(max_length=255, unique=True, blank=False, null=False, verbose_name="اسلاگ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی محصولات'
        verbose_name_plural = 'دسته بندی محصولات'


class ArticleCategory(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False, verbose_name="عنوان")
    slug = models.SlugField(max_length=255, unique=True, blank=False, null=False, verbose_name="اسلاگ")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ذسته بندی مقالات'
        verbose_name_plural = 'دسته بندی های مقالات'


class Products(models.Model):
    STATUS = (
        ('available', 'موجود'),
        ('unavailable', 'ناموجود')
    )
    GROUP = (
        ('special', 'ویژه'),
        ('normal', 'معمولی')
    )
    title = models.CharField(max_length=255, blank=False, null=False, verbose_name="عنوان")
    slug = models.SlugField(max_length=255, unique=True, blank=False, null=False, verbose_name="اسلاگ")
    description = models.TextField(null=False, blank=False, verbose_name="درباره")
    thumbnail = models.ImageField(null=False, blank=False, upload_to='product/%y/%m/%d', verbose_name="تصویر")
    price = models.IntegerField(blank=False, null=False, verbose_name="قیمت")
    status = models.CharField(choices=STATUS, max_length=20, blank=False, null=False, verbose_name="وضعیت")
    number = models.IntegerField(null=False, blank=False, verbose_name="تعداد")
    group = models.CharField(choices=GROUP, max_length=10, verbose_name="نوع محصول")
    category = models.ManyToManyField(ProductCategory, verbose_name="دسته بندی")
    created = models.DateTimeField(auto_now_add=True, verbose_name="زمان ساخت")
    updated = models.DateTimeField(auto_now=True, verbose_name="آخرین تغییرات")

    def jdateCreated(self):
        return django_jalali(self.created)

    def jdateUpdated(self):
        return django_jalali(self.updated)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'


class Article(models.Model):
    STATUS = (
        ('published', 'منتشر شده'),
        ('draft', 'پیش نویس')
    )
    title = models.CharField(max_length=255, blank=False, null=False, verbose_name="عنوان")
    slug = models.SlugField(max_length=255, unique=True, blank=False, null=False, verbose_name="اسلاگ")
    description = models.TextField(null=False, blank=False, verbose_name="درباره")
    thumbnail = models.ImageField(null=False, blank=False, upload_to='article/%y/%m/%d', verbose_name="تصویر")
    category = models.ManyToManyField(ArticleCategory, verbose_name="دسته بندی")
    status = models.CharField(choices=STATUS, max_length=10, blank=False, null=False, verbose_name="وضعیت")
    created = models.DateTimeField(auto_now_add=True, verbose_name="زمان ساخت")
    updated = models.DateTimeField(auto_now=True, verbose_name="آخرین تغییرات")
    auther = models.ForeignKey(User, on_delete=models.CASCADE, default=User, verbose_name="نویسنده")

    def jdateCreated(self):
        return django_jalali(self.created)

    def jdateUpdated(self):
        return django_jalali(self.updated)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


class Email(models.Model):
    customer = models.ForeignKey(User, related_name='Send', on_delete=models.CASCADE, verbose_name='مشتری')
    subject = models.CharField(max_length=255, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیام')

    def __str__(self):
        return self.subject


class Order(models.Model):
    customer = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, verbose_name='مشتری')
    paid = models.BooleanField(default=False, verbose_name='پرداخت شده')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'سفارش'
        verbose_name_plural = 'سفارشات'

    def jdateCreated(self):
        return django_jalali(self.created)

    def jdateUpdated(self):
        return django_jalali(self.updated)

    def get_total(self):
        return sum(item.get_cost()for item in self.item.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='item')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, verbose_name='محصول')
    quantity = models.IntegerField(default=1, verbose_name='تعداد')

    class Meta:
        verbose_name = 'مورد سفارش'
        verbose_name_plural = 'موارد سفارشات'

    def __str__(self):
        return self.id

    def get_cost(self):
        return self.product.price * self.quantity
