from django.urls import path
from blogs.views import ArticleListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView, ArticleCreateFunctionView


app_name = "articles"
urlpatterns = [
    path('', ArticleListView.as_view(), name="list-view"),
    path('<int:id>/', ArticleDetailView.as_view(), name='detail-view'),
    path('create/', ArticleCreateView.as_view(), name='create-view'),
    path('function-create/', ArticleCreateFunctionView.as_view(),
         name='create-view'),
    path('<int:id>/update/', ArticleUpdateView.as_view(), name='update-view'),
    path('<int:id>/delete/', ArticleDeleteView.as_view(), name='delete-view')
]

