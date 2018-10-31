package proxy;

import java.rmi.Remote;
import java.rmi.RemoteException;

public interface GumballMachineRemote extends Remote {
    public String getLocation() throws RemoteException;
    public int getCount() throws RemoteException;
}
