# Generated by Django 2.1.5 on 2019-01-21 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='total',
            new_name='subtotal',
        ),
    ]