from song import Song

class TestSong:
    @classmethod
    def setup_class(cls):
        cls.song_99_problems = Song("99 Problems", "Jay Z", "Rap")
        cls.song_halo = Song("Halo", "Beyonce", "Pop")
        cls.song_smells_like_teen_spirit = Song("Smells Like Teen Spirit", "Nirvana", "Rock")

    def test_saves_name_artist_genre(self):
        '''instantiates with a name, artist, and genre.'''
        out_of_touch = Song("Out of Touch", "Hall and Oates", "Pop")
        assert(out_of_touch.name == "Out of Touch")
        assert(out_of_touch.artist == "Hall and Oates")
        assert(out_of_touch.genre == "Pop")

    def test_has_song_count(self):
        '''counts the total number of Song objects.'''
        assert(Song.count == 4)
        Song("Sara Smile", "Hall and Oates", "Pop")
        assert(Song.count == 5)

    def test_has_genres(self):
        '''keeps track of all Song genres.'''
        assert("Rap" in Song.genre_count)
        assert("Pop" in Song.genre_count)
        assert("Rock" in Song.genre_count)

    def test_has_artists(self):
        '''keeps track of all Song artists.'''
        assert("Jay Z" in Song.artist_count)
        assert("Beyonce" in Song.artist_count)
        assert("Nirvana" in Song.artist_count)
        assert("Hall and Oates" in Song.artist_count)
        
    def test_has_genre_count(self):
        '''keeps count of Songs for each genre.'''
        assert(Song.genre_count["Rap"] == 1)
        assert(Song.genre_count["Pop"] == 3)
        assert(Song.genre_count["Rock"] == 1)

    def test_has_artist_count(self):
        '''keeps count of Songs for each artist.'''
        assert(Song.artist_count["Jay Z"] == 1)
        assert(Song.artist_count["Beyonce"] == 1)
        assert(Song.artist_count["Nirvana"] == 1)
        assert(Song.artist_count["Hall and Oates"] == 2)
