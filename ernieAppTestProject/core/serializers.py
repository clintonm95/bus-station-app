from rest_framework import serializers
from .models import Bus, Driver, SeatReservation


class BusDetailsSerializer(serializers.ModelSerializer):
    reserved_seats = serializers.ReadOnlyField()

    def get_reserved_seats(self, obj):
        return obj.reserved_seats

    class Meta:
        model = Bus
        fields = "__all__"
        read_only_fields = [
            "id",
            "liscence_plate",
            "starting_station",
            "final_station",
            "status",
            "max_seats",
            "driver",
            "time_of_departure",
        ]


class BusListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bus
        fields = [
            "id",
            "liscence_plate",
            "time_of_departure",
            "starting_station",
            "final_station",
        ]


class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"


class SeatReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeatReservation
        fields = "__all__"
