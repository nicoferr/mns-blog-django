from django.urls import path
from .views import articles_list, articles_details

urlpatterns = [
    path('', articles_list, name="articles_list"),
    path('<int:article_id>/', articles_details, name="articles_details")
]