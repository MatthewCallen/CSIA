#Purpose of views: render html web pages
import random
from django.http import HttpResponse, response


def home_view(request):
    """
    take in a request
    return HTML as a response
    """
    name = "Matthew!" # hard coded
    number = random.randint(10,1233123) #pseudo random(not truly random)

    # from the databse??
    #article_name = 
    #article_content = 


    # Django Templates
    H1_STRING = f"""
    <h1>Hello {name} - {number}</h1>
    """

    P_STRING = f"""
    <p>Hi {name} - {number}</p>
    """

    HTML_STRING = H1_STRING + P_STRING
    return HttpResponse(HTML_STRING)


 