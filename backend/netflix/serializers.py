from rest_framework import serializers
from .models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = [
            'id',
            'show_id',
            'country'
        ]

class FormSerializer(serializers.ModelSerializer):
    class Meta:
        model = Form
        fields = [
            'id',
            'show_id',
            'title',
            'type',
            'cast',
            'director',
            'country',
            'rating',
            'duration',
            'release_year',
            'catalog',
            'average_score',
            'score_count',
            'comments',
        ]

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = [
            'id',
            'show_id',
            'comment',
        ]

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = [
            'id',
            'show_id',
            'cast',
        ]

class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ranking
        fields = [
            'show_id',
            'title',
            'average_score',
        ]
