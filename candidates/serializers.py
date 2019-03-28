from rest_framework import serializers

from .models import Candidate, Votepool, Department, Choice

class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = '__all__'


class VotepoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Votepool
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['vote_to', 'email', 'create_at', 'is_valid',]