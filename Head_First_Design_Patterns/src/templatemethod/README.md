模板方法模式：在一个方法中定义一个算法的骨架，而将一些步骤延迟到子类中。模板方法使得子类可以在不改变算法结构的情况下，重新定义算法中的某些步骤。

* 抽象类 CaffeeineBeverageWithHook.java 咖啡饮料并且有钩子
    1. prepareRecipe() 封装好所有的调用逻辑，且不可被子类扩展
    2. 抽象方法 brew() addCondiments() ，需要子类根据自己的需求进行编写
    3. 普通方法 boilWater() pourInCup() customerWantsCondiments() 子类可以重写可以直接用的

* 子类 Tea.java Coffee.java
    1. 继承自CaffeeineBeverageWithHook.java
    2. 提供一个私有方法getUserInput，来获取用户的输入，customerWantsCondiments() 会用到这个输入

* 测试类 BeverageTestDrive.java