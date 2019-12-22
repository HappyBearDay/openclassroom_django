from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404
from datetime import datetime
from django.template import loader
from .models import MiniUrl
from .forms import MiniUrlForm
import random
import string
# Create your views here.



def generer(nb_caracteres):
    caracteres = string.ascii_letters + string.digits
    aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]
    return ''.join(aleatoire)


def list_url(request):
    template = loader.get_template("miniurl/urls_list.html")
    context = {"urls": MiniUrl.objects.all()}
    return HttpResponse(template.render(context, request=request))



def NewUrl(request):
    form = MiniUrlForm(request.POST or None)
    #print(form)
    print("New url")
    if form.is_valid():
        url = form.cleaned_data["url"]
        auteur = form.cleaned_data["auteur"]
        reduced_url = generer(len(url))
        MiniUrl.objects.create(
            url=url,
            auteur=auteur,
            reduced_url=reduced_url,
            compteur=0)
        print(form.cleaned_data)
        envoi = True
    url_post = "/newmurl/"
    return render(request, 'blog/form.html', locals())


def redirection_url(request, reduced_url):
    print("redirection",reduced_url)
    mini = get_object_or_404(MiniUrl, reduced_url=reduced_url)
    mini.compteur += 1
    mini.save()
    return redirect(mini.url)