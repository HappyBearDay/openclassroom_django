from django.shortcuts import render
from django.http import HttpResponse
import datetime
from .models import Album, Artist, Contact, Booking
from django.db.models import Q


def create_artist( artist_names ):
    for i in artist_names:
        Artist.objects.create(name = i)

def create_album( albums_list ):
    for curr_album_dict in albums_list:

        curr_album = Album.objects.create( title = curr_album_dict["title"])
        list_artists = [ Artist.objects.filter(name = curr_artist_name)[0]  for curr_artist_name in curr_album_dict["artists"]]
        curr_album.artists.add(*list_artists)
        curr_album.save()


def init_db(request):
    Album.objects.all().delete()
    Artist.objects.all().delete()
    Contact.objects.all().delete()
    Booking.objects.all().delete()
    ARTISTS = ['Francis Cabrel', 'Elijay', 'Rosana', 'María Dolores Pradera']

    ALBUMS = [
        {'title': 'Sarbacane', 'artists': ['Francis Cabrel']},
        {'title': 'La Dalle', 'artists': ['Elijay']},
        {'title': 'Luna Nueva', 'artists': ['Rosana', 'María Dolores Pradera']}
    ]

    create_artist( ARTISTS )
    create_album( ALBUMS )
    return HttpResponse("Ok")

def index(request):

    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    now = datetime.datetime.now()
    
    formatted_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(formatted_albums))
    message += f"\n{now}"
    
    return HttpResponse(message)

def listing(request):
    ALBUMS = Album.objects.filter(available=True)
    albums = [f"""<li>{ album['name'] }</li>""" for album in ALBUMS]
    message = """<ul> {} </ul>""".format("\n".join(albums))
    return HttpResponse(message)

def detail(request, album_id):
    
    album = Album.objects.get(pk = album_id)

    artists = ", ".join([curr_artist.name for curr_artist in album.artists.all()] )

    message ="Le nom de l'album est {}. Il a été écrit par {}".format(album.title, artists)
    return HttpResponse(message)


def search(request):
    obj = request.GET
    message = ""

    if "query" not in request.GET:
        message = "Aucun requête"
        return HttpResponse(message)
    else:
        query = request.GET["query"]
        
        albums = Album.objects.filter(Q(title__icontains = query) | Q(artists__name__icontains = query)).distinct()
        
        if len(albums) == 0:
            
            message = "Misère de misère, nous n'avons trouvé aucun résultat !"
        else:
            albums = ["<li>{}</li>".format(album) for album in albums]

            message = """
                Nous avons trouvé les albums correspondant à votre requête ! les voici :
                <ul>
                    {}
                </ul>
            """.format("</li><li>".join(albums))

    return HttpResponse(message)
