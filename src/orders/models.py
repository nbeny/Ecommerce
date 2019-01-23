from django.db import models
from django.db.models.signals import pre_save


from carts.models import Cart
from Ecommerce.utils import unique_order_id_generator


ORDER_STATUS_CHOICES = (
    ('creates', 'Created'),
    ('paid', 'Paid'),
    ('shipped', 'Shipped'),
    ('refunded', 'Refunded'),
)


# Random, Unique
class Order(models.Model):
    length = 120
    # pk / id 345678765678
    # billing_profile = ?
    # shipping_address
    # billing_address
    order_id        = models.CharField(max_length=length, blank=True) # AB23DE4
    cart            = models.name = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status          = models.name = models.CharField(max_length=length, default='created', choices=ORDER_STATUS_CHOICES)
    shipping_total  = models.DecimalField(default=5.99, max_digits=100, decimal_places=2)
    total           = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)

    def __str__(self):
        return self.order_id


def pre_save_create_order_id(sender, instance, *args, **kwargs):
    if not instance.order_id:
        instance.oder_id = unique_order_id_generator(instance)


pre_save.connect(pre_save_create_order_id, sender=Order)


# generate the order id?
# generate the order total?