组合模式：允许你将对象组合成树形结构来表现“整体/部分”层次结构。组合能让客户以一致的方式处理个别对象以及对象组合。

* 抽象类 MenuComponent.java 菜单组件，集合了两种子类的所有方法
    1. 抽象方法createIterator()，两种子类都必须要实现的
    2. 其他所有方法，菜单和条目的两种子类的方法，如果一个实现另一个，就抛异常

* 抽象类的两个子类 Menu.java MenuItem.java
    1. 两个类都实现了MenuComponent.java的部分方法

* 迭代器的实现 CompositeIterator.java NullIterator.java
    1. 因为这个菜单是树状结构，有的菜单项为菜单不是条目，所以自己实现迭代器要
    2. stack中的peek是返回栈顶的元素但不移除它
    3. MenuItem.java 是条目，是叶节点，没有子节点了，所以用NullIterator.java


* 菜单的使用者 Waitress.java
    1. 打印菜单

* 测试类 MenuTestDrive.java

