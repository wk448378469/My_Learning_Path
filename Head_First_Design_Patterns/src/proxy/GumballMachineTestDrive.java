package proxy;

import java.rmi.Naming;
import java.rmi.registry.LocateRegistry;

public class GumballMachineTestDrive {
    public static void main(String[] args){
        try{
            LocateRegistry.createRegistry(9999);
            GumballMachine gumballMachine1 = new GumballMachine("beijing", 10);
            GumballMachine gumballMachine2 = new GumballMachine("shanghai", 20);
            GumballMachine gumballMachine3 = new GumballMachine("guangzhou", 30);

            Naming.rebind("rmi://127.0.0.1:9999/gumballmachine1", gumballMachine1);
            Naming.rebind("rmi://127.0.0.1:9999/gumballmachine2", gumballMachine2);
            Naming.rebind("rmi://127.0.0.1:9999/gumballmachine3", gumballMachine3);

        }catch (Exception e){
            e.printStackTrace();
        }
    }
}
