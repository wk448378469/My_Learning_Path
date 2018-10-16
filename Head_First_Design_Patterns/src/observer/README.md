观察者模式：定义了对象之间的一对多依赖，这样一来，当一个对象改变状态时，它的所有依赖者都会收到通知并自动更新。

>一对多中的“一”：
>>WeatherData.java
>>>*. 继承自Observable.java， 即可以被观察的类
>>>*. setMeasurements() 设置三个测量值
>>>*. getXX() 获取属性
>>>*. measurementsChanged() 状态变化，调用Observable中的setChanged与notifyObservers方法
>>>*. notifyObservers方法为向观察者推送新的数据


>一对多中的“多”：
>>CurrentConditionsDisplay.java、ForecastDisplay.java、StatisticsDisplay.java
>>>*. 实现DisplayElement.java, Observer.java这两个接口
>>>*. asd



