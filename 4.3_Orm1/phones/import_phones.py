import csv
from datetime import datetime
from django.core.management.base import BaseCommand
from models import Phone

class Command(BaseCommand):
    help = 'Import phones from csv file'

    def handle(self, *args, **options):
        with open('phones.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                phone = Phone()
                phone.name = row['name']
                phone.price = row['price']
                phone.image = row['image']
                phone.release_date = datetime.strptime(row['release_date'], '%Y-%m-%d').date()
                phone.lte_exists = row['lte_exists']
                phone.save()