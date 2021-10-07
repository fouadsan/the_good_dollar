import sqlite3

from django.db.models import F
from .models import Viewer


class ViewersMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def viewer_count(self):
        Viewer.objects.update(count=F('count') + 1)

    def __call__(self, request):
        if request.path == "/":
            self.viewer_count()
        response = self.get_response(request)

        return response
