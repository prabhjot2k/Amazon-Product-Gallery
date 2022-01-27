from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework import status
from .serializers import CategorySerializer, SellerSerializer, ProductSerializer

from .models import Product, Category, Seller


"""
Calls Product model, serializes the data and returns it to the client
"""


class ProductList(APIView):

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
A dedicated API for search and filter function
"""


class ProductListAPIVIew(ListAPIView):
     serializer_class = ProductSerializer
     queryset = Product.objects.all()

     filter_fields = (
         'category__id',
     )
     search_fields = (
         'title',
    )


"""
Calls Category model, serializes the data and returns it to the client
"""


class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""
Calls Seller model, serializes the data and returns it to the client
"""


class SellerList(APIView):
    def get(self, request):
        sellers = Seller.objects.all()
        serializer = SellerSerializer(sellers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)