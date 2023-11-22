from .base import BaseModel, BaseModelWithName
from django.db import models
import uuid

# Create your models here.


# Creamos nuestro modelo. Para hacer que una clase sea de tipo modelo, debemos extender de models.Model

class Category(BaseModelWithName):
    description = models.CharField(max_length=100, null=False)

class VideoGames(BaseModelWithName):
    image = models.ImageField(upload_to="mvc_image")
    description = models.CharField(max_length=150, null=False)
    rate = models.CharField(max_length=5)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)



class Store(BaseModelWithName):
    dir = models.CharField(max_length=100, null=True)
    games = models.ManyToManyField(VideoGames, through="StoreGame") # La palabra through nos permite definir una tercera tabla que trabaja como intermediario en una relación de muchos a muchos
    category = models.ManyToManyField(Category, blank=True) # La relaci'on de muchos a muchos se debe definir en el componente contenedor. En este caso, la tienda posee diferentes categorías de juegos

class StoreGame(BaseModel):
    game = models.ForeignKey(VideoGames, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    price = models.FloatField()

    def __str__(self): # El str es la contraparte del toString en java. Permite devolver una representación de la clase
        return f'{self.game}-{self.store}'

    class Meta:
        db_table = "store_game"

class List(BaseModelWithName):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)  # Creamos la relación de muchos a uno con Store
    games = models.ManyToManyField(VideoGames)

    class Meta:
        db_table = "video_game"
