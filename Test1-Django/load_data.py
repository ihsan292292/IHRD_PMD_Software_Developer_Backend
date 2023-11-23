import json
from django.core.management.base import BaseCommand
from users.models import CountryPopulation

class Command(BaseCommand):
    help = 'Load population data from JSON file into the database'

    def handle(self, *args, **kwargs):
        with open('dataset_world_population_by_country_name.json', 'r') as file:
            data = json.load(file)

        for entry in data:
            country = entry['country']
            population = entry['population']
            CountryPopulation.objects.update_or_create(country=country, defaults={'population': population})

        self.stdout.write(self.style.SUCCESS('Population data has been loaded successfully'))
