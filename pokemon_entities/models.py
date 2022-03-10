from django.db import models  # noqa F401


class Pokemon(models.Model):
    """Покемон"""
    title_ru = models.CharField(max_length=200, verbose_name="название")
    title_en = models.CharField(
        max_length=200, default="", verbose_name="английское название", blank=True)
    title_jp = models.CharField(
        max_length=200, default="", verbose_name="японское название", blank=True)
    image = models.ImageField(null=True, blank=True,
                              verbose_name="изображение")
    description = models.TextField(
        default="", blank=True, verbose_name="описание")
    next_evolution = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        related_name="previous_evolution",
        null=True,
        blank=True,
        verbose_name="в кого эволюционирует")

    def __str__(self) -> str:
        return self.title_ru


class PokemonEntity(models.Model):
    """Сущности покемонов на карте"""
    pokemon = models.ForeignKey(
        Pokemon, on_delete=models.CASCADE, verbose_name="покемон")
    latitude = models.FloatField(verbose_name="широта")
    longitude = models.FloatField(verbose_name="долгота")
    appeared_at = models.DateTimeField(verbose_name="когда появится", default=None, blank=True)
    disappeared_at = models.DateTimeField(verbose_name="когда исчезнет", default=None, blank=True)
    level = models.IntegerField(verbose_name="уровень", null=True, blank=True)
    health = models.IntegerField(verbose_name="здоровье", null=True, blank=True)
    strength = models.IntegerField(verbose_name="атака", null=True, blank=True)
    defence = models.IntegerField(verbose_name="защита", null=True, blank=True)
    stamina = models.IntegerField(verbose_name="выносливость", null=True, blank=True)
