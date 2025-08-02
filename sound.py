import os
# IMPORT PYGAME AND ITS MODULES
import pygame
from pygame.mixer import Sound

# INITIALISE THE PYGAME AND MIXER MODULE
pygame.mixer.init()

# MANAGES ALL SOUND RELATED FEATURES
class SoundEffects:

    # STATIC METHOD TO LOAD FILE
    @staticmethod
    def load_sound(path):
        if not os.path.exists(path):
            print(f"[ERROR] Sound file not found: {path}")
            return None
        try:
            return Sound(path)
        except pygame.error as e:
            print(f"[ERROR] Failed to load sound {path}: {e}")
            return None

    def __init__(self):
        self.collision = self.load_sound("./assets/sounds/collision_with_paddle.wav")
        self.score = self.load_sound("./assets/sounds/score.wav")
        self.music_file = "./assets/sounds/background_music.wav"
        self.background_music()

    # PLAY COLLISION SOUND EFFECT
    def play_collision(self):
        if self.collision:
            self.collision.play()

    # PLAY SCORE SOUND EFFECT
    def score_effect(self):
        if self.score:
            self.score.play()

    # PLAY BACKGROUND MUSIC
    def background_music(self):
        if not os.path.exists(self.music_file):
            print(f"[ERROR] Background music file not found: {self.music_file}")
            return
        try:
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.set_volume(0.1)
            pygame.mixer.music.play(-1)
        except pygame.error as e:
            print(f"[ERROR] Failed to play background music: {e}")





