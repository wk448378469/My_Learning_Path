# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 17:01:53 2018

@author: 凯风
"""

class electric(object):
    
    def on(self):
        print(self.desc + " on")
        
    def off(self):
        print(self.desc + " off")
    
    def __str__(self):
        return self.desc


class Amplifier(electric):
    def __init__(self, desc):
        self.desc = desc
    
    def setStereoSound(self):
        print(self.desc + " stereo mode on")
    
    def setSurroundSound(self):
        print(self.desc + " surround sound on (5 speakers, 1 subwoofer)")
    
    def setVolume(self, level):
        print(self.desc + " setting volume to " + str(level))
    
    def setTuner(self, tuner):
        print(self.desc + " setting tuner to " + str(tuner))
        self.tuner = tuner
    
    def setDvd(self, dvd):
        print(self.desc + " setting dvd player to " + str(dvd))
        self.dvd = dvd
    
    def setCd(self, cd):
        print(self.desc + " setting cd player to " + str(cd))
        self.cd = cd


class CdPlayer(electric):
    def __init__(self, desc, amplifier):
        self.desc = desc
        self.amplifier = amplifier
    
    def eject(self):
        self.title = None
        print(self.desc + " eject")
    
    def play(self, **kw):
        if "title" in kw:
            self.title = kw["title"]
            self.currentTrack = 0
            print(self.desc + " playing \"" + self.title + "\"")
        elif "track" in kw:
            if self.title == None:
                print(self.desc + " can't play track " + self.currentTrack + ", no cd inserted")
            else:
                self.currentTrack = kw["track"]
                print(self.desc + " playing track " + self.currentTrack)
        else:
            print("error!!!")


    def stop(self):
        self.currentTrack = 0
        print(self.desc + " stopped")
    
    def pause(self):
        print(self.desc + " paused \"" + self.title + "\"")
    

class DvdPlayer(electric):
    def __init__(self, desc, amplifier):
        self.desc = desc
        self.amplifier = amplifier
    
    def eject(self):
        self.movie = None
        print(self.desc + " eject")
    
    def play(self, **kw):
        if "movie" in kw:
            self.movie = kw["movie"]
            self.currentTrack = 0
            print(self.desc + " playing \"" + kw["movie"] + "\"")
        elif "track" in kw:
            if self.movie == None:
                print(self.desc + " can't play track " + kw["track"] + " no dvd inserted")
            else:
                self.currentTrack = kw["track"]
                print(self.desc + " playing track " + self.currentTrack + " of \"" + self.movie + "\"")
        else:
            print("error")
    
    def stop(self):
        self.currentTrack = 0
        print(self.desc + " stopped \"" + self.movie + "\"")
    
    def pause(self):
        print(self.desc + " paused \"" + self.movie + "\"")
    
    def setTwoChannelAudio(self):
        print(self.desc + " set two channel audio")
    
    def setSurroundAudio(self):
        print(self.desc + " set surround audio")


class PopcornPopper(electric):
    def __init__(self, desc):
        self.desc = desc
    
    def pop(self):
        print(self.desc + " popping popcorn!")
    

class Projector(electric):
    def __init__(self, desc, dvdPlayer):
        self.desc = desc
        self.dvdPlayer = dvdPlayer
    
    def wideScreenMode(self):
        print(self.desc + " in widescreen mode (16*9 aspect ratio)")
    
    def tvMode(self):
        print(self.desc + " in tv mode (4*3 aspect ratio)")


class Screen(electric):
    def __init__(self, desc):
        self.desc = desc
    
    def up(self):
        print(self.desc + " going up")
    
    def down(self):
        print(self.desc + " going down")
    

class TheaterLights(electric):
    def __init__(self, desc):
        self.desc = desc
    
    def dim(self, level):
        print(self.desc + " dimming to " + str(level) + "%")


class Tuner(electric):
    def __init__(self, desc, amplifier):
        self.desc = desc
        self.amplifier = amplifier
    
    def setFrequency(self, frequency):
        self.frequency = frequency
        print(self.desc + " setting frequency to " + str(frequency))
    
    def setAm(self):
        print(self.desc + " setting AM mode")
    
    def setFm(self):
        print(self.desc + " setting FM mode")
    
            








































