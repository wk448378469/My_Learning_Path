package simple_factory;

import java.util.ArrayList;

public abstract class Pizza {
    String name;
    String dough;       //用什么面
    String sauce;       //用什么酱
    ArrayList<String> toppings = new ArrayList<String>();       //配料

    public String getName(){
        return name;
    }

    public void prepare(){
        System.out.println("Preparing " + name);
    }

    public void bake(){
        //烘焙
        System.out.println("Baking " + name);
    }

    public void cut(){
        System.out.println("Cutting " + name);
    }

    public void box(){
        System.out.println("Boxing " + name);
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
