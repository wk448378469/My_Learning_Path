package proxy;

import java.rmi.RemoteException;
import java.rmi.server.UnicastRemoteObject;

public class GumballMachine extends UnicastRemoteObject implements GumballMachineRemote{
    String location;
    int count;

    public GumballMachine(String location, int count) throws RemoteException {
        this.location = location;
        this.count = count;
    }

    public String getLocation(){
        return location;
    }

    public int getCount(){
        return count;
    }
}
