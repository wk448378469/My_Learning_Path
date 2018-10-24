package facade;

public class Projector {
    String description;
    DvdPlayer dvdPlayer;

    public Projector(String description, DvdPlayer dvdPlayer){
        this.description = description;
        this.dvdPlayer = dvdPlayer;
    }

    public void on(){
        System.out.println(description + " on");
    }

    public void off(){
        System.out.println(description + " off");
    }

    public void wideScreenMode(){
        System.out.println(description + " in widescreen mode (16*9 aspect ratio)");
    }

    public void tvMode(){
        System.out.println(description + " in tv mode (4*3 aspect ratio)");
    }

    public String toString(){
        return description;
    }

}
