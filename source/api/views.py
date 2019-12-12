from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets, permissions

from api.serializers import QuoteSerializer
from lab_quote.models import Quote, QUOTE_APPROVED, QUOTE_STATUS_CHOICES
from rest_framework.authtoken.models import Token




class LogoutView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class QuoteViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return Quote.objects.all()
        else:
            return Quote.objects.filter(status=QUOTE_APPROVED)