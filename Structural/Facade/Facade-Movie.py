# Subsystem Classes
class DVDPlayer:
    def on(self):
        print('Turn DVDPlayer on')

    def play(self,movie):
        print(f'Playing {movie} movie')

    def off(self):
        print('Turn DVDPlayer off')


class Projector:
    def on(self):
        print('Turn Projector on')

    def off(self):
        print('Turn Projector off')


class SoundSystem:
    def on(self):
        print('Sound System is on')

    def set_volume(self, level):
        print(f"Sound System volume set to {level}")

    def off(self):
        print('Sound System is off')


# Facade Class
class HomeTheaterFacade:
    def __init__(self, movie: str):
        self.dvd_player = DVDPlayer()
        self.projector = Projector()
        self.sound_system = SoundSystem()
        self.movie = movie

    def watch_movie(self):
        print(f'Be ready to watch {self.movie} movie')
        self.dvd_player.on()
        self.projector.on()
        self.sound_system.on()
        self.sound_system.set_volume(10)
        self.dvd_player.play(self.movie)

    def end_movie(self):
        self.dvd_player.off()
        self.projector.off()
        self.sound_system.off()


# Usage

# Create a Facade
home_theater = HomeTheaterFacade('Inception')
home_theater.watch_movie()
print("\n--- Movie finished ---\n")
home_theater.end_movie()
