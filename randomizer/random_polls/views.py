from django.http import HttpResponse

def index(_):
    return HttpResponse("Hello, world. You're at the random polls index.")
