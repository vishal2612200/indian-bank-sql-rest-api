from django.shortcuts import render
from django.http import Http404
from rest_framework import generics
from django.db.models import Q

from .models import Branch
from .serializer import BranchDetailSerializer
from functools import reduce
import operator

# Create your views here.

class BankDetailAutocompleteView(generics.ListAPIView):
    """ 
    GET autocomplete/?q=<name>&limit=<limit>&offset=<offset>
    """

    serializer_class = BranchDetailSerializer

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query == None:
            raise Http404("URL does not exist")
        return Branch.objects.filter(branch__startswith=query).order_by('ifsc')

class BankDetailSearchView(generics.ListAPIView):
    """ 
    GET /?q=<name>&limit=<limit>&offset=<offset>
    """

    serializer_class = BranchDetailSerializer

    def get_queryset(self):
        query = self.request.GET.get('q')

        if query == None:
            seven_cities = ['PUNE', 'BANGALORE', 'MUMBAI', 'NANDED', 'NASHIK', 'AURANGABAD', 'THANE']
            return Branch.objects.filter(city__in=seven_cities).order_by('ifsc')

        all_fields = Branch._meta.get_fields()
        search_fields = [field.name for field in all_fields]
        q = reduce(operator.or_, [Q(**{'{}__icontains'.format(field): query}) for field in search_fields], Q())
        return Branch.objects.filter(q).order_by('ifsc')

