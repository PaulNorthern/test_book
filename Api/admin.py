from django.contrib import admin
from .models import Author, Book


class AuthorAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'birth_date', 'gender')
    list_filter = ('gender', )
    list_per_page = 25


admin.site.register(Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Book)
