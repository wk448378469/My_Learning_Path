package abstract_factory;

public abstract class Pizza {
    String name;
    Dough dough;
    Sauce sauce;
    Veggies veggies[];
    Cheese cheese;
    Pepperoni pepperoni;
    Clams clams;

    abstract void prepare();

    void bake(){
        System.out.println("Bake for 25min at 350");
    }

    void cut(){
        System.out.println("Cutting the pizza into diagonal slices");
    }

    void box(){
        System.out.println("Place pizza in official PizzaStore box");
    }

    void setName(String name){
        this.name = name;
    }

    String getName(){
        return name;
    }

    public String toString(){
        StringBuffer result = new StringBuffer();
        result.append("---- " + name + " ----\n");
        if (dough != null)
            result.append(dough + "\n");
        if (sauce != null)
            result.append(sauce + "\n");
        if (cheese != null)
            result.append(cheese + "\n");

        if (veggies != null){
            for (int i = 0; i < veggies.length; i++){
                result.append(veggies[i]);
                if (i < veggies.length-1)
                    result.append(", ");
            }
        }

        if (clams != null)
            result.append(clams + "\n");
        if (pepperoni != null)
            result.append(pepperoni + "\n");

        return result.toString();
    }
}
