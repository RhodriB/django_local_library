from django.contrib import admin

# Register your models here.

from .models import Author, Genre, Book, BookInstance, Language

class BookInline(admin.TabularInline):
    model = Book
    extra = 0

# admin.site.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    
    inlines = [BookInline]

admin.site.register(Author, AuthorAdmin)

admin.site.register(Genre)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0

# admin.site.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    
    inlines = [BookInstanceInline]

# admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    
    fieldsets = (
    (None, {
    'fields': ('book', 'imprint', 'id')
     }),
     ('Availability', {
     'fields': ('status', 'due_back', 'borrower')
      }),
                 )

admin.site.register(Language)
