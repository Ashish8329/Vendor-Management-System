# serializers.py
from performance_history.models import HistoricalPerformance
from rest_framework import serializers


class VedorHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoricalPerformance
        fields = [
            "vendor",
            "on_time_delivery_rate",
            "average_response_time",
            "quality_rating_avg",
            "fulfillment_rate",
        ]
