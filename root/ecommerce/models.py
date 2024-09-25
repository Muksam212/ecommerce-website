from django.db import models

from root.utils import BaseModel
from users.models import User
# Create your models here.

class Customer(BaseModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "customer", null = True)

    def __str__(self):
        return f"{self.user.username}"


class Category(BaseModel):
    name = models.CharField(max_length=100, unique = True)
    slug = models.SlugField(unique = True)

    def __str__(self):
        return f"{self.name}"
    

class Product(BaseModel):
    name = models.CharField(max_length=100, unique = True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default = 0)
    category = models.ForeignKey(Category, on_delete = models.CASCADE, related_name = "product_category")
    image = models.ImageField(upload_to = "product/images", null = False, blank = False)
    updated_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f"{self.name}"
    

class Address(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user_address")
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    is_default_shipping = models.BooleanField(default=False)
    is_default_billing = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.state}, {self.country}"
    

class Order(BaseModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user_orders")
    order_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    STATUS = (
        ("Pending","Pending"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
        ("None", "None")
    )
    status = models.CharField(max_length=20, choices = STATUS, default = "None")
    shipping_address = models.ForeignKey(Address, related_name='shipping_orders', on_delete=models.SET_NULL, null=True)
    billing_address = models.ForeignKey(Address, related_name='billing_orders', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username}"
    

class OrderItem(BaseModel):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "order_product_items")
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Order #{self.order.id}"
    


class Cart(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = "user_cart_items")
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = "user_product", null = True, blank = False)
    quantity = models.PositiveIntegerField(default = 1)


    def __str__(self):
        return f"Cart for {self.user.username}"
    


class CartItem(BaseModel):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name = "product_cart_items")
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in Cart"


class Review(BaseModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "users_review")
    product = models.ForeignKey(Product, on_delete = models.CASCADE, related_name = "product_review")
    rating = models.PositiveIntegerField(choices = [(i, str(i)) for i in range(1, 6)])
    comment = models.TextField(null = False, blank = False)

    def __str__(self):
        return f"Review for {self.product.name} by {self.user.username}"
    

class Discount(BaseModel):
    code = models.CharField(max_length=20, unique=True)
    percentage = models.DecimalField(max_digits=5, decimal_places=2)  # e.g., 10.00 for 10%
    active = models.BooleanField(default=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.code}"
    

PAYMENT_METHOD = (
    ("COD", "COD"),
    ("KHALTI", "KHALTI"),
    ("None", "None")
)

class Payment(BaseModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "user_payment", null = True)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD, default = "None", null = True)
    amount = models.DecimalField(max_digits = 10, decimal_places=2, null = True)

    def __str__(self):
        return f"{self.user.username}"
    

class Subscription(BaseModel):
    name = models.CharField(max_length=100, null = True)
    email = models.EmailField(unique=True, null = True, blank = False)
    
    def __str__(self):
        return f"{self.name}"