from .models import News
from rest_framework import serializers


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('id', 'title', 'pub_date')


class NewsDetailSerializer(serializers.ModelSerializer):
    likes = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = News
        fields = '__all__'

