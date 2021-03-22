from django.db import models
from app.model.base import Base
from app.model.users import User


class Advisor(Base):
    # user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    photo_url = models.URLField()

    def __str__(self):
        return self.name