from rest_framework import serializers
from dashboard.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "_all_"
