import sqlite3

from django.db.models import F
from .models import Viewer


class ViewersMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        conn = sqlite3.connect('db.sqlite3')
        c = conn.cursor()

    def viewer_count(self):

        # # get the count of tables with the name
        # self.c.execute(
        #     ''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='students' ''')

        # # if the count is 1, then table exists
        # if self.c.fetchone()[0] == 1:

        #     print('Table exists.'),
        #     Viewer.objects.update(count=F('count') + 1)

        # commit the changes to db
        self.conn.commit()
        # close the connection
        self.conn.close()

    def __call__(self, request):
        if request.path == "/":
            self.viewer_count()
        response = self.get_response(request)

        return response
