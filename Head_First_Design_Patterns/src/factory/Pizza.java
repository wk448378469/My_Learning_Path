package factory;

import java.util.ArrayList;

public abstract class Pizza {
    String name;
    String dough;       //用什么面
    String sauce;       //用什么酱
    ArrayList<String> toppings = new ArrayList<String>();       //配料

    public String getName(){
        return name;
    }

    void prepare(){
        System.out.println("Preparing...");
    }

    void bake(){
        //烘焙
        System.out.println("Baking...");
    }

    void cut(){
        System.out.println("Cutting...");
    }

    void box(){
        System.out.println("Boxing...");
    }

    public String toString(){
        StringBuffer diplay = new StringBuffer();
        diplay.append("---- " + name + " ----\n");
        diplay.append(dough + "\n");
        diplay.append(sauce + "\n");
        for (String topping: toppings
             ) {
            diplay.append(topping + "\n");
        }
        return diplay.toString();
    }

}
