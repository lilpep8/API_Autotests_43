from pydantic import BaseModel
from typing import Optional


class BookingDates(BaseModel):
    checkin: str
    checkout: str


class BookingResponse(BaseModel):
    firstname: str
    lastname: str
    totalprice: int
    depositpaid: bool
    bookingdates: BookingDates
    additionalneeds: Optional[str] = None


# Отдельная модель для дат в методе PATCH
class PatchedBookingDates(BaseModel):
    checkin: Optional[str]
    checkout: Optional[str]


# Отдельная модель для метода PATCH
class PatchedBookingResponse(BaseModel):
    firstname: Optional[str] = None
    lastname: Optional[str] = None
    totalprice: Optional[int] = None
    depositpaid: Optional[bool] = None
    bookingdates: Optional[PatchedBookingDates] = None
    additionalneeds: Optional[str] = None
