from ecommerce.models import Customer, Category, Product

import django_filters

class CustomerFilter(django_filters.FilterSet):
    username = django_filters.CharFilter(field_name='user__username', lookup_expr='icontains')
    email = django_filters.CharFilter(field_name = 'user__email', lookup_expr='icontains')
    class Meta:
        model = Customer
        fields = ("user__username", "user__email")


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name = "name", lookup_expr = 'icontains')
    slug = django_filters.CharFilter(field_name = "slug", lookup_expr = "icontains")

    class Meta:
        model = Category
        fields = ("name", "slug")

    
class ProductFilter(django_filters.FilterSet):
    slug = django_filters.CharFilter(field_name = "slug", lookup_expr = "icontains")

    class Meta:
        model = Product
        fields = ("slug",)