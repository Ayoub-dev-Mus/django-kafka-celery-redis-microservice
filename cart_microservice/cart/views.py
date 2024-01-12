from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import CartSerializer
from .services.cartServiceImpl import CartServiceImpl
from django.http import HttpResponseServerError
from kafka_integration.tasks import run_kafka_consumer
from kafka_integration.kafka_consumer import consume_messages
class CartViewSet(viewsets.ViewSet):

    def list(self, request):
        try:
            cart_service = CartServiceImpl()
            carts = cart_service.find_all_carts()
            serializer = CartSerializer(carts, many=True)
            return Response({'carts': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return HttpResponseServerError(e)

    def create(self, request):
        try:
            serializer = CartSerializer(data=request.data)
            if serializer.is_valid():
                cart_service = CartServiceImpl()
                new_cart = cart_service.add_product_to_cart(serializer.validated_data)
                result = run_kafka_consumer.delay()

                kafka_consumer_result = result.get()


                print(f"Kafka consumer result: {kafka_consumer_result}")

                return Response({'cart': CartSerializer(new_cart).data}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return HttpResponseServerError(e)

    def retrieve(self, request, pk=None):
        try:
            cart_service = CartServiceImpl()
            existing_cart = cart_service.find_cart_by_user_id(pk)
            if existing_cart:
                serializer = CartSerializer(existing_cart)
                return Response({'cart': serializer.data}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return HttpResponseServerError(e)

    def partial_update(self, request, pk=None):
        try:
            cart_service = CartServiceImpl()
            existing_cart = cart_service.find_cart_by_user_id(pk)
            if existing_cart:
                serializer = CartSerializer(instance=existing_cart, data=request.data, partial=True)
                if serializer.is_valid():
                    updated_cart = cart_service.update_cart(pk, serializer.validated_data)
                    return Response({'cart': CartSerializer(updated_cart).data}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Validation error', 'details': serializer.errors},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return HttpResponseServerError(e)

    def destroy(self, request, pk=None):
        try:
            cart_service = CartServiceImpl()
            cart_exists = cart_service.find_cart_by_user_id(pk)
            if not cart_exists:
                return Response({'error': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

            success = cart_service.clear_cart(pk)

            if success:
                return Response({'message': 'Cart cleared successfully'}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({'error': 'Failed to clear cart'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=False, methods=['get'])
    def get_top_rated_carts(self, request):
        try:
            cart_service = CartServiceImpl()
            carts = cart_service.find_all_carts()
            serializer = CartSerializer(carts, many=True)
            return Response({'carts': serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return HttpResponseServerError(e)
