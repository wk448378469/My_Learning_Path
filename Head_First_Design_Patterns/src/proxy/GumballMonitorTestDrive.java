package proxy;

import java.rmi.Naming;

public class GumballMonitorTestDrive {
    public static void main(String[] args){
        String[] location = {"rmi://127.0.0.1:9999/gumballmachine1",
                             "rmi://127.0.0.1:9999/gumballmachine2",
                             "rmi://127.0.0.1:9999/gumballmachine3"};

        GumballMonitor[] monitors = new GumballMonitor[location.length];

        for (int i = 0; i < location.length; i++){
            try{
                GumballMachineRemote machine = (GumballMachineRemote) Naming.lookup(location[i]);
                monitors[i] = new GumballMonitor(machine);
            }catch (Exception e){
                e.printStackTrace();
            }
        }

        for (int i = 0; i < monitors.length; i++)
            monitors[i].report();
    }
}
