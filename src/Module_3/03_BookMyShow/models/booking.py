# models/booking.py
from enum import Enum, auto

from models.base_model import BaseModel
from sqlalchemy import ForeignKey, declarative_base
from sqlalchemy import Column, Integer, DateTime, SAEnum, relationship


class BookingStatus(Enum):
    CONFIRMED = auto()
    CANCELLED = auto()
    PENDING = auto()


class Booking(BaseModel):
    __tablename__ = "bookings"

    # def __init__(self, booking_status, show_seats, user, booked_at, show, amount):
    #     super().__init__()
    #     self.booking_status = booking_status
    #     self.show_seats = show_seats
    #     self.user = user
    #     self.booked_at = booked_at
    #     self.show = show
    #     self.amount = amount
    #     self.payments = []

    user_id = Column(Integer, ForeignKey("users.id"))
    # being able to move from one python object to another python object using an attribute 
    # is called as relationship in SQLAlchemy . AKA Python side navigation
    user = relationship("User", back_populates="bookings")
    # back_populates is used to define the reverse relationship from User to Booking.
    #  It allows us to access the bookings associated with a user using user.bookings.

    show_id = Column(Integer, ForeignKey("shows.id"))
    show = relationship("Show")

    booking_status = Column(SAEnum(BookingStatus), default=BookingStatus.PENDING)

    # 1 booking -> M show_seats
    # 1 show_seat -> 1 booking
    # 1 : M relationship between booking and show_seats


    # 1 booking -> M payments
    # 1 payment -> 1 booking
    # 1 : M relationship between booking and payments

    # booking object  -- booking.user_id