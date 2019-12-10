from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets

from api.serializers import QuoteSerializer
from lab_quote.models import Quote


class LogoutView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        user = self.request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'ok'})


class QuoteViewset(viewsets.ModelViewSet):
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer