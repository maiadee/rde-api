from django.urls import path
from .views import UserProposalListView


urlpatterns = [
    path('', UserProposalListView.as_view())
]