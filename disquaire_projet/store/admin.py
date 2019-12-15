from django.contrib import admin
from django.utils.safestring import mark_safe
from django.urls import reverse
from django.contrib.contenttypes.models import ContentType
from .models import Booking, Contact, Album, Artist


class AdminURLMixin(object):
    def get_admin_url(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        return reverse("admin:store_%s_change" % ( content_type.model), args=(obj.id,))

class BookingInline(admin.TabularInline):
    model = Booking
    readonly_fields = ["created_at", 'album_link', 'contact']
    fields = ["created_at", 'album_link', 'contacted']
    extra = 0
    verbose_name = "Reservation"
    verbose_name_plural = "Reservations"

    def has_add_permission(self, request):
        return False

    def album_link(self, booking):
        path = "admin:store_album_change"
        url = self.get_admin_url(booking.album)
        print("url", url)
        return mark_safe(f"<a href='{url}'>'{booking.album.title}'</a>")
    
    album_link.short_description = "Album"

class AlbumArtistInline(admin.TabularInline):
    model = Album.artists.through
    extra = 1
    verbose_name = "Disque"
    verbose_name_plural = "Disques"



@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    inlines = [BookingInline, ]


@admin.register(Artist)
class ContactArtist(admin.ModelAdmin):
    inlines = [AlbumArtistInline, ]



@admin.register(Album)
class ContactArtist(admin.ModelAdmin):
    search_fields = ["reference", "title" ]
 

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin, AdminURLMixin):
    list_filter = ["created_at", "contacted"]
    fields = ["created_at","contact_link" ,"album_link" , 'contacted']

    readonly_fields = ["created_at","contact_link" ,"album_link" , 'contacted']
    #fieldsets = [ (None, {'fields': ['album', 'contact']})]
    
    
    def has_add_permission(self, request):
        return False

    def contact_link(self, booking):
        url = self.get_admin_url(booking.contact)
        return mark_safe("<a href='{}'>{}</a>".format(url, booking.contact.name))

    def album_link(self, booking):
        path = "admin:store_album_change"
        url = self.get_admin_url(booking.album)
        print("url", url)
        return mark_safe(f"<a href='{url}'>{booking.album.title}</a>")

    contact_link.short_description = "Contact"

    album_link.short_description = "Album"  