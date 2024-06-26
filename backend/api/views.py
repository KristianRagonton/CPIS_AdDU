# handle CRUD here

from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer, ProductSerializer, InventorySerializer 
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Product, Inventory

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    
class ProductCreate(generics.CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

class ProductDetail(APIView):
    def delete(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny] 
    
class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

class InventoryListView(generics.ListAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = [AllowAny] 

class StockInView(generics.CreateAPIView):
    serializer_class = InventorySerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            product = serializer.validated_data['product']
            stock_in = serializer.validated_data['stock']
            try:
                inventory = Inventory.objects.get(product=product)
                inventory.stock += stock_in
                inventory.save()
            except Inventory.DoesNotExist:
                Inventory.objects.create(product=product, stock=stock_in)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class StockOutView(generics.CreateAPIView):
    serializer_class = InventorySerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            product = serializer.validated_data['product']
            stock_out = serializer.validated_data['stock']
            try:
                inventory = Inventory.objects.get(product=product)
                if inventory.stock >= stock_out:
                    inventory.stock -= stock_out
                    inventory.save()
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Not enough stock'}, status=status.HTTP_400_BAD_REQUEST)
            except Inventory.DoesNotExist:
                return Response({'error': 'Product not found in inventory'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
