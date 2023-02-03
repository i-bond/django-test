from django.shortcuts import render, redirect
from .models import ShortURL
from django.shortcuts import get_object_or_404
from django.conf import settings
import redis


r = redis.Redis(host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                db=settings.REDIS_DB)


def short_url_home(request):
    objects_list = ShortURL.objects.all()

    # Creating a dict of cached values stored in Redis
    short_url_lst = ShortURL.objects.values_list('short_url', flat=True)
    cached_views = r.mget(list(short_url_lst))
    cached_views_lst = [0 if val is None else val.decode() for val in cached_views]

    return render(request, "shortener/shorturl_list.html", {'shorturl_list': zip(objects_list, cached_views_lst)})


def redirect_to_website(request, token):

    website = get_object_or_404(ShortURL, short_url=token)
    website.times_followed += 1
    website.save()
    cached_times_followed = r.incr(f'{website.short_url}')

    return redirect(website.original_url)
