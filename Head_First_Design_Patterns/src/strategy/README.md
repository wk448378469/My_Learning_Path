策略模式：定义了算法族，分别封装起来，让它们之间可以相互替换，此模式让算法的变化独立于使用算法的客户。

* 封装飞行行为：
    1. 接口       ：FlyBehavior.java
    2. 需实现     ：fly()
    3. 接口的实现 ：FlyWithWings.java、FlyRocketPowered.java、FlyNoWay.java

* 封装呱呱叫行为：
    1. 接口       ：QuackBehavior.java
    2. 需实现     ：quack()
    3. 接口的实现 ：MuteQuack.java、Quack.java、Squeak.java

* 抽象类（父类） ：
    1. 类名       ：Duck.java
    2. 属性       ：
                    1. FlyBehavior flyBehavior
                    2. QuackBehavior quackBehavior
    3. 方法       ：
                    1. swim()
                    2. display()               抽象方法
                    3. performQuack()          执行接口的quack()
                    4. setQuackBehavior()      设置quackBehavior变量
                    5. performFly()            执行接口的fly()
                    6.setFlyBehavior()        设置flyBehavior变量

* 子类（继承自Duck）
    1. 类名       ： MallardDuck.java、ModelDuck.java
    2. 方法       ：
                    1.display                 实现父类的抽象方法


* 测试
    1.类名       ：MiniDuckSimulater.java