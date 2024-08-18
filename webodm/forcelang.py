from django.utils import translation

class ForceDefaultLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Forzar el idioma a español
        user_language = 'es'
        translation.activate(user_language)
        response = self.get_response(request)
        response.set_cookie('django_language', user_language)
        return response
