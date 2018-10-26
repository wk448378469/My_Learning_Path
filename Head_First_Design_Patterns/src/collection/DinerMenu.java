package collection;

public class DinerMenu implements Menu{
    static final int MAX_ITEMS = 6;
    int numberofItems = 0;
    MenuItem[] menuItems;

    public DinerMenu(){
        menuItems = new MenuItem[MAX_ITEMS];
        addItem("Vegetarian BLT","",true, 2.99);
        addItem("BLT","", false, 2.99);
        addItem("Soup of the day", "", false, 3.29);
        addItem("Hotdog","", false, 3.05);
    }

    public void addItem(String name, String desc, boolean vegetarian, double price){
        MenuItem menuItem = new MenuItem(name, desc, vegetarian, price);
        if(numberofItems >= MAX_ITEMS)
            System.err.println("menu is full!");
        else{
            menuItems[numberofItems] = menuItem;
            numberofItems = numberofItems + 1;
        }
    }

    @Deprecated
    public MenuItem[] getMenuItems(){
        return menuItems;
    }

    public Iterator createIterator(){
        return new DinerMenuIterator(menuItems);
    }
}
