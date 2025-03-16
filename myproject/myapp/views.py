from django.http import HttpResponse

def hello(request):
    return HttpResponse('Hello World')
def homepage(request):
    return HttpResponse('Welcome to Little Lemon')
from datetime import datetime

def display_date(request):
    date_joined = datetime.now().year
    return HttpResponse(f'This year is {date_joined}')
def menu(request):
    html_code = """
    <html>
    <head>
        <style>
            body { color: green; }
            h1 { color: blue; }
        </style>
    </head>
    <body>
        <h1>Menu</h1>
        <p>Welcome to the menu page!</p>
    </body>
    </html>
    """
    return HttpResponse(html_code)
