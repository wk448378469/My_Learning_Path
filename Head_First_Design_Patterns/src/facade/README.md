外观模式：提供了一个统一的接口，用来访问子系统中的一群接口。外观定义了一个高层接口，让子系统更容易使用。

* 一堆家电类 Amplifier.java CdPlayer.java DvdPlayer.java PopcornPopper.java Projector.java Screen.java TheaterLights.java Tuner.java
    1. 这些子类，乱七八糟的，彼此之间还有依赖关系
    2. 如果调用者自己调用就很烦，然后就是耦合

* 外观类 HomeTheaterFacade.java
    1. 封装好一些好用的接口给调用者用
    2. 调用者就不用操心那一堆家电类了

* 测试类 HomeTheaterTestDrive.java