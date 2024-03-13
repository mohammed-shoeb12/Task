# from django.urls import path
# from rest_framework.routers import DefaultRouter
# from .views import BookViewSet, AuthorViewSet

# router = DefaultRouter()
# router.register(r'books', BookViewSet)
# router.register(r'authors', AuthorViewSet)

# urlpatterns = router.urls

from django.urls import path
from .views import BookListView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('create/', BookCreateView.as_view(), name='book-create'),
    path('<int:pk>/update/', BookUpdateView.as_view(), name='book-update'),
    path('<int:pk>/delete/', BookDeleteView.as_view(), name='book-delete'),
]