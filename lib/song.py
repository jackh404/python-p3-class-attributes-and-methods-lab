class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}
    
    def __init__(self,name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)

    @classmethod
    def add_song_to_count(cls):
        cls.count += 1
    @classmethod
    def add_to_genres(cls,genre):
        if genre not in Song.genres:
            Song.genres.append(genre)
    @classmethod
    def add_to_artists(cls,artist):
        if artist not in Song.artists:
            Song.artists.append(artist)
    @classmethod
    def add_to_genre_count(cls,genre):
        if genre not in Song.genre_count.keys():
            Song.genre_count[genre] = 1
        else:
            Song.genre_count[genre] += 1
    @classmethod
    def add_to_artist_count(cls,artist):
        if artist not in Song.artist_count.keys():
            Song.artist_count[artist] = 1
        else:
            Song.artist_count[artist] += 1