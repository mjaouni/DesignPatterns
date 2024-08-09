class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def __str__(self):
        return f"'{self.title}' by {self.artist}"


class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, Song):
        self.songs.append(Song)

    def __iter__(self):
        return PlaylistIterator(self.songs)

    def reverse_iterator(self):
        return ReversePlaylistIterator(self.songs)


class PlaylistIterator:
    def __init__(self, songs):
        self._songs = songs
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._songs):
            song = self._songs[self._index]
            self._index += 1
            return song
        else:
            raise StopIteration


class ReversePlaylistIterator:
    def __init__(self, songs):
        self._songs = songs
        self._index = len(songs) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= 0:
            song = self._songs[self._index]
            self._index -= 1
            return song
        else:
            raise StopIteration


# Usage
# Create a Playlist
playlist = Playlist()
playlist.add_song(Song("Tala'al Badru Alayna", "Meshari El Afasi"))
playlist.add_song(Song("Ya Nabi Salam Alayka", "Maher Zain"))
playlist.add_song(Song("Hasbi Rabbi", "Sami Yusuf"))

# Iterate over the playlist using a for loop
for song in playlist:
    print(song)

print()
print('***Now we will iterate the playlist in reverse order*** ')
print()
# Iterate over the playlist in reverse using the reverse iterator
for song in playlist.reverse_iterator():
    print(song)
