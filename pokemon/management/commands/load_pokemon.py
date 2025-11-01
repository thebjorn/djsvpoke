import json
from django.core.management.base import BaseCommand
from pokemon.models import Pokemon
from pathlib import Path


class Command(BaseCommand):
    help = 'Load Pokemon data from pokemons.json file'

    def handle(self, *args, **options):
        # Get the base directory (project root)
        base_dir = Path(__file__).resolve().parent.parent.parent.parent
        json_file = base_dir / 'pokemons.json'

        self.stdout.write(f'Loading Pokemon data from {json_file}...')

        # Clear existing Pokemon data
        Pokemon.objects.all().delete()
        self.stdout.write(self.style.WARNING('Cleared existing Pokemon data'))

        # Load JSON data
        with open(json_file, 'r', encoding='utf-8') as f:
            pokemon_data = json.load(f)

        # Create Pokemon objects
        pokemon_objects = []
        for data in pokemon_data:
            # Join types array into comma-separated string
            types_str = ','.join(data['types'])

            pokemon = Pokemon(
                pokemon_id=data['id'],
                name=data['name'],
                height=data['height'],
                weight=data['weight'],
                types=types_str,
                family=data['family']
            )
            pokemon_objects.append(pokemon)

        # Bulk create for efficiency
        Pokemon.objects.bulk_create(pokemon_objects)

        self.stdout.write(
            self.style.SUCCESS(f'Successfully loaded {len(pokemon_objects)} Pokemon!')
        )
