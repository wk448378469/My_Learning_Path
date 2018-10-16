观察者模式：定义了对象之间的一对多依赖，这样一来，当一个对象改变状态时，它的所有依赖者都会收到通知并自动更新。

* 一对多中的“一” WeatherData.java
    1. 继承自Observable.java， 即可以被观察的类
    2. setMeasurements() 设置三个测量值
    3. getXX() 获取属性
    4. measurementsChanged() 状态变化，调用Observable中的setChanged与notifyObservers方法
    5. notifyObservers方法为向观察者推送新的数据

* 一对多中的“多” CurrentConditionsDisplay.java、ForecastDisplay.java、StatisticsDisplay.java
    1. 实现DisplayElement.java, Observer.java这两个接口
    2. 初始化的时候调用Observer中的addObserver方法，将实例化的自己加入至Observable的观察者列表中
    3. update() 实现Observer接口中的方法，接收更新的数据
    4. display() 实现DisplayElement接口中的方法，展示数据

* 测试类 WeatherStation.java

* java9 之后Observable.java 和 Observer.java 均已被弃用了
    1. 如果以后实践可以用书中介绍的第一部分自己实现
    2. 弃用的原因见这里：https://stackoverflow.com/questions/46380073/observer-is-deprecated-in-java-9-what-should-we-use-instead-of-it


