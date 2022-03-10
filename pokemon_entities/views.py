import folium
from django.http import HttpResponseNotFound
from django.shortcuts import render

from .models import Pokemon, PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision"
    "/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832"
    "&fill=transparent"
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemon_entities = PokemonEntity.objects.all()

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon_entity in pokemon_entities:
        add_pokemon(
            folium_map, pokemon_entity.latitude,
            pokemon_entity.longitude,
            request.build_absolute_uri(pokemon_entity.pokemon.image.url)
        )

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        pokemon_image_url = None
        if pokemon.image:
            pokemon_image_url = pokemon.image.url
        pokemons_on_page.append({
            "pokemon_id": pokemon.id,
            "img_url": pokemon_image_url,
            "title_ru": pokemon.title_ru,
        })

    return render(request, "mainpage.html", context={
        "map": folium_map._repr_html_(),
        "pokemons": pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    try:
        bd_pokemon = Pokemon.objects.get(pk=pokemon_id)
    except Pokemon.DoesNotExist:
        return HttpResponseNotFound("<h1>Такой покемон не найден</h1>")

    pokemon = {
        "title_ru": bd_pokemon.title_ru,
        "title_en": bd_pokemon.title_en,
        "title_jp": bd_pokemon.title_jp,
        "description": bd_pokemon.description,
        "img_url": request.build_absolute_uri(bd_pokemon.image.url),
    }
    evolution_pokemon = bd_pokemon.next_evolution
    if evolution_pokemon is not None:
        pokemon["next_evolution"] = {
            "pokemon_id": evolution_pokemon.id,
            "title_ru": evolution_pokemon.title_ru,
            "img_url": request.build_absolute_uri(evolution_pokemon.image.url),
        }

    if bd_pokemon.previous_evolution.count():
        evolution_pokemon = bd_pokemon.previous_evolution.get()
        pokemon["previous_evolution"] = {
            "pokemon_id": evolution_pokemon.id,
            "title_ru": evolution_pokemon.title_ru,
            "img_url": request.build_absolute_uri(evolution_pokemon.image.url),
        }

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    requested_entites = PokemonEntity.objects.filter(pokemon=bd_pokemon)
    for pokemon_entity in requested_entites:
        add_pokemon(
            folium_map, pokemon_entity.latitude,
            pokemon_entity.longitude,
            pokemon["img_url"]
        )

    return render(request, "pokemon.html", context={
        "map": folium_map._repr_html_(), "pokemon": pokemon
    })
