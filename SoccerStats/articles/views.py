from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .forms import ArticleForm
from .models import Article
# Create your views here.
#Purpose of views: render html web pages
import random
from django.http import HttpResponse, response
from django.template.loader import render_to_string 
global secondRand

def home_view(request, id=None, *args, **kwargs):
    """
    take in a request
    return HTML as a response
    """
    name = "Matthew!" # hard coded
    random_id = random.randint(5,7)
    #random_id = random.randint(1, ) #pseudo random(not truly random)

    # from the database??
    #article_obj = Article.objects.get(id=random_id)
    #article_obj = Article.objects.get(id = random_id)
    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()

    #article_name = 
    #article_content = 

    context = {
        "object_list": article_queryset,
        "object": article_obj, 
        "title": article_obj.title,
        #"id": article_obj.id,
        "content": article_obj.content

    }
    # Django Templates
    HTML_STRING = render_to_string("home-view.html", context=context)
    #HTML_STRING = """
    #<h1>{title} (id: {id})</h1>
    #<p>{content}</p>
    #""".format(**context)
    return HttpResponse(HTML_STRING)


 
def article_search_view(request):
    #print(dir(request))
    #print(request.GET)
    query_dict = request.GET #this is a dictionary
    #query = query_dict.get("q") #<input type='text' name='q' />

    try: 
        query = int(query_dict.get("q"))
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id=query)
    context = {"object": article_obj}
    return render(request, "articles/search.html", context=context)

@login_required
def article_create_view(request):
    #print(request.POST)
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
        # context['object'] = article_object
        # context['created'] = True
    return render(request, "articles/create.html", context = context)
# def article_create_view(request):
#     #print(request.POST)
#     form = ArticleForm()
#     context = {
#         "form": form
#     }
#     if request.method == "POST":
#         form = ArticleForm(request.POST)
#         context['form'] = form
#         if form.is_valid():
#             title = form.cleaned_data.get("title")
#             content = form.cleaned_data.get("content")
#             article_object = Article.objects.create(title=title, content=content)
#             context['object'] = article_object
#             context['created'] = True
#     return render(request, "articles/create.html", context = context)


def article_detail_view(request, id=None):
    article_obj = None
    if id is not None:
        article_obj = Article.objects.get(id = id)
    context = {
        "object": article_obj,
    }

    return render(request, "articles/details.html", context = context)

def table_view(request):
    #Get all teams in database 
    # all_teams = Teams.objects.get()

    #context = {"teams": all_teams}

    return render(request, "premtable.html") #add additional context parameter