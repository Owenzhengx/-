pythonNet09.py

2.服务器模型
    循环模型　：同一时刻只能处理一个请求
    并发模型　：IO　并发　：多个IO任务　
    　　　　　　　　　多进程/多线程并发　：任何任务

３．基于fork的多进程并发程序
    每当有一个客户端连接就创建一个新的进程

４．ftp文件服务程序
*****************************************

多线程并发　

    threading 的多线程并发

    对比多进程并发：
        *　消耗资源较少
        *　线程应该更注意共享资源的操作
        *　在python中应该注意GIL问题，网络延迟较高，线程并发也是一种可行的办法

    实现步骤：
        １．创建套接字，绑定监听
        ２．接收客户端请求，创建新的线程
        ３．主线程继续接收其他客户端连接
        ４．分支线程启动对应的函数处理客户端请求
        ５．当客户端断开，则分支线程结束

        示例：thread_server.py　　process.py

    *cookie
        import traceback

        traceback.print_exc()
        功能　：更详细的打印异常信息
        示例：trace.py


功能，参数，返回值

集成模块的使用
    python2 SocketServer
    python3 SocketServer

    功能　：通过模块的不同类的组合完成多进程/多线程　的tcp/udp的并发

    StreamRequestHandler 处理tcp套接字请求类
    DatagramRequestHandler 处理udp套接字请求

    TCPServer  创建tcp server
    UDPServer  创建udp server

    ForkingMixIn  创建多进程
    ForkingTCPServer  --->   ForkingMixIn + TCPServer
    ForkingUDPServer  --->   ForkingMixIn + UDPServer

    ThreadingMixIn  创建多线程
    ThreadingTCPServer  --->  ThreadingMixIn + TCPServer
    ThreadingUDPServer  --->  ThreadingMixIn + UDPServer

    示例见：sock_server.py，sock_server1.py


HTTPServer V2.0
    １．接收客户端请求
    ２．解析客户端请求
    ３．组织数据，形成http response
    ４．将数据发送给客户端

    升级：
        １．采用多线程并发接收多个客户端请求
        ２．基本的请求解析，根据请求返回相应的内容
        ３．除了可以请求静态网页，也可以请求简单的数据
        ４．将功能封装在一个类中

    技术点：
        １．socket tcp　套接字
        ２．http 协议的请求响应格式
        ３．线程并发的创建方法
        ４．类的基本使用

    示例：HTTPServer.py

协程基础
    定义　：纤程，微线程．协程的本质是一个单线程程序，所以协程不能够使用计算机多核资源

    作用　：能够高效的完成并发任务，占用较少的资源，因此协程的并发量较高

    原理　：通过记录应用层的上下文栈区，实现在运行中进行上下文跳转，达到可以选择性的运行想要运行的部分，
            以此提高程序的运行效率

    优点　：消耗资源少
        　　无需切换开销
        　　无需同步互斥
        　　IO并发性好

    缺点　：无法利用计算机多核

    yield  --->  协程实现的基本关键字

    greenlet
        greenlet.greenlet() 生成协程对象
        gr.switch() 选择要执行的协程事件

        示例：greenlet0.py

    gevent
        １．将协程事件封装为函数
        ２．生成协程对象
            gevent.spawn(func,argv)
            功能　：生成协程对象
            参数　：func  协程函数
                　　argv  给协程函数传参
            返回值　：返回协程对象
        ３．回收协程
            gevent.joinall()
            功能　：回收协程
            参数　：列表　将要回收的协程放入列表

        gevent.sleep()
            功能　：设置协程阻塞，让协程跳转
            参数　：n 阻塞时间

        示例　：gevent_test.py

        from gevent import monkey
        monkey.patch_all()
            功能　：修改套接字的IO阻塞行为

            *　必须在socket导入之前使用

            示例：gevent_server.py 重点在２０行