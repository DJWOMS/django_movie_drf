from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views, api

urlpatterns = format_suffix_patterns([
    path("movie/", views.MovieViewSet.as_view({'get': 'list'})),
    path("movie/<int:pk>/", views.MovieViewSet.as_view({'get': 'retrieve'})),
    path("review/", views.ReviewCreateViewSet.as_view({'post': 'create'})),
    path("rating/", views.AddStarRatingViewSet.as_view({'post': 'create'})),
    path('actor/', views.ActorsViewSet.as_view({'get': 'list'})),
    path('actor/<int:pk>/', views.ActorsViewSet.as_view({'get': 'retrieve'})),
])


# urlpatterns = [
    # path("movie/", views.MovieListView.as_view()),
    # path("movie/<int:pk>/", views.MovieDetailView.as_view()),
    # path("review/", views.ReviewCreateView.as_view()),
    # path("rating/", views.AddStarRatingView.as_view()),
    # path("actors/", views.ActorsListView.as_view()),
    # path("actors/<int:pk>/", views.ActorsDetailView.as_view()),
# ]


###########
# router = DefaultRouter()
# router.register(r'actor-set', api.ActorViewSet, basename='actor')
# router.register(r'actor-read', api.ActorReadOnly, basename='actor')
# router.register(r'actor-modelset', api.ActorModelViewSet, basename='actor')
# urlpatterns = router.urls
