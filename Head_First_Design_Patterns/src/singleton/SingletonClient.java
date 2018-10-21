package singleton;

public class SingletonClient {
    public static void main(String[] agrs){
        Singleton singleton = Singleton.getInstance();
        System.out.println(singleton.otherUsefulMethods());

        Singleton singleton1 = Singleton.getInstance();
        if (singleton.equals(singleton1)){
            System.out.println("two val points to one memory address");
        }
    }
}
