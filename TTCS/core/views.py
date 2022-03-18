import sys

from django.shortcuts import render

class Web:
    def index (request):
        return render(request, "index.html")

def handler505(request):
    type_, value, traceback = sys.exc_info()
    data: dict = dict(value=value)
    return render(request, "error.html", data)