from django.shortcuts import render
from django.views import generic
from .models import Author, Book, BookInstance, Genre, Language

# Create your views here.

# home_page
def index(request):
    """Home page function view."""
    
    #1 Counts of main objects
    website_title = 'Local Library'
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_authors = Author.objects.count()
    num_genres = Genre.objects.count()
    
    
    #2 Available books (status = a), (genre = Text Book)
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    #2.1 get the id of exact genre (M2M reverse)
    genre_id = Genre.objects.get(name__exact='Text Book')
    #
    num_text_books_available = genre_id.book_set.all()
    genre_count = genre_id.book_set.count()
    
    #3 Contexts - data to pass to the template for processing
    context = {
        'website_title': website_title,
        'num_books': num_books,
        'num_instances': num_instances,
        'num_authors': num_authors,
        'num_instances_available': num_instances_available,
        'num_genres': num_genres,
        'genre_count': genre_count,
        'num_text_books_available': num_text_books_available,
    }
    
    #4 Render the HTML templat index.html with data in the context
    return render(request, 'index.html', context=context)

# Book list view
class BookListView(generic.ListView):
    model = Book
    paginate_by = 20
# Book detail view
class BookDetailView(generic.DetailView):
    model = Book
    
# Author list view
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 20
class AuthorDetailView(generic.DetailView):
    model = Author