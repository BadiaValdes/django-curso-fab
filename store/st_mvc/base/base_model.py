from django.db import models
from ..auxiliar import validate_length, NAME_MAX_LENGTH, NAME_MIN_LENGTH
import uuid


def generate_uuid() -> str:
    return uuid.uuid4().hex


class BaseModel(models.Model):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True)


    class Meta:
        abstract = True # Hacemos que esta clase sea abstracta; de esta forma los hijos pueden heredar los atributos del padre.
        ordering = ['name'] # Seteamos como estarán ordenados los elementos


class BaseModelWithName(BaseModel):
    id = models.CharField(primary_key=True, default=generate_uuid, editable=False, unique=True)
    # El validador puesto aqui saldra como error debajo del campo
    name = models.CharField(editable=True, unique=True, max_length=NAME_MAX_LENGTH, db_index=True,validators=[validate_length(field='name',max_length=NAME_MAX_LENGTH, min_length=NAME_MIN_LENGTH)], verbose_name="Nombre") # Validators

    def __str__(self):
        return self.name;

    class Meta:
        abstract = True # Hacemos que esta clase sea abstracta; de esta forma los hijos pueden heredar los atributos del padre.
        ordering = ['name'] # Seteamos como estarán ordenados los elementos