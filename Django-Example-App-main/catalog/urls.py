from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("books", views.BookListView.as_view(), name="books"),
    path("book/<int:pk>", views.BookDetailView.as_view(), name="book"),
    path("authors", views.AuthorListView.as_view(), name="authors"),
    path("author/<int:pk>", views.AuthorDetailView.as_view(), name="author"),
    path(
        "book/instance/<uuid:pk>/reserve",
        views.reserve_book_form,
        name="reserve-book-form",
    ),
    path("authors/create", views.AuthorCreateView.as_view(), name="author-create"),
    path(
        "author/<int:pk>/update", views.AuthorUpdateView.as_view(), name="author-update"
    ),
    path(
        "author/<int:pk>/delete", views.AuthorDeleteView.as_view(), name="author-delete"
    ),

]
