from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome on the main site</h1>")
