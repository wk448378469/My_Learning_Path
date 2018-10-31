代理模式：为另一个对象提供一个替身或占位符以控制对这个对象的访问。

* 接口类 GumballMachineRemote.java
    1. 这个接口继承自Remote.java
    2. 所有的方法必须定义异常处理
    3. 方法返回的结果要可以序列化（用以网络传输）

* 接口类的实现 GumballMachine.java
    1. 实现GumballMachineRemote.java中方法
    2. 继承自UnicastRemoteObject.java
    3. 类初始化的时候记得抛异常处理

* 服务端（被代理者的创建和关联）GumballMachineTestDrive.java
    1. 定义了一些GumballMachine.java的实例对象
    2. 通过rmi绑定到某接口下的某个路径下，等着被lookup

* 客户GumballMonitor.java   Monitor监控
    1. 实例化的时候接收一个GumballMachineRemote.java的实例
    2. 调用初始化时传入的实例的具体方法

* 客户测试GumballMonitorTestDrive.java
    1. 根据地址，找到一堆GumballMachineRemote.java的实例
    2. 创建一堆GumballMonitor.java实例，并把第一步的实例传入
    3. 调用GumballMonitor.java 的方法，达到对GumballMachineRemote.java的操作