from rest_framework import serializers

from lab_quote.models import Quote


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('id', 'text', 'created_at', 'author_name', 'author_email', 'rating', 'status')