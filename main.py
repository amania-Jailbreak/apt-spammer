import json
import os
import subprocess
import sys
import time
import pygame
import keyboard
"""
author:amania
discription: apt spammer
"""

class get_lyric:
    def __init__(self):
        self.lyric = None
        self.lyric_file = "Lyric.json"
        self.musicfile = "Music.mp3"
        with open(self.lyric_file,encoding='UTF-8') as f:
            self.lyric = json.load(f)
        self.music_starttime = self.lyric["StartTime"]
        self.music_endtime = self.lyric["EndTime"]
        self.now_index = 0
    def display_lyrics(self, current_time):
        for content in self.lyric["Content"]:
            if content["Type"] == "Vocal":
                lead = content["Lead"]
                if lead["StartTime"] <= current_time <= lead["EndTime"]:
                    for syllable in lead["Syllables"]:
                        if syllable["StartTime"] <= current_time <= syllable["EndTime"]:
                            index = self.lyric["Content"].index(content)
                            if not index == self.now_index:
                                keyboard.write("\n#")
                            self.now_index = self.lyric["Content"].index(content)
                            if not hasattr(self, 'displayed_texts'):
                                self.displayed_texts = {}
                            if syllable["Text"] not in self.displayed_texts or self.displayed_texts[syllable["Text"]] != syllable["StartTime"]:
                                if syllable["Text"] == "아":
                                    keyboard.write("\na")
                                elif syllable["Text"] == "파트":
                                    keyboard.write("pt")
                                elif syllable["Text"] == "파":
                                    keyboard.write("p")
                                elif syllable["Text"] == "트":
                                    keyboard.write("t\n")
                                else:
                                    keyboard.write(syllable["Text"])
                                self.displayed_texts[syllable["Text"]] = syllable["StartTime"]



    
    def play_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load(self.musicfile)
        pygame.mixer.music.play()
        start_time = time.time()
        while True:
            current_time = time.time() - start_time
            if current_time > self.music_endtime:
                break
            self.display_lyrics(current_time)
            time.sleep(0.1)
        pygame.mixer.music.stop()
        pygame.mixer.quit()

if __name__ == "__main__":
    lyric = get_lyric()
    keyboard.write("clear\n")
    lyric.play_music()