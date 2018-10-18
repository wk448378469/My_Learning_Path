简单工厂：其实并不是设计模式之一，更像是一种编程习惯。

* 工厂类 SimplePizzaFactory.java
    1. 根据传入的类型参数，判断返还何种产品

* 工厂类的“客户？” PizzaStore.java
    1. 初始化时实例化工厂类
    2. 根据传入的类型参数，生成披萨订单，返回披萨

* 产品们的父类 Pizza.java
    1. 是抽象类，所需要被继承
    2. 包含一些属性和方法
    3. toString() 返回字符串表示披萨的种类和成分

* 产品 CheesePizza.java ClamPizza.java PepperoniPizza.java VeggiePizza.java
    1. 四个产品均继承自Pizza.java

* 测试类 PizzaTestDrive.java