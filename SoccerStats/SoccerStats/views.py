#Purpose of views: render html web pages
from django.http import HttpResponse, response

HTML_STRING = """
<h1>Hello World this is matthew</h1>
"""

def home_view(request):
    """
    take in a request
    return HTML as a response
    """
    print(100*1000)
    return HttpResponse(HTML_STRING)


