迭代器模式：提供一种方法顺序访问一个聚合对象中的各个元素，而又不暴露其内部的表示。

* 菜单条目类 MenuItem.java
    1. 菜单条目中的一道菜吧理解成，包含价格名字描述等

* 接口 Menu.java Iterator.java
    1. Menu.java 一个方法createIterator()
    2. Iterator.java 和原生的java接口类似，hasNext和next两个方法需要实现

* Iterator接口的实现类 DinerMenuIterator.java  PancakeHouseMenuIterator.java
    1. DinerMenuIterator.java 因为DinerMenu.java 用数组保存MenuItem对象，所以接收数组初始化的时候
    2. PancakeHouseMenuIterator.java 因为PancakeHouseMenu.java 用ArrayList保存MenuItem对象，所以接收ArrayList

* 菜单类 DinerMenu.java PancakeHouseMenu.java
    1. DinerMenu.java 实现Menu.java的createIterator()方法，返回一个DinerMenuIterator.java的对象
    2. PancakeHouseMenu.java 实现Menu.java的createIterator()方法，返回一个PancakeHouseMenuIterator.java对象

* 服务员 Waitress.java 不需要知道两个菜单的具体都有说明，只要遍历就可以了，实现解耦

* 测试类 MenuTestDrive.java