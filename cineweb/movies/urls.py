from django.urls import path

from . import views

urlpatterns = [

    path('movies/',views.MovieListCreateView.as_view()),

    path('movies/<str:uuid>/',views.MovieRetrieveUpdateDestroyView.as_view()),

    path('industries/',views.IndustryListCreateView.as_view()),

    path('recommended-movies/<str:uuid>/',views.RecommendedMoviesView.as_view()),
]