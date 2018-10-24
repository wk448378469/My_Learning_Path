package adapter_use_class;

public class test {
    public static void main(String[] agrs){
        System.out.println("------ 适配器 -----");
        Moble moble = new Moble();
        moble.charging(new VoltageAdapter());
    }
}
