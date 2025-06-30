from django.http import HttpResponsePermanentRedirect

class WwwRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        host = request.get_host()
        if host == 'play2learn.app':
            new_url = 'https://www.play2learn.app' + request.get_full_path()
            return HttpResponsePermanentRedirect(new_url)
        return self.get_response(request)

# helps redirect with the middleware