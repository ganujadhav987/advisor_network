from django.db import models
from app.model.base import Base
from app.model.users import User
from app.model.advisor import Advisor


class Booking(Base):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    advisor = models.ForeignKey(Advisor, on_delete=models.SET_NULL, null=True)
    date_time = models.DateTimeField()
