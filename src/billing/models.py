# coding=utf-8

"""
    Ecommerce - A Python Dating Website
    Copyright (C) 2018-2019 nbeny
    <nbeny@student.42.fr>
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from django.conf import settings
from django.db import models
from django.db.models.signals import post_save


User = settings.AUTH_USER_MODEL


# abc@teamcfe.com -->> 10000 billing profiles
# abc@teamcfe.com -- 1 billing profile
class BillingProfile(models.Model):
    user        = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    email       = models.EmailField()
    active      = models.BooleanField(default=True)
    update      = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)
    # customer_id in Stripe or Braintree

    def __str__(self):
        return self.email


# def billing_profile_created_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         print('ACTUAL API REQUEST Send to stripe/braintree')
#         instance.customer_id = newID
#         instance.save()

def user_created_receiver(sender, instance, created, *args, **kwargs):
    if created:
        BillingProfile.objects.get_or_create(user=instance, email=instance.email)


post_save.connect(user_created_receiver, sender=User)
