import csv
from datetime import date

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open("phones.csv", encoding="utf-8", newline="") as f:
            for row in csv.DictReader(f, delimiter=";"):
                name = row["name"].strip()

                Phone.objects.update_or_create(
                    id=int(row["id"]),
                    defaults={
                        "name": name,
                        "image": row["image"].strip(),
                        "price": int(row["price"]),
                        "release_date": date.fromisoformat(row["release_date"].strip()),
                        "lte_exists": row["lte_exists"].strip().lower() in {"true", "1", "yes"},
                        "slug": slugify(name),
                    },
                )
