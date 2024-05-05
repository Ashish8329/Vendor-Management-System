from rest_framework import serializers

from performance_history.models import HistoricalPerformance


class HistoricalPerformanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoricalPerformance
        fields = "__all__"
