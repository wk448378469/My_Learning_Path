package abstract_factory;

public class PizzaTestDrive {
    public static void  main (String[] args){
        PizzaStore nyStore = new NYPizzaStore();
        PizzaStore chicagoStore = new ChicagoPizzaStore();

        Pizza pizza = nyStore.orderPizza("cheese");
        System.out.println("Ordered a " + pizza + "\n\n");

        pizza = chicagoStore.orderPizza("clam");
        System.out.println("Ordered a " + pizza + "\n\n");
    }
}
