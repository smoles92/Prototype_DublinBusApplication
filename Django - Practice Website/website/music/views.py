from django.shortcuts import render, get_object_or_404
from .models import Album, Song # Import Album class and Song class (Tut 24)

def index(request):
    all_albums = Album.objects.all() # Connects to DB, look at albums table and get all objects (albums)
    context = {'all_albums' : all_albums} # Information that your template needs
    
    return render (request, 'music/index.html', context) # Passing this information into the template (Tutorial 15 edit)

    

def detail(request, album_id): # Album_id variable: represents 71 in this case
    album = get_object_or_404(Album, pk=album_id) # Replaces but implements try/except 
    
    # Changed context to album, as only used once (Better style). Passing album information
    return render (request, 'music/detail.html', {'album' : album}) 
  
    
def favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id) # Replaces but implements try/except
    try:
        selected_song = album.song_set.get(pk=request.POST['song']) # Get the value of whatever song was posted/selected
    except(KeyError, Song.DoesNotExist): # Error message
        return render (request, 'music/detail.html', {
            'album' : album,
            'error message' : "You did not select a valid song",
        }) # Sends them back to the details page with information in {}
    else:
        selected_song.is_favorite = True # Changes the attribute
        selected_song.save() # Save the change explicitly to the Database
        return render(request, 'music/detail.html', {'album' : album})
 
    
    