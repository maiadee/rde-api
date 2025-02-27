from django.urls import path
from .views import UserProposalListView, AdminProposalListView, SingleProposalView


urlpatterns = [
    path("user/", UserProposalListView.as_view()),
    path("admin/", AdminProposalListView.as_view()),
    path("<int:proposal_id>/", SingleProposalView.as_view())
]