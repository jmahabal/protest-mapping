from django.shortcuts import render
from django.views.generic import ListView
from tweets.models import Tweet
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView

from twitter_stream.models import Tweet

class AboutView(TemplateView):
    template_name = "tweet_list.html"
# Create your views here.

class TweetList(ListView):
    model = Tweet

class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_to_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context

class TweetsJSON(TemplateView, JSONResponseMixin):
	def get_data(self, context):
		tweets = []
		for tweet in Tweet.objects.exclude(latitude=None):
			attributes = {}
			attributes['lat'] = tweet.latitude
			attributes['lon'] = tweet.longitude
			attributes['text'] = tweet.text
			attributes['tweetid'] = tweet.tweet_id
			tweets.append(attributes)
		data = {}
		data['tweets'] = tweets
		return data

	def render_to_response(self, context, **response_kwargs):
		return self.render_to_json_response(context, **response_kwargs)

class MapView(TemplateView):
	template_name = 'map.html'

def index(request):
    return HttpResponse(model.tweettest)