from django.conf import settings

def vue_games_cdn(request):
    return {
        'VUE_GAMES_CDN_URL': settings.VUE_GAMES_CDN_URL,
    }