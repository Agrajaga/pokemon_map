from django.db import models  # noqa F401


class Pokemon(models.Model):
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, default="")
    title_jp = models.CharField(max_length=200, default="")
    image = models.ImageField(null=True, blank=True)
    description = models.TextField(default="", blank=True)
    next_evolution = models.ForeignKey(
        "self", 
        on_delete=models.DO_NOTHING, 
        related_name="+",
        null=True, 
        blank=True)
    previous_evolution = models.ForeignKey(
        "self", 
        on_delete=models.DO_NOTHING,
        related_name="+", 
        null=True, 
        blank=True)

    def __str__(self) -> str:
        return self.title_ru


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    latitude = models.FloatField(name="Lat")
    longitude = models.FloatField(name="Lon")
    appeared_at = models.DateTimeField()
    disappeared_at = models.DateTimeField()
    level = models.IntegerField()
    health = models.IntegerField()
    strength = models.IntegerField()
    defence = models.IntegerField()
    stamina = models.IntegerField()
