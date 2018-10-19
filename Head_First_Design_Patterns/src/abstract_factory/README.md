抽象工厂模式：提供一个接口，用于创建相关或依赖对象的家族，而不需要明确指定具体类。

* 披萨原材料(工厂)接口 PizzaIngredientFactory.java
    1. 实现该接口的类，需要实现六个原材料的创建

* 披萨原材料(工厂)实现，NYPizzaIngredientFactory.java ChicagoPizzaIngredientFactory.java
    1. 实现PizzaIngredientFactory.java中的六种创建原材料的方法
    2. 每种方法均返回一个原材料接口的具体实现的实例


* 披萨商店抽象类 PizzaStore.java
    1. 抽象方法createPizza()需要子类去实现
    2. orderPizza() 返回披萨Pizza对象

* 披萨商店子类 ChicagoPizzaStore.java NYPizzaStore.java
    1. 实现PizzaStore.java接口中得到createPizza()方法
    2. 这个方法是最重要的枢纽，连接工厂和产品，即将实例化的工厂对象传给对应的披萨(产品)进行披萨的实例化，返回披萨实例
    3. 工厂知道如何选择原材料，所以不需要这类知道实现细节


* 披萨(产品)抽象类 Pizza.java
    1. 六个属性值，对应下面的六个原材料
    2. 抽象方法prepare()，需要去实现

* 披萨(产品)子类 CheesePizza.java VeggiePizza.java ClamPizza.java PepperoniPizza.java
    1. 类初始化时，接收工厂对象
    2. 实现父类的prepare()，即调用工厂对象中的各种原材料来构成披萨


* 原材料接口 Dough.java Clams.java Sauce.java Cheese.java Veggies.java Pepperoni.java
    1. 实现该四个接口的类均需要实现toString()
    2. 翻译： dough-面团 clam-蛤 sauce-酱 cheese-奶酪 veggies-蔬菜 pepperoni-香肠

* 原材料实现，实现上面6个接口的
    1. Veggies.java的下列实现：
        * BlackOlives.java       黑橄榄
        * Eggplant.java          茄子
        * Garlic.java            大蒜
        * Mushroom.java          蘑菇
        * Onion.java             洋葱
        * RedPepper.java         红辣椒
        * Spinach.java           菠菜

    2. Dough.java的下列实现：
        * ThickCrustDough.java    厚皮面团
        * ThinCrustDough.java     薄皮面团

    3. Sauce.java的下列实现：
        * MarinaraSauce.java      番茄酱
        * PlumTomatoSauce.java    李子番茄酱

    4. Cheese.java的下列实现：
        * MozzarellaCheese.java   莫扎里拉干酪
        * ParmesanCheese.java     意大利干酪
        * ReggianoCheese.java     雷吉诺奶酪

    5. Clam.java的下列实现：
        * FreshClams.java         鲜蛤
        * FrozenClams.java        冻蛤

    6. Pepperoni.java的下列实现：
        * SlicedPepperoni.java    意大利辣香肠

* 测试类 PizzaTestDrive.java