from app import books


def print_best_books():
    best_books = sorted(books, key=lambda x: x.rating)
    for book in best_books:
        print(book)


def print_cheapest_books():
    cheapest_books = sorted(books, key=lambda x: x.price)
    for book in cheapest_books:
        print(book)


print_cheapest_books()
# print_best_books()
