package command;

// 车库门
public class GarageDoor {
    String location = "";

    public GarageDoor(String location){
        this.location = location;
    }

    public void up(){
        System.out.println(location + " garage door is up");
    }

    public void down(){
        System.out.println(location + " garage door is down");
    }

    public void stop(){
        System.out.println(location + " garage door is stop");
    }

    public void lightOn(){
        System.out.println(location + " garage door light is on");
    }

    public void lightOff(){
        System.out.println(location + " garage door light is on");
    }
}
