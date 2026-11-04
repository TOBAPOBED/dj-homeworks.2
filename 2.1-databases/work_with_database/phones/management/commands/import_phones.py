import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # Создаём объект Phone из строки CSV
            Phone.objects.create(
                id=int(phone['id']),
                name=phone['name'],
                price=float(phone['price']),
                image=phone['image'],
                release_date=phone['release_date'],
                lte_exists=phone['lte_exists'].lower() == 'true',
            )
            self.stdout.write(self.style.SUCCESS(
                f'Добавлен телефон: {phone["name"]}'
            ))
        
        self.stdout.write(self.style.SUCCESS('Импорт завершён!'))
