from django.urls import path
from . import views

urlpatterns = [
    path('applyLoan', views.applyLoan, name='applyLoan'),
    path('uploadDocument/<basicdetails_id>',
         views.uploadDocument, name='uploadDocument'),
    path('reviewApplication/<basicdetails_id>',
         views.reviewApplication, name='reviewApplication'),
    path('submitApplication/<basicdetails_id>',
         views.submitApplication, name='submitApplication'),
    path('editDetails/<basicdetails_id>',
         views.editDetails, name='editDetails'),
    path('viewAllLoan',
         views.viewAllLoan, name='viewAllLoan'),
]
