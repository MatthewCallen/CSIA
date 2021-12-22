# #Purpose of views: render html web pages
# import random
# from django.http import HttpResponse, response
# from django.template.loader import render_to_string 
# from articles.models import Article




# def home_view(request, id=None, *args, **kwargs):
#     """
#     take in a request
#     return HTML as a response
#     """
#     name = "Matthew!" # hard coded
#     random_id = random.randint(1, 4) #pseudo random(not truly random)

#     # from the database??
#     article_obj = Article.objects.get(id=random_id)
#     article_queryset = Article.objects.all()

#     #article_name = 
#     #article_content = 

#     context = {
#         "object_list": article_queryset,
#         "object": article_obj, 
#         "title": article_obj.title,
#         "id": article_obj.id,
#         "content": article_obj.content

#     }
#     # Django Templates
#     HTML_STRING = render_to_string("home-view.html", context=context)
#     #HTML_STRING = """
#     #<h1>{title} (id: {id})</h1>
#     #<p>{content}</p>
#     #""".format(**context)
#     return HttpResponse(HTML_STRING)


 