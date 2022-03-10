from django.db import models  # noqa F401


class Pokemon(models.Model):
    """Покемон"""
    title_ru = models.CharField(max_length=200, verbose_name="название")
    title_en = models.CharField(
        max_length=200, default="", verbose_name="английское название")
    title_jp = models.CharField(
        max_length=200, default="", verbose_name="японское название")
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
    appeared_at = models.DateTimeField(verbose_name="когда появится")
    disappeared_at = models.DateTimeField(verbose_name="когда исчезнет")
    level = models.IntegerField(verbose_name="уровень")
    health = models.IntegerField(verbose_name="здоровье")
    strength = models.IntegerField(verbose_name="атака")
    defence = models.IntegerField(verbose_name="защита")
    stamina = models.IntegerField(verbose_name="выносливость")
