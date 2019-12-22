from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404
from datetime import datetime
from django.template import loader
from .models import Article, Categorie, Member
from .forms import  ContactForm, ArticleForm, MemberForm

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid(): 
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']
        envoi = True
    url_post = "/blog/contact/"
    return render(request, 'blog/form.html', locals())

def voir_members(request):
    return render(
        request, 
        'blog/members.html', 
        {'members': Member.objects.all()}
    )

def NewMember(request):
    form = MemberForm(request.POST or None, request.FILES)
    #print(form)
    print("New Member")
    if form.is_valid():
        form.save()
        print(form.cleaned_data)
        envoi = True
    url_post = "/blog/newmember/"
    return render(request, 'blog/form.html', locals())


def article_form(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid(): 
        form.save()
        envoi = True
    url_post = "/blog/articleform/"
    return render(request, 'blog/form.html', locals())



def db_init(request):
    categorie_a = Categorie(nom="Categorie A")
    categorie_b = Categorie(nom="Categorie B")
    categorie_c = Categorie(nom="Categorie C")
    categorie_a.save()
    categorie_b.save()
    categorie_c.save()
    article_01 = Article(titre = "Titre 01", auteur="Auteur 01", categorie = categorie_a, contenu="""Sed ut perspiciatis unde omnis iste natus error sit""")  
    article_02 = Article(titre = "Titre 02", auteur="Auteur 02", categorie = categorie_a, contenu="""At vero eos et accusamus et iusto odio dignissimos ducimus qui blanditiis praesentium""")  
    article_03 = Article(titre = "Titre 03", auteur="Auteur 02", categorie = categorie_b, contenu="""Lorem ipsum dolor sit amet, consectetur adipiscing elit.""")  
    article_01.save()
    article_02.save()
    article_03.save()
    return HttpResponse("ok!")


def date_actuelle(request):
    template = loader.get_template("blog/date.html")
    context = {'date': datetime.now()}
    return HttpResponse(template.render(context, request=request))


def addition(request, nombre1, nombre2):    
    total = nombre1 + nombre2
    template = loader.get_template("blog/addition.html")
    context = {'total': total, "nombre1" : nombre1, "nombre2" : nombre2}
    return HttpResponse(template.render(context, request=request))

def about(request):
    template = loader.get_template("blog/about.html")
    return HttpResponse(template.render())


def home(request):
    template = loader.get_template("blog/home.html")
    return HttpResponse(template.render())


def view_article(request, article_id):
    article = get_object_or_404(Article, id =article_id  )
    print("aaaaa")
    template = loader.get_template("blog/detail.html")
    context = {"article" : article}
    return HttpResponse(template.render(context, request=request))



def list_articles(request, year, month=1):
    """ Liste des articles d'un mois précis. """
    return HttpResponse(
        "Vous avez demandé les articles de {0} {1}.".format(month, year)  
    )