# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 18:01:22 2018

@author: 凯风
"""

class HomeTheaterFacade(object):
    def __init__(self, amplifier, tuner, dvdPlayer, cdPlayer, projector, screen, lights, popper):
        self.amplifier = amplifier
        self.tuner = tuner
        self.dvdPlayer = dvdPlayer
        self.cdPlayer = cdPlayer
        self.projector = projector
        self.screen = screen
        self.lights = lights
        self.popper = popper
    
    def watchMovie(self, movie):
        print("Get ready to watch a movie...")
        self.popper.on()
        self.popper.pop()
        self.lights.dim(10)
        self.screen.down()
        self.projector.on()
        self.projector.wideScreenMode()
        self.amplifier.on()
        self.amplifier.setDvd(self.dvdPlayer)
        self.amplifier.setSurroundSound()
        self.amplifier.setVolume(15)
        self.dvdPlayer.on()
        self.dvdPlayer.play(movie = movie)
    
    def endMovie(self):
        print("Shutting movie theater down...")
        self.popper.off()
        self.lights.on()
        self.screen.up()
        self.projector.off()
        self.amplifier.off()
        self.dvdPlayer.stop()
        self.dvdPlayer.eject()
        self.dvdPlayer.off()
    
    def listenToCd(self, cdTitle):
        print("Get ready for an audiopile experence...")
        self.lights.on()
        self.amplifier.on()
        self.amplifier.setVolume(5)
        self.amplifier.setCd(self.cdPlayer)
        self.amplifier.setStereoSound()
        self.cdPlayer.on()
        self.cdPlayer.play(title = cdTitle)
    
    def endCd(self):
        print("Shutting down CD...")
        self.amplifier.off()
        self.amplifier.setCd(self.cdPlayer)
        self.cdPlayer.eject()
        self.cdPlayer.off()
    
    def listenToRadio(self, frequency):
        print("Tuning in the airwaves...")
        self.tuner.on()
        self.tuner.setFrequency(frequency)
        self.amplifier.on()
        self.amplifier.setVolume(7)
        self.amplifier.setTuner(self.tuner)
    
    def endRadio(self):
        print("Shutting down the tuner...")
        self.tuner.off()
        self.amplifier.off()
                        
    