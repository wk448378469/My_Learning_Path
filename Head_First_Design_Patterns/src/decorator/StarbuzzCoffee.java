package decorator;

public class StarbuzzCoffee {
    public static void main(String agrs[]){
        Beverage beverage = new Espresso();
        System.out.println(beverage.getDescription() + " $" + beverage.cost() + "\n");

        Beverage beverage1 = new DarkRoast();    // 新的咖啡
        beverage1 = new Mocha(beverage1);        // 加摩卡
        beverage1 = new Mocha(beverage1);        // 再加摩卡
        beverage1 = new Whip(beverage1);         // 加whip
        beverage1 = new Soy(beverage1);          // 加soy
        System.out.println(beverage1.getDescription() + " $" + beverage1.cost() + "\n");
    }
}
