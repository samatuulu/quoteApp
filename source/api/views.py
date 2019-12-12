from rest_framework.generics import get_object_or_404
from rest_framework.permissions import BasePermission, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from api.serializers import QuoteSerializer
from lab_quote.models import Quote, QUOTE_APPROVED


class LogoutView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class IsQuotOwner(BasePermission):

    def has_permission(self, request, view):
        return  request.user.has_perm('lab_quote.change_quote')

    def has_object_permission(self, request, view, obj):
        user = request.user
        return obj.user == user


class QuoteViewset(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    queryset = Quote.objects.none()
    serializer_class = QuoteSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Quote.objects.all()
        else:
            return Quote.objects.filter(status=QUOTE_APPROVED)


class RateUPView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, pk=None):
        quote = get_object_or_404(Quote, pk=pk)
        if quote.status != QUOTE_APPROVED:
            return Response({'error': 'Quote is not approved1'}, status=400)
        quote.rating += 1
        quote.save()
        return Response({'id': quote.pk, 'rating': quote.rating})


class RateDownView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, pk=None):
        quote = get_object_or_404(Quote, pk=pk)
        if quote.status != QUOTE_APPROVED:
            return Response({'error': 'Quote is not approved1'}, status=400)
        quote.rating -= 1
        quote.save()
        return Response({'id': quote.pk, 'rating': quote.rating})