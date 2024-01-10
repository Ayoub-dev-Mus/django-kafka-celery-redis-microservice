# views.py
import json
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from  kafka_integration.views import send_kafka_message
from .serializers import ProductSerializer
from .services.productServiceImpl import ProductServiceImpl
from django.http import HttpResponseServerError




class ProductViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            product_service = ProductServiceImpl()
            products = product_service.find_all_products()
            serializer = ProductSerializer(products, many=True)
            send_message = send_kafka_message(request,serializer.data)
            return Response({'products': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
             return HttpResponseServerError(e)

    def create(self, request):
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                product_service = ProductServiceImpl()
                new_product = product_service.create_product(serializer.validated_data)
                send_message = send_kafka_message(request, ProductSerializer(new_product).data)
                return Response({'product': ProductSerializer(new_product).data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
              return HttpResponseServerError(e)

    def retrieve(self, request, pk=None):
        try:
            product_service = ProductServiceImpl()
            existing_product = product_service.find_product_by_id(pk)
            if existing_product:
                serializer = ProductSerializer(existing_product)
                return Response({'product': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
           return HttpResponseServerError(e)

    def partial_update(self, request, pk=None):
        try:
            print()
            product_service = ProductServiceImpl()
            existing_product = product_service.find_product_by_id(pk)
            if existing_product:
                serializer = ProductSerializer(instance=existing_product, data=request.data, partial=True)
                if serializer.is_valid():
                    updated_product = product_service.update_product(pk, serializer.validated_data)
                    return Response({'product': ProductSerializer(updated_product).data}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Validation error', 'details': serializer.errors},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
           return HttpResponseServerError(e)



    def destroy(self, request, pk=None):
        try:
            product_service = ProductServiceImpl()
            product_exists = product_service.find_product_by_id(pk)

            print(product_exists)
            if not product_exists:
                return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

            success = product_service.delete_product(pk)

            print(success)

            if success:
                return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error': 'Failed to delete product'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def search(self, request):
        try:
            keyword = request.GET.get('keyword', '')
            if keyword:
                product_service = ProductServiceImpl()
                products = product_service.search_products(keyword)
                serializer = ProductSerializer(products, many=True)
                return Response({'products': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Please provide a keyword for search'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return HttpResponseServerError(e)

    @action(detail=False, methods=['get'])
    def get_top_rated_products(self, request):
        try:
            product_service = ProductServiceImpl()
            products = product_service.find_all_products()
            serializer = ProductSerializer(products, many=True)
            return Response({'products': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
           return HttpResponseServerError(e)
