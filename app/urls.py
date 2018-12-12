from django.urls import path
from .views import ItemFilterView, ItemCreateView, ItemDetailView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path("", ItemFilterView.as_view(), name="index"),
    path("detail/<int:pk>/", ItemDeleteView.as_view(), name="detail"),
    path("create/", ItemCreateView.as_view(), name="create"),
    path("update/<int:pk>/", ItemUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", ItemDeleteView.as_view(), name="delete"),
]