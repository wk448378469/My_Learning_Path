package collection;

import java.util.ArrayList;

public class PancakeHouseMenu implements Menu{
    ArrayList menuItems;

    public PancakeHouseMenu(){
        menuItems = new ArrayList();
        addItem("K&B's Pancake Breakfast", "", true,2.99);
        addItem("Regular Pancake Breakfast", "", false, 2.99);
        addItem("Blueberry Pancakes", "", true, 3.49);
        addItem("Waffles", "", true, 3.59);
    }

    public void addItem(String name,
                        String desc,
                        boolean vegetarian,
                        double price){
        MenuItem menuItem = new MenuItem(name, desc, vegetarian, price);
        menuItems.add(menuItem);
    }

    @Deprecated
    public ArrayList getMenuItems(){
        return menuItems;
    }

    public Iterator createIterator(){
        return new PancakeHouseMenuIterator(menuItems);
    }
}

