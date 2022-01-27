from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Category, Product, Seller


"""
Displays categories to the client
"""


class CategorySerializer(ModelSerializer):
    random_photo = SerializerMethodField()

    def get_random_photo(self, obj):
        try:
            return obj.products.first().photo
        except:
            return ""

    class Meta:
        model = Category
        fields = (
            'id',
            'name',
            'random_photo'
        )


"""
Displays sellers to the client
"""


class SellerSerializer(ModelSerializer):
    class Meta:
        model = Seller
        fields = '__all__'



"""
Displays products to the client
"""


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'photo',
            'price',
            'title',
            'category',
            'seller',
            'photo',
        )
