from use import Process
import time

class cheak:
    def __init__(self):
        self.cheak = True
        self.computer = Process.Computer()
        self.process = Process.Process()
        self.cpuUseList = []
        self.memyUseList = []



    def averageCPU(self):
        if len(self.cpuUseList)>30:
            self.cpuUseList.pop(-1)
        u = self.computer.getCPUse()
        self.cpuUseList.append(u)
        print('CPU使用率{}%'.format(u))

    def averageMemy(self):
        if len(self.memyUseList)>30:
            self.memyUseList.pop(-1)
        u = self.computer.getMemoryUse()
        self.memyUseList.append(u)
        print('内存使用{}G'.format(u))

    def __cheakRun(self):
        d = self.process.isDeadlineslaveRun() == False #如果 deadline 没有运行  并且  houdini 没有运行 并且 短时间内cpu使用量 小于30  并且 内存使用率 小于15 G 
        h = self.process.isHouUsed() == False
        self.averageCPU()
        self.averageMemy()

        cpu = max(self.cpuUseList)<10
        memy = max(self.memyUseList)<10

        print(d,h,cpu,memy)


        if d and h and cpu and memy :
            Process.Deadline().openSlave()
            self.cheak = False
            print('已经打开deadline')
            self.__re_run()

    def run(self):
        while self.cheak:
            pos = self.computer.getMousePos()
            time.sleep(10)
            newPos = self.computer.getMousePos()
            if pos == newPos:
                self.__cheakRun()
            else :
                self.cheak = False
                print('鼠标动停止检测')
                self.__re_run()

    def __re_run(self):
        while not self.cheak:
            pos = self.computer.getMousePos()
            time.sleep(10)
            newPos = self.computer.getMousePos()
            if pos == newPos:
                self.cheak = True
                print('鼠标不动继续检测')

