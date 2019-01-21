# coding=utf-8

"""
    PyMatcha - A Python Dating Website
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

"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, re_path

from .views import (
    ProductListView,
    # product_list_view,
    # ProductDetailView,
    # product_detail_view,
    # ProductFeaturedListView,
    # ProductFeaturedDetailView,
    ProductDetailSlugView
)

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    # re_path(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),

    # path('products-fbv/', product_list_view),
    # re_path(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),

    # path('featured/', ProductFeaturedListView.as_view()),
    # re_path(r'featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),

    re_path(r'(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'),
]
