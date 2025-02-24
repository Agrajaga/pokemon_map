# Generated by Django 3.1.14 on 2022-03-10 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_auto_20220310_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemonentity',
            name='defence',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='health',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='level',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='stamina',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pokemonentity',
            name='strength',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]
