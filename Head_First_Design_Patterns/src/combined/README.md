* 复合模式：复合模式结合两个或以上的模式，组成一个解决方案，解决一再发生的一般性问题。

* 复合模式中的案例：MVC（模型-视图-控制器）
    1. 模型，使用观察者模式，以便观察者更新，同时保持解耦
    2. 视图，使用组合模式实现用户界面，用户界面通常组合了嵌套的组件，像面板，框架和按钮
    3. 控制器，是视图的策略，视图可以使用不同的控制器实现，得到不同的行为
    4. 对于新增的模型+控制器的功能，使用适配者模式将新的模型适配成已有的视图上（控制器可重新也可不重写）


* 模型接口 BeatModelInterface.java HeartModelInterface.java
    1. 除了自己一些特殊的方法外，最重要的就是观察者的一些方法，注册观察者和移出观察者

* 模型 BeatModel.java HeartModel.java HeartAdapter.java 实现模型接口
    1. BeatModel.java和HeartModel.java 作为整个系统的核心，所有的逻辑都在这里
    2. BeatModel.java和HeartModel.java 除了1之外，作为被观察者，如果有状态的更新也要通知观察者
    3. 适配器HeartAdapter.java，接收一个HeartModel.java的实例，使其可以实现BeatModel.java的相关功能


* 观察者接口 BeatObserver.java BPMObserver.java
    1. 接收更新的方法

* 视图 DJView.java 实现观察者接口
    1. 初始化的时候接收模型和控制器的实例
    2. 把自己作为参数，利用模型的注册方法注册成为观察者，并实现接收通知的方法
    3. 一堆创建前端界面的方法，同时将相关的按钮触发事件绑定到控制器的方法上


* 控制器接口 ControllerInterface.java
    1. 定义了系统的一些功能，例如用户点击开始、暂停等方法

* 控制器 BeatController.java HeartController.java
    1. 初始化的时候接受一个模型作为参数
    2. 将自身和模型作为参数，创建一个视图
    3. 实现相关系统的功能具体处理中转过程，以供视图调用
    4. 本身并不处理太多逻辑，都是将用户的操作（行为）转给模型做处理


* 测试类 DJTestDrive.java HeartTestDrive.java
    1. 创建模型
    2. 将模型作为参数，创建一个控制器