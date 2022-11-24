from rest_framework import serializers

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = Product
        fields = [
            "title",
            "content",
            "price",
            "sale_price",
            "my_discount",
        ]
    
    def get_my_discount(self,obj):  #obj refers to instance of the object
        return obj.get_discount()