# coding=utf-8

"""
    eCommerce - A Python Dating Website
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

'''
# Shell session 1
# python manage.py shell
'''


from tags.models import Tag

qs = Tag.objects.all()
print(qs)
black = Tag.objects.last()
black.title
black.slug

black.products
'''
returns:
<django.db.models.fields.related_descriptiors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager>
'''

black.products.all()
'''
This is an actual queryset of PRODUCTS
Mush like Producs.objects.all(), but in this case it's ALL of the products that are
related to the "Black" tag
'''

black.products.all().first()

'''
returns the first instance, if any
'''

exit()

'''
# Shell session 2
python manage.py shell
'''

from products.models import Product

qs = Product.object.all()
print(qs)
tshirt = qs.first()
tshirt.title
tshirt.description

tshirt.tag

'''
Raises an error because the Product model doesn't have a field "tag"
'''

tshirt.tags

'''
Raises an error because the Product model doesn't have a field "tags"
'''

tshirt.tag_set
'''
This works because the Tag model has the "products" field with the ManyToMany to Product
<django.db.models.fields.related_descriptiors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager>
'''

tshirt.tag_set.all().filter()
'''
Returns an actual Queryset of the Tag model related to this product
<QuerySet [<Tag: T shirt>, <Tag: TSirt>, <Tag: T-shirt>, <TAg: Red>, <Tag: Black>]>
'''
tshirt.tag_set.filter(title__icontains='black')
