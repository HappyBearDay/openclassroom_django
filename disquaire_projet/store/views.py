from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import ALBUMS


def index(request):
    now = datetime.datetime.now()
    html = f"""<html>
                <body>
                It is now {now}.
                </body>
               </html>""" 
    return HttpResponse(html)


def listing(request):
    albums = [f"""<li>{ album['name'] }</li>""" for album in ALBUMS]
    message = """<ul> {} </ul>""".format("\n".join(albums))
    return HttpResponse(message)

def detail(request, album_id):
    id = int(album_id)
    album = ALBUMS[id]
    artists = " ".join([artist["name"] for artist in album["artists"]])

    message ="Le nom de l'album est {}. Il a été écrit par {}".format(album["name"], artists)
    return HttpResponse(message)


def search(request):
    obj = request.GET
    message = ""

    if "query" not in request.GET:
        message = "Aucun requête"
        return HttpResponse("Aucun artiste")
    else:
        query = request.GET["query"]
        
        albums = [
            album for album in ALBUMS
            if query.lower() in " ".join(artist["name"].lower() for artist in album["artists"])
        ]
        
        if len(albums) == 0:
            
            message = "Misère de misère, nous n'avons trouvé aucun résultat !"
        else:
            albums = ["<li>{}</li>".format(album['name']) for album in albums]

            message = """
                Nous avons trouvé les albums correspondant à votre requête ! les voici :
                <ul>
                    {}
                </ul>
            """.format("</li><li>".join(albums))

    return HttpResponse(message)
