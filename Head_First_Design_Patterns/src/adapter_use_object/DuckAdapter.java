package adapter_use_object;

import java.util.Random;

public class DuckAdapter implements Turkey {
    Duck duck;
    Random random;

    public DuckAdapter(Duck duck){
        this.duck = duck;
        random = new Random();
    }

    public void gobble(){
        duck.quack();
    }

    public void fly(){
        if (random.nextInt(5) == 0)
            duck.fly();
    }
}
