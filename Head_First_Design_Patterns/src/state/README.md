状态模式：允许对象在内部状态改变时改变它的的行为，对象看起来好像修改了它的类

* 接口 State.java
    1. 状态类，每个实现类都需要实现一些“约定俗成”的行为（方法）

* 接口State.java的实现，HasQuarterState.java NoQuarterState.java SoldOutState.java SoldState.java WinnerState.java
    1. 初始化时接收一个具体所有状态的变量的类
    2. 实现State.java的一些方法
    3. 这些方法中，有可能涉及到状态的转换，调用初始化时的保存的类中的相关方法进行状态转换


* 实体类GumballMachine.java，该类具有各种各样的状态+行为
    1. 实例化各种状态类，并将自身传入进去
    2. 提供一些方法供别人使用
    3. 这些方法中最重要的是设置状态和具体行为

* 测试类GumballMachineTestDrive.java
