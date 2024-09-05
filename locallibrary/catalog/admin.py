from django.contrib import admin
from catalog.models import Author, Book, BookInstance, Genre, Language

# Register your models here. The easiest approach

# admin.site.register(Author)
# admin.site.register(Book)
# admin.site.register(BookInstance)
admin.site.register(Genre)
admin.site.register(Language)

# Register ModelAdmin class, Admin Site customization

# Method 1
# 1 Define the admin class
# 2 Register the admin class with the associated model

class BookInline(admin.TabularInline):
    model = Book
    extra = 1
class AuthorAdmin(admin.ModelAdmin):
    # List View configuration 
    # select to change list
    list_display = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    list_filter= ['date_of_birth']
    
    # Detail View configuration
    # change page
    
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    
    #Inline editing of a book in Author
    inlines = [BookInline]
    
admin.site.register(Author, AuthorAdmin)

# repeat for Book, and BookInstance
# Configure BookInstance for Inline editing
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 1
# Method 2: method 1 done in 1 step
# 1 Define and Register the Admin class for Book and BookInstance 
#   using decorator
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # List View 
    list_display = ['title', 'author', 'language', 'display_genre']
    
    # detail view
    fields = ['title', 'summary', 'isbn', ('author', 'language'), 'genres']
    
    # Inline editing of BookInstance
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # List View
    list_display = ('book', 'status', 'due_back')
    list_filter = ('status', 'due_back')
    
    # Detail View
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'id')
        }),
        ('More Details',{
            'fields': (('status', 'due_back'),)
        } 
         )
    )
    
    