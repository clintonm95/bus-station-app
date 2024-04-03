import uuid
from django.db import models


class Driver(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    birth_date = models.DateTimeField()
    year_of_driving_experience = models.IntegerField()
    starting_date = models.DateTimeField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Bus(models.Model):
    STATUS = [
        ("ON PLATFORM", "On platform"),
        ("ARRIVING", "Arriving"),
        ("LEAVING", "Leaving"),
        ("LEFT", "Left"),
    ]
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    liscence_plate = models.SlugField(max_length=100)
    driver = models.ForeignKey(Driver, null=True, on_delete=models.SET_NULL)
    time_of_departure = models.DateTimeField()
    max_seats = models.IntegerField()
    starting_station = models.CharField(max_length=100)
    final_station = models.CharField(max_length=100)
    status = models.CharField(choices=STATUS, max_length=11)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f"BUS {self.liscence_plate} {self.starting_station} - {self.final_station}"
        )

    @property
    def reserved_seats(self):
        return [seat.seat_number for seat in self.seatreservation_set.all()]

    class Meta:
        verbose_name_plural = "Buses"


class SeatReservation(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    bus = models.ForeignKey(Bus, on_delete=models.SET_NULL, null=True)
    seat_number = models.IntegerField()
    passenger_fullname = models.CharField(max_length=100)

    def __str__(self):
        return self.passenger_fullname

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["bus", "seat_number"], name="unique_seat_per_bus"
            )
        ]
