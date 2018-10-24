package adapter_use_class;

public class Moble {
    public void charging(Voltage5 voltage5) {
        if (voltage5.output5V() == 5)
            System.out.println("电压刚刚5V，手机开始充电");
        else
            System.out.println("电压不对，手机可能被你搞坏了");
    }
}
