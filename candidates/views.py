from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Candidate, Choice
from .serializers import CandidateSerializer, VotepoolSerializer, DepartmentSerializer, ChoiceSerializer
from rest_framework.decorators import action


class CandidateViewSet(viewsets.ModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

    # @action(['POST'], True)
    # def vote(self, request, pk):

    #     # ticket = Candidate.objects.add()
    #     # ticket.count += 1
    #     # ticket.save()
    #     serializer = CandidateSerializer()
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response('投票成功')
    #     else:
    #         return Response('投票失敗')

    

    
    
    

