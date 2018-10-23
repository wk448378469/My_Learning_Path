# -*- coding: utf-8 -*-
"""
Created on Tue Oct 23 17:38:39 2018

@author: 凯风
"""

from RemoteControl import RemoteControl
from executor import Light, CeilingFan, Stereo, GarageDoor
import command

if __name__ == "__main__":
    remoteControl = RemoteControl()

    livingRoomLight = Light("Living Room")
    ceilingFan = CeilingFan("Living Room")
    garageDoor = GarageDoor("")
    stereo = Stereo("Kitchen Room")
    
    ceilingFanMediumCommand = command.CeilingFanMediumCommand(ceilingFan)
    ceilingFanHighCommand = command.CeilingFanHighCommand(ceilingFan)
    ceilingFanLowCommand = command.CeilingFanLowCommand(ceilingFan)
    ceilingFanOffCommand = command.CeilingFanOffCommand(ceilingFan)
    
    livingRoomLightOn = command.LightOnCommand(livingRoomLight)
    livingRoomLightOff = command.LightOffCommand(livingRoomLight)
    
    stereoOnWithCDCommand = command.StereoOnWithCDCommand(stereo)
    stereoOffCommand = command.StereoOffCommand(stereo)
    
    garageDoorDownCommand = command.GarageDoorDownCommand(garageDoor)
    garageDoorUpCommand = command.GarageDoorUpCommand(garageDoor)
    
    partyOn = [ceilingFanHighCommand, livingRoomLightOn]
    partyOff = [ceilingFanOffCommand, livingRoomLightOff]
    
    partyOnMacro = command.MacroCommand(partyOn)
    partyOffMacro = command.MacroCommand(partyOff)
    
    
    remoteControl.setCommand(0, partyOnMacro, partyOffMacro)
    remoteControl.setCommand(1, ceilingFanMediumCommand, ceilingFanOffCommand)
    remoteControl.setCommand(2, ceilingFanLowCommand, ceilingFanOffCommand)
    remoteControl.setCommand(3, stereoOnWithCDCommand, stereoOffCommand)
    remoteControl.setCommand(4, garageDoorUpCommand, garageDoorDownCommand)

    print(remoteControl)

    for i in range(5):
        remoteControl.onButtonWasPressed(i)
        remoteControl.offButtonWasPushed(i)
        print("\n")
    
    remoteControl.undoButtonPushed()
    