import json

from django.core.management import BaseCommand

from catalog.models import Category

class Command(BaseCommand):
    def handle(self):
        lst = []
        with open('data.json', 'r', encoding = 'utf-8') as file:
            lst = [Category(**cvarks['fields']) for cvarks in json.load(file)]
        self.delite_data()
        Category.objects.bulk_create(lst)

    def delite_data(self):
        Category.objects.all().delete()