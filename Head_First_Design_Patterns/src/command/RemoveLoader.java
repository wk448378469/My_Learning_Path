package command;

public class RemoveLoader {
    public static void main(String[] agrs){
        // 遥控器实例化
        RemoteControl remoteControl = new RemoteControl();

        // 电器实例化
        Light livingRoomLight = new Light("Living Room");
        CeilingFan ceilingFan = new CeilingFan("Living Room");
        //Light kitchenLight = new Light("Kitchen");
        //CeilingFan ceilingFan = new CeilingFan("Living Room");
        //GarageDoor garageDoor = new GarageDoor("");
        Stereo stereo = new Stereo("Living Room");

        // 命令实例化
        CeilingFanMediumCommand ceilingFanMediumCommand = new CeilingFanMediumCommand(ceilingFan);
        CeilingFanHighCommand ceilingFanHighCommand = new CeilingFanHighCommand(ceilingFan);
        CeilingFanLowCommand ceilingFanLowCommand = new CeilingFanLowCommand(ceilingFan);
        CeilingFanOffCommand ceilingFanOffCommand = new CeilingFanOffCommand(ceilingFan);
        LightOnCommand livingRoomLightOn = new LightOnCommand(livingRoomLight);
        LightOffCommand livingRoomLightOff = new LightOffCommand(livingRoomLight);
        //LightOnCommand kitchenLightOn = new LightOnCommand(kitchenLight);
        //LightOffCommand kitchenLightOff = new LightOffCommand(kitchenLight);
        //CeilingFanOnCommand ceilingFanOnCommand = new CeilingFanOnCommand(ceilingFan);
        //CeilingFanOffCommand ceilingFanOffCommand = new CeilingFanOffCommand(ceilingFan);
        //GarageDoorUpCommand garageDoorUpCommand = new GarageDoorUpCommand(garageDoor);
        //GarageDoorDownCommand garageDoorDownCommand = new GarageDoorDownCommand(garageDoor);
        StereoOnWithCDCommand stereoOnWithCDCommand = new StereoOnWithCDCommand(stereo);
        StereoOffCommand stereoOffCommand = new StereoOffCommand(stereo);

        // 组合命令
        Command[] partyOn = {livingRoomLightOn, stereoOnWithCDCommand};
        Command[] partyOff = {livingRoomLightOff, stereoOffCommand};
        MacroCommand partyOnMacro = new MacroCommand(partyOn);
        MacroCommand partyOffMacro = new MacroCommand(partyOff);


        // 将命令绑定至按钮
        remoteControl.setCommand(0, ceilingFanMediumCommand, ceilingFanOffCommand);
        remoteControl.setCommand(1,ceilingFanHighCommand, ceilingFanOffCommand);
        remoteControl.setCommand(2, ceilingFanLowCommand, ceilingFanOffCommand);
        remoteControl.setCommand(3, partyOnMacro, partyOffMacro);

        // 按下按钮
        for (int i = 0; i < 4; i++){
            remoteControl.onButtonWasPressed(i);
            remoteControl.offButtonWasPushed(i);
            System.out.println("\n");
        }

        // 打印控制器
        System.out.println(remoteControl);

        // 撤销操作
        remoteControl.undoButtonWasPushed();

    }
}
