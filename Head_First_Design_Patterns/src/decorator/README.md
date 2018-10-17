装饰者模式：动态地将责任附加到对象上。若要扩展功能，装饰者提供了比继承更有弹性的替代方案

* 超类Beverage.java （Beverage：饮料）
    1. 装饰者和被装饰者都需要继承自同一个超类（Beverage.java）
    2. getDescription() 获取属性，本例中为咖啡+配料的字符串
    3. cost() 抽象方法，本例为产品（咖啡+配料）的价值

* 被装饰类DarkRoast.java、Decaf.java、Espresso.java、HouseBlend.java （四种咖啡的种类）
    1. 四个均继承自Beverage.java
    2. 初始化时赋值类中的属性值（description，由超类继承而来）
    3. 实现超类中的抽象方法cost()， 即咖啡的价格

* 装饰父类CondimentDecorator.java （Condiment：配料）
    1. CondimentDecorator.java继承自Beverage.java
    2. Beverage.java本身也是一个抽象类，所以不需要重定义超类的cost()
    3. 重定义getDescription()为抽象方法

* 装饰类Mocha.java、Soy.java、Whip.java （三种具体的配料）
    1. 三个均继承自CondimentDecorator.java
    2. 类变量beverage用来保存被修饰类的对象，并且需要在初始化时传入
    3. getDescription() 获取beverage的description 并加上类自己的description
    4. cost() 获取beverage的cost 并加上类自己的cost

* 测试类StartbuzzCoffee.java