from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# View to handle GET requests
def get_view(request):
    return HttpResponse("This is a GET request response", content_type="text/plain")

# View to handle POST requests
@csrf_exempt  # Disable CSRF verification for simplicity (not recommended for production)
def post_view(request):
    if request.method == 'POST':
        # Assuming the client sends JSON data
        data = json.loads(request.body)
        return HttpResponse(f"Received POST data: {data}", content_type="text/plain")
    return HttpResponse("This is a POST request response", content_type="text/plain")

# View to handle PUT requests
@csrf_exempt
def put_view(request):
    if request.method == 'PUT':
        # Assuming the client sends JSON data
        data = json.loads(request.body)
        return HttpResponse(f"Received PUT data: {data}", content_type="text/plain")
    return HttpResponse("This is a PUT request response", content_type="text/plain")

# View to handle DELETE requests
@csrf_exempt
def delete_view(request):
    if request.method == 'DELETE':
        # Logic for handling DELETE (you could look for a resource to delete)
        return HttpResponse("DELETE request received and handled", content_type="text/plain")
    return HttpResponse("This is a DELETE request response", content_type="text/plain")
