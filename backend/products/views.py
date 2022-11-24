from rest_framework import generics


from .models import Product
from.serializers import ProductSerializer

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        #serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get("title")
        content = serializer.validated_data.get("content") or None
        if content is None:
            content = title
        serializer.save(content=content)
        # send a Django signal <- this can be done here

product_list_create_view = ProductListCreateAPIView.as_view()

class ProductDetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field = "pk"

#not using this method -> ProductCreateApiView changing to ProductListCreateApiView
class ProductListApiView(generics.ListAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #lookup_field = "pk"




