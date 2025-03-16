from django.http import HttpResponse

def home(request):
    # Accessing request.path
    path = request.path
    
    # Creating the HttpResponse object with path data
    response = HttpResponse(path, content_type="text/plain; charset=utf-8")
    return response
