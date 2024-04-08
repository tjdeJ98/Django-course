from django.db import models

# Promotion m:m Products


class Promotion(models.Model):
    description = models.CharField(max_length=254)
    discount = models.FloatField()


class Collection(models.Model):
    title = models.CharField(max_length=254)
    featured_product = models.ForeignKey(
        'Product', on_delete=models.SET_NULL, null=True, related_name='+')

# Create your models here.


class Product(models.Model):
    # if we want to create the PK ourself do this:
    # sku = models.CharField(max_length=10, primary_key=True)

    # CharField is a "Field Type"
    # Field types have "Field options"
    title = models.CharField(max_length=254)
    slug = models.SlugField(default='0')
    description = models.TextField()
    # 9999.99 <- max price. 4 digits + 2 digits
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField()
    last_update = models.DateField(auto_now=True)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT)
    promotions = models.ManyToManyField(Promotion)


class Customer(models.Model):
    MEMBERSHIP_BRONZE = 'B'
    MEMBERSHIP_SILVER = 'S'
    MEMBERSHIP_GOLD = 'G'

    # Array [] of Tuples ('', '')
    MEMBERSHIP_CHOICES = [
        (MEMBERSHIP_BRONZE, 'Bronze'),
        (MEMBERSHIP_SILVER, 'Silver'),
        (MEMBERSHIP_GOLD, 'Gold')
    ]

    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(unique=True)
    # phone = models.DecimalField(max_digitis=10, decimal_places=0)
    phone = models.CharField(max_length=254)
    birth_date = models.DateField()

    # Imagine we want 3 values: E, S, G (Bronze, Silver, Gold) we add the choices with a array
    membership = models.CharField(
        max_length=1, choices=MEMBERSHIP_CHOICES, default=MEMBERSHIP_BRONZE)
    # order_set because foreignkey in Order


class Order(models.Model):
    PAYMENT_PENDING = 'P',
    PAYMENT_COMPLETE = 'C',
    PAYMENT_FAILED = 'F',

    PAYMENT_CHOISES = [
        ('', 'Pending'),
        ('', 'Complete'),
        ('', 'Failed'),
    ]

    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(
        max_length=1, choices=PAYMENT_CHOISES, default=PAYMENT_PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)


class Address(models.Model):
    street = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    zip = models.CharField(max_length=254, blank=True)

    # The costumer has a Address so the costumer is the parent
    costomer = models.ForeignKey(
        Customer, on_delete=models.CASCADE)


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
