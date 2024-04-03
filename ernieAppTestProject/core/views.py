from rest_framework import mixins, viewsets
from .models import Bus, SeatReservation
from .serializers import (
    BusDetailsSerializer,
    BusListSerializer,
    SeatReservationSerializer,
)

# Create your views here.


class BusViewset(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    queryset = Bus.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return BusListSerializer
        if self.action == "retrieve":
            return BusDetailsSerializer
        return super().get_serializer_class()


class SeatReservationModelViewset(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = SeatReservation.objects.all()
    serializer_class = SeatReservationSerializer


# TODO logic for the service required every 6 months for each buses
#  may need to extend models status field with a new status for this purpose ...
