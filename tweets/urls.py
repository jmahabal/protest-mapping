from django.conf.urls import url
from tweets.views import TweetList
from . import views
from tweets.views import AboutView, TweetsJSON, MapView

urlpatterns = [
	#url(r'^tweets/$', TweetList.as_view()),
	#url(r'^tweets/$', AboutView.as_view()),
	url(r'^api/tweets.json/$', TweetsJSON.as_view(), name='tweets'),
    url(r'^$', MapView.as_view(), name='index'),
]