策略模式：定义了算法族，分别封装起来，让它们之间可以相互替换，此模式让算法的变化独立于使用算法的客户。

封装飞行行为：
    接口       ：FlyBehavior.java
    需实现     ：fly()
    接口的实现 ：FlyWithWings.java、FlyRocketPowered.java、FlyNoWay.java

封装呱呱叫行为：
    接口       ：QuackBehavior.java
    需实现     ：quack()
    接口的实现 ：MuteQuack.java、Quack.java、Squeak.java

抽象类（父类） ：
    类名       ：Duck.java
    属性       ：
                    FlyBehavior flyBehavior
                    QuackBehavior quackBehavior
    方法       ：
                    swim()
                    display()               抽象方法
                    performQuack()          执行接口的quack()
                    setQuackBehavior()      设置quackBehavior变量
                    performFly()            执行接口的fly()
                    setFlyBehavior()        设置flyBehavior变量

子类（继承自Duck）
    类名       ： MallardDuck.java、ModelDuck.java
    方法       ：
                    display                 实现父类的抽象方法


测试
    类名       ：MiniDuckSimulater.java