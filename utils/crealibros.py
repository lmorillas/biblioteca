from catalogo.models import Book

for n in range(1, 1000):
    b = Book(title=f'Libro de prueba {n}')
    b.save()
