from django.utils.deprecation import MiddlewareMixin
from django.db.models import F
from .models import RequestCounter

class RequestCountMiddleware(MiddlewareMixin):
    def process_view(self, request, *args, **kwargs):
        RequestCounter.objects.update(count=F('count') + 1)
        return None
