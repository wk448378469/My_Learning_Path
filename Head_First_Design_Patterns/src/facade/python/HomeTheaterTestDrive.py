# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 18:10:48 2018

@author: 凯风
"""

from sub import Amplifier,Tuner,DvdPlayer,CdPlayer,PopcornPopper,TheaterLights,Screen,Projector
from HomeTheaterFacade import HomeTheaterFacade

if __name__ == "__main__":
    amplifier = Amplifier("Top-O-Line Amplifier")
    tuner = Tuner("Top-O-Line AM/FM Tuner", amplifier)
    dvdPlayer = DvdPlayer("Top-O-Line DVD Player", amplifier)
    cdPlayer = CdPlayer("Top-O-Line CD Player", amplifier)
    projector = Projector("Top-O-Line Projector", dvdPlayer)
    lights = TheaterLights("Theater Ceiling Lights")
    screen = Screen("Theater Screen")
    popper = PopcornPopper("Popcorn Popper")
    
    homeTheaterFacade = HomeTheaterFacade(amplifier, tuner, dvdPlayer, cdPlayer, projector, screen, lights, popper)
    
    homeTheaterFacade.watchMovie("F***************k")
    homeTheaterFacade.endMovie()
    
    print("\n")
                              
    homeTheaterFacade.listenToCd("Kamikaze")
    homeTheaterFacade.endCd()
