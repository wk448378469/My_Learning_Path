工厂方法模式：定义了一个创建对象的接口，但由子类决定要实例化的类是哪一个。工厂方法让类把实例化推迟到子类。


* 工厂父类 PizzaStore.java
    1. 抽象类，其中createPizza()方法为抽象方法，需要子类来实现
    2. orderPizza() 实例化产品并返回

* 工厂子类 ChicagoPizzaStore.java NYPizzaStore.java
    1. 实现父类要求的createPizza()方法，判断客户要求什么类型的披萨，并返回产品子类实例

* 产品父类 Pizza.java
    1. 是抽象类，所需要被继承
    2. 包含一些属性和方法
    3. toString() 返回字符串表示披萨的种类和成分

* 产品子类 ChicagoStyleCheesePizza.java NYStyleCheesePizza.java ChicagoStyleVeggiePizza.java 等
    1. 继承自Pizza.java， 类初始化的时候会定义一些父类要求的属性的值

* 测试类 PizzaTestDrive.java
