from django.shortcuts import render, redirect
from django.template import loader
from django.template import loader
from django.db.models import Sum,Count,Avg,Max
import logging
from django.http import HttpResponse, JsonResponse

from rest_framework.generics import GenericAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import *
from .models import *
from .filter import *
# Create your views here.

@api_view(['GET', 'POST', 'DELETE', 'PATCH'])
def AllCountry(request):
    if request.method=='GET':
        queryset = Country.objects.all()
        serializer = CountrySerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = CountrySerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        x=Country.objects.all()
        for t in x:
            t.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST', 'DELETE', 'PATCH'])   
def OneCountry(request, show_id):
    if request.method=='GET':
        queryset = Country.objects.get(show_id=show_id)
        serializer = CountrySerializer(queryset, many=False)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        x=Country.objects.get(show_id=show_id)
        x.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method=="PATCH":
        x=Country.objects.get(show_id=show_id)
        print(x)
        serializer = CountrySerializer(x, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE', 'PATCH'])
def AllForm(request):
    if request.method=='GET':   
        queryset = Form.objects.all()
        serializer = FormSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = FormSerializer(data=request.data)
        print(request.data.get('director'))
        if serializer.is_valid():
            x=Country(show_id=request.data.get('show_id'), country=request.data.get('country'))
            x.save()
            x=Data(show_id=request.data.get('show_id'), type=request.data.get('type'), release_year=request.data.get('release_year'), rating=request.data.get('rating'))
            x.save()
            x=Director(show_id=request.data.get('show_id'), director=request.data.get('director'))
            x.save()
            x=Listed(show_id=request.data.get('show_id'), catalog=request.data.get('catalog'))
            x.save()
            x=Netflix(show_id=request.data.get('show_id'), type=request.data.get('type'), title=request.data.get('title'), director=request.data.get('director'), duration=request.data.get('duration'))
            x.save()
            x=Ranking(show_id=request.data.get('show_id'), title=request.data.get('title'), average_score=0)
            x.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        x=Form.objects.all()
        for i in x:
            i.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
  
@api_view(['GET', 'POST', 'DELETE', 'PATCH'])
def OneForm(request, show_id):
    if request.method=='GET':   
        queryset = Form.objects.get(show_id=show_id)
        serializer = FormSerializer(queryset)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = FormSerializer(data=request.data)
        print(request.data.get('director'))
        if serializer.is_valid():
            x=Country(show_id=request.data.get('show_id'), country=request.data.get('country'))
            x.save()
            x=Data(show_id=request.data.get('show_id'), type=request.data.get('type'), release_year=request.data.get('release_year'), rating=request.data.get('rating'))
            x.save()
            x=Director(show_id=request.data.get('show_id'), director=request.data.get('director'))
            x.save()
            x=Listed(show_id=request.data.get('show_id'), catalog=request.data.get('catalog'))
            x.save()
            x=Netflix(show_id=request.data.get('show_id'), type=request.data.get('type'), title=request.data.get('title'), director=request.data.get('director'), duration=request.data.get('duration'))
            x.save()
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="PATCH":
        x=Form.objects.get(show_id=show_id)
        serializer = FormSerializer(x, data=request.data, partial=True)
        print(x.show_id)
        print(x.country)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            x=Form.objects.get(show_id=show_id)
            print(x.show_id)
            print(x.country)
            return Response(serializer.data, status=status.HTTP_206_PARTIAL_CONTENT)
        else:
            # print("error")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        x=Form.objects.get(show_id=show_id)
        x.delete()
        x=Ranking.objects.get(show_id=show_id)
        x.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET', 'POST', 'DELETE', 'PATCH'])
def AllCast(request):
    if request.method=='GET':
        queryset = Cast.objects.all()
        serializer = CastSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = CastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        x=Cast.objects.all()
        for t in x:
            t.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
@api_view(['GET', 'POST', 'DELETE', 'PATCH'])   
def OneCast(request,id):
    if request.method=='GET':
        queryset = Cast.objects.get(id=id)
        serializer = CastSerializer(queryset, many=False)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = CastSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        x=Cast.objects.get(id=id)
        x.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method=="PATCH":
        x=Cast.objects.get(id=id)
        serializer = CastSerializer(x, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE', 'PATCH'])
def AllComment(request ,show_id):
    if request.method=='GET':
        queryset = Comment.objects.filter(show_id=show_id)
        serializer = CommentSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        x=Comment.objects.all()
        for t in x:
            t.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['GET', 'POST', 'DELETE', 'PATCH'])
def OneComment(request, show_id):
    if request.method=='GET':
        queryset = Comment.objects.get(show_id=show_id)
        serializer = CommentSerializer(queryset, many=False)
        return Response(serializer.data)
    elif request.method=='POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        x=Comment.objects.get(show_id=show_id)
        x.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method=="PATCH":
        x=Comment.objects.get(show_id=show_id)

        serializer = CommentSerializer(x, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PATCH'])
def AllFormFilter(request, show_id):
    if request.method=='GET':   
        queryset = Form.objects.filter(show_id=show_id)
        serializer = FormSerializer(queryset, many=True)
        return Response(serializer.data)
    elif request.method=='PATCH':
        queryset = Form.objects.filter(show_id=show_id)
        print(request)
        tt=Ranking.objects.get(show_id=show_id)
        for x in queryset:
            x.average_score=x.average_score*x.score_count+request.data['star']
            x.score_count=x.score_count+1
            x.average_score=x.average_score/x.score_count
            tt.average_score=x.average_score
            x.save()
        tt.save()
        serializer = RankSerializer(tt)
        return Response(serializer.data)

@api_view(['GET'])
def AllRanking(request):
    if request.method=='GET':   
        queryset = Ranking.objects.all().order_by('-average_score')[:10]
        #queryset = Form.objects.all()
        #print(queryset)
        print(queryset)
        serializer = RankSerializer(queryset, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def Filter(request):
    if request.method=='GET':
        # print(request)
        # print(request.GET.get('release_yearStart'))
        # print(request.GET.get('release_yearEnd'))
        
        queryset=Form.objects.all()
        
        if request.GET.get('title')!='':
            queryset = queryset.filter(title=request.GET.get('title'))
        # print(queryset)
        if request.GET.get('country')!='':
            queryset =queryset.filter(country=request.GET.get('country'))
        if request.GET.get('rating')!='':
            queryset =queryset.filter(rating=request.GET.get('rating'))
        if request.GET.get('director')!='':
            queryset =queryset.filter(director=request.GET.get('director'))
        if request.GET.get('cast')!='':
            queryset =queryset.filter(cast=request.GET.get('cast'))
        # print(queryset)
        if request.GET.get('catalog')!='':
            queryset =queryset.filter(catalog=request.GET.get('catalog'))
        # print(queryset)

        
        if request.GET.get('release_yearStart')!="0" and request.GET.get('release_yearEnd')!="0":
            queryset =queryset.filter(release_year__range=((int)(request.GET.get('release_yearStart')),(int)(request.GET.get('release_yearEnd'))))
        # print(queryset)
        if request.GET.get('score_countStart')!="0" and request.GET.get('score_countEnd')!="0":
            queryset =queryset.filter(score_count__range=((int)(request.GET.get('score_countStart')),(int)(request.GET.get('score_countEnd'))))
        # print(queryset)
        if request.GET.get('status')!='...' and request.GET.get('status')!="" :
            if request.GET.get('status')=='descending':
                queryset =queryset.order_by('-average_score')
                print('here')
            else:
                queryset =queryset.order_by('average_score')
                print(request.GET.get('status'))
        # print(queryset)
        serializer = FormSerializer(queryset, many=True)
        return Response(serializer.data)
            