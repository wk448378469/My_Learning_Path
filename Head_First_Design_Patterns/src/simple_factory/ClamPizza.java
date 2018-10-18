package simple_factory;

public class ClamPizza extends Pizza {
    public ClamPizza(){
        name = "Clam Pizza";
        dough = "Thin Crust";
        sauce = "White garlic Sauce";
        toppings.add("Clams");
        toppings.add("Grated parmesan cheese");
    }
}
