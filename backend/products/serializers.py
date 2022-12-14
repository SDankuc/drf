from rest_framework import serializers
from rest_framework.reverse import reverse
from api.serializers import UserPublicSerializer
from .models import Product
from .validators import validate_title_no_hello , unique_product_title

class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name="product-detail", lookup_field = "pk",read_only = True)
    title = serializers.CharField(read_only = True)

class ProductSerializer(serializers.ModelSerializer):
    #user = UserPublicSerializer(read_only = True)
    owner = UserPublicSerializer(source = "user",read_only = True)
    #related_products = ProductInlineSerializer(source = "user.product_set.all", read_only = True, many=True)
    #my_user_data = serializers.SerializerMethodField(read_only=True)
    #my_discount = serializers.SerializerMethodField(read_only = True)
    title = serializers.CharField(validators = [validate_title_no_hello, unique_product_title])

    #name = serializers.CharField(source = "title", read_only = True) # source to grab the title and display it as name
    email = serializers.EmailField(source = "user.email", read_only = True)
    #email = serializers.EmailField(write_only=True)
    body = serializers.CharField(source="content")
    class Meta:
        model = Product
        fields = [
            "owner", # user_id by default
            "email",
            "pk",
            "title",
            #"name",
            "body",
            "price",
            "sale_price",
            #"my_discount",
            #"my_user_data",
            #"related_products",
            "public",
            'path',
            'endpoint',
        ]
    def get_my_user_data(self,obj):
        return{
            "username":obj.user.username
        }


    #def validate <fieldName>
    # def validate_title(self,value):
    #     request = self.context.get("request")
    #     user = request.user
    #     qs = Product.objects.filter(user=user,title__iexact = value) #iexact -< i for case insensitive
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value

    # def create(self, validated_data):
    #     #return Product.objects.create(**validated_data)
    #     #email = validated_data.pop("email")
    #     obj = super().create(validated_data)
    #     #print(email, obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     email = validated_data.pop("email")
    #     instance.title = validated_data.get("title")
    #     return super().update(instance, validated_data)

    def get_edit_url(self,obj):
        request = self.context.get("request")
        if request is None:
            return None
        return reverse("product-edit",kwargs = {"pk":obj.pk}, request=request)

    def get_my_discount(self,obj):  #obj refers to instance of the object
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return "122"