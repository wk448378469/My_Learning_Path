package collection;

import java.util.ArrayList;

public class PancakeHouseMenuIterator implements Iterator {
    ArrayList<MenuItem> items;
    int position = 0;

    public PancakeHouseMenuIterator(ArrayList<MenuItem> items){
        this.items = items;
    }

    public MenuItem next(){
        MenuItem menuItem = (MenuItem) items.get(position);
        position++;
        return menuItem;
    }

    public boolean hasNext(){
        if (position >= items.size())
            return false;
        else
            return true;
    }
}
