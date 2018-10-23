命令模式：将“请求”封装成对象，以便使用不同的请求、队列或者日志来参数化其他对象。命令模式也支持可撤销的操作。

* 家电类（被命令者）CeilingFan.java Light.java GarageDoor.java Stereo.java
    1. 就是一些被别人操作的类，提供一些开关或调整的方法


* 命令接口 Command.java
    1. execute() 执行动作
    2. undo() 撤销上一次操作

* 命令接口的实现，这些实现必须实现execute和undo这两个方法，初始化时需要告知绑定的家电类（除了组合命令）
    1. 吊扇(CeilingFan.java)相关命令
        * CeilingFanHighCommand.java
        * CeilingFanLowCommand.java
        * CeilingFanMediumCommand.java
        * CeilingFanOffCommand.java

    2. 车库门(GarageDoor.java)相关命令
        * GarageDoorDownCommand.java
        * GarageDoorUpCommand.java

    3. 灯(Light.java)相关命令
        * LightOffCommand.java
        * LightOnCommand.java

    4. 音响(Stereo.java)相关命令
        * StereoOffCommand.java
        * StereOffCommand.java

    5. 组合命令(MacroCommand.java)，初始化的时候用数组来保存一组命令，然后execute依次执行每一条命令的execute，undo类似

    6. 啥都不干命令(NoCommand.java)，就是实现了execute和undo但是函数体啥都不干

* 控制器(RemoteControl.java 可以称为调用者？)
    1. 用一些变量来保存传入的命令
    2. 提供一些方法来执行相关命令的execute或undo方法

* 测试类 RemoveLoader.java