# models/payment.py
from enum import Enum, auto

from sqlalchemy import Column, Float, ForeignKey, String, SAEnum, Integer

from models.base_model import BaseModel


class PaymentProvider(Enum):
    PAYU = auto()
    RAZORPAY = auto()


class PaymentStatus(Enum):
    SUCCESS = auto()
    FAILURE = auto()
    REFUNDED = auto()


class Payment(BaseModel):
    # def __init__(self, ref_no, amount, payment_provider, payment_status):
    #     super().__init__()
    #     self.ref_no = ref_no
    #     self.amount = amount
    #     self.payment_provider = payment_provider
    #     self.payment_status = payment_status

    ref_no = Column(String)
    amount = Column(Float)
    payment_provider = Column(SAEnum(PaymentProvider))
    payment_status = Column(SAEnum(PaymentStatus))

    # 1 payment -> 1 booking
    # 1 booking -> M payments

    booking_id = Column(Integer, ForeignKey("bookings.id"))