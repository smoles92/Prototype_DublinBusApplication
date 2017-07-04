from django.db import models

# PK as each album added to DB has unique ID number
class Album(models.Model):
    # Column 1
    artist = models.CharField(max_length=250) # Variable name "artist" will be column name in database 
    # Column 2
    album_title = models.CharField(max_length=500) # Album name will also just be characters
    # Column 3
    genre = models.CharField(max_length=100)
    #Column 4
    album_logo = models.CharField(max_length=1000)
    
    def __str__(self): # Built-in string representation of this object (Album)
        return self.album_title + " - " + self.artist
    
class Song(models.Model):
    # FK as a song is part of an album, Cascade as if album gone/deleted, songs linked are gone deleted too
    album = models.ForeignKey(Album, on_delete=models.CASCADE) 
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False) # When True, song is a favorite of user
    
    def __str__(self): # Built-in string representation of this object (Song)
        return self.song_title # Whenever need to represent a song, print/return song title
    