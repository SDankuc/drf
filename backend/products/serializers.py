from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title_no_hello , unique_product_title

class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only = True)
    edit_url = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail",
        lookup_field = "pk"
        )
    title = serializers.CharField(validators = [validate_title_no_hello, unique_product_title])

    #name = serializers.CharField(source = "title", read_only = True) # source to grab the title and display it as name
    # email = serializers.CharField(source = "user.email", read_only = True)
    #email = serializers.EmailField(write_only=True)
    class Meta:
        model = Product
        fields = [
            #"user",
            "url",
            "edit_url",
            #"email",
            "pk",
            "title",
            #"name",
            "content",
            "price",
            "sale_price",
            "my_discount",
        ]
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