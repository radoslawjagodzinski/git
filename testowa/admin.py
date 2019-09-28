from django.contrib import admin

# Register your models here.
from testowa.models import Movie, Genre

class MovieInLine(admin.TabularInline):
    model = Movie
    extra =1
class GenreListAdmin(admin.ModelAdmin):
    inlines = (MovieInLine, )

admin.site.register(Movie)
admin.site.register(Genre, GenreListAdmin)