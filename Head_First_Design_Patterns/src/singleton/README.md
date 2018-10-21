单件模式：确保一个类只有一个实例，并提供一个全局访问点。

* 主类 Singleton.java
    1. 一个静态、volatile变量，用来记录Singleton这个类的唯一实例化
    2. 把构造器声明设为private，只有类内部才可以调用构造器
    3. getInstance()，实例化本类，并返回实例
    4. 利用volatile和synchronized来解决多线程问题


* 测试类 SingletonClient.java