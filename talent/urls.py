from django.urls import path
from .views import TalentListView, TalentDetailView

urlpatterns = [
    path('', TalentListView.as_view()),
    path('<int:talent_id>/', TalentDetailView.as_view())
]