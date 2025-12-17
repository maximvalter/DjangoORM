from django.shortcuts import render
from .models import Book

def books_view(request, pub_date=None):
    # Список всех уникальных дат
    dates = list(Book.objects.order_by("pub_date")
                 .values_list("pub_date", flat=True)
                 .distinct())

    books = Book.objects.order_by("pub_date", "id")
    # Значения для ссылок "предыдущая дата" и "следующая дата"
    prev_date = next_date = None

    # Если передали конкретную дату — фильтруем книги только по этой дате
    if pub_date is not None:
        books = books.filter(pub_date=pub_date)
        # Если такая дата реально есть среди дат в базе — вычисляем соседние даты
        if pub_date in dates:
            i = dates.index(pub_date)
            prev_date = dates[i - 1] if i > 0 else None # предыдущая дата, если не первая
            next_date = dates[i + 1] if i < len(dates) - 1 else None # следующая дата, если не последняя

    return render(request, "books/books_list.html", {
        "books": books,
        "pub_date": pub_date,
        "prev_date": prev_date,
        "next_date": next_date,
    })
