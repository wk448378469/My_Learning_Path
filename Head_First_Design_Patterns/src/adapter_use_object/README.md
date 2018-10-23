对象适配器模式：将一个类的接口，转换为客户期望的另一个接口。适配器让原本接口不兼容的类可以合作无间。

* 接口 Duck.java Turkey.java
    1. Duck.java 鸭子的接口，需要实现quack和fly两个方法
    2. Turkey.java 火鸡的接口，需要实现gobble和fly两个方法

* 两个接口的实现 MallarDuck.java WildTurkey.java
    1. 就是各自实现自己的接口，没什么好说的

* 两个适配器类 DuckAdapter.java TurkeyAdapter.java
    1. 以TurkeyAdapter.java为例，该类需要实现Duck.java接口
    2. 初始化的时候需要传入一个实现了Turkey.java的对象
    3. 因为要实现Duck.java中的quack方法，所以调用初始化时传入的Turkey.java的对象中的gobble方法来代替quack
    4. 因为都有fly，所以具体看那需求吧

* 测试类DuckTestDrive.java
    1. requirer()方法为适配器使用者，他需要一个参数，这个参数需要实现Duck.java这个接口
    2. 可以穿入MallarDuck.java的实例，也可以传入适配器TurkeyAdapter.java 用来做“伪装成”鸭子传入进去