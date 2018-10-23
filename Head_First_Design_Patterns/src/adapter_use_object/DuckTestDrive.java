package adapter_use_object;

public class DuckTestDrive {
    public static void main(String[] args){
        MallardDuck duck = new MallardDuck();
        WildTurkey turkey = new WildTurkey();

        Duck turkeyAdapter = new TurkeyAdapter(turkey);

        System.out.println("The Turkey says...");
        turkey.gobble();
        turkey.fly();

        System.out.println("\nThe Duck says...");
        requirer(duck);         // 传入鸭子类型

        System.out.println("\nThe TurkeyAdapter says...");
        requirer(turkeyAdapter);        // 传入利用火鸡改的，像鸭子的适配器
    }

    static void requirer(Duck duck){
        // 这个方法需要鸭子类型的参数
        duck.quack();
        duck.fly();
    }
}
