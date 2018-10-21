package singleton;

public class Singleton {
    private volatile static Singleton uniqueInstance;

    private Singleton() {}

    public static Singleton getInstance(){
        if (uniqueInstance == null){
            synchronized (Singleton.class){
                if (uniqueInstance == null){
                    uniqueInstance = new Singleton();
                }
            }
        }
        return uniqueInstance;
    }

    public String otherUsefulMethods(){
        return "I'm a classic Singleton!\n";
    }
}
