from rest_framework import serializers
from .models import Branch


class BranchDetailSerializer(serializers.ModelSerializer):

    class Meta:
        name = 'branches'
        model = Branch
        fields = '__all__'
