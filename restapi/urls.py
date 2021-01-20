from django.urls import path, include
from .views import BankDetailAutocompleteView, BankDetailSearchView

app_name = 'restapi'
urlpatterns = [
    path('', BankDetailSearchView.as_view(), name="bank-search"),
    path('autocomplete/', BankDetailAutocompleteView.as_view(), name="bank-autocomplete")
    
]