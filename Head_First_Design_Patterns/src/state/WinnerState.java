package state;

public class WinnerState implements State {
    GumballMachine gumballMachine;

    public WinnerState(GumballMachine gumballMachine){
        this.gumballMachine = gumballMachine;
    }

    public void insertQuarter(){
        System.out.println("Please wait, we're already giving you a gumball");
    }

    public void ejectQuarter(){
        System.out.println("Sorry, you already turned the crank");
    }

    public void turnCrank(){
        System.out.println("Turing twice doesn't get you another gumball!");
    }

    public void refill(){}

    public void dispense(){
        System.out.println("YOU'RE A WINNER! You get two gumballs for you quarter");
        gumballMachine.releaseBall();

        if (gumballMachine.getCount() == 0){
            gumballMachine.setState(gumballMachine.getSoldOutState());
        }
        else{
            gumballMachine.releaseBall();
            if (gumballMachine.getCount() > 0){
                gumballMachine.setState(gumballMachine.getNoQuarterState());
            }else{
                System.out.println("Oops, out of gumballs");
                gumballMachine.setState(gumballMachine.getSoldOutState());
            }
        }
    }

    public String toString(){
        return "despensing two gumballs for you quarter, because YOU'RE A WINNER!";
    }
}
