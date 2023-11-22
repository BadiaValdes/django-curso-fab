from django.contrib import admin
from .models import Store, Category, List, VideoGames, StoreGame


# Register your models here.


@admin.register(Store,Category,List,VideoGames, StoreGame)
class SoreAdmin(admin.ModelAdmin):
    pass
