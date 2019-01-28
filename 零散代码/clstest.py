class Human(object):
    def __init__(self,h,w,color,name):
        self.h=h
        self.w=w
        self.color=color
        self.name=name
    def getBaseInfo(self):
        print('姓名:' ,self.name)
        print('肤色：',self.color)
        print('身高：',self.h)
        print('体重：',self.w)

    def getusuasay(self):
        print('他喜欢说:%s' %('enen aa') )
        
class AsiaMan(Human):
    def __init__(self,h,w,name):
        self.h=h
        self.w=w
        self.color='yellow'
        self.name=name

    def getusuasay(self):
        print('他喜欢说:%s' %('呵呵') )

class AficaMan(Human):
    def __init__(self,h,w,name):
        self.h=h
        self.w=w
        self.color='black'
        self.name=name

    def getusuasay(self):
        print('我是黑人')

human1=Human(172,65,'yellow','lsq')
print("print格式化输出测试，新对象姓名：%s,身高：%dcm、体重:%dkg，是个%s人" %(human1.name,human1.h,human1.w,human1.color))


human2=AsiaMan(180,50,'qqq')
print("print格式化输出测试，新对象姓名：%s,身高：%dcm、体重:%dkg，是个%s人" %(human2.name,human2.h,human2.w,human2.color))
print(human2.getusuasay())

human3=AficaMan(200,100,'www')
print("print格式化输出测试，新对象姓名：%s,身高：%dcm、体重:%dkg，是个%s人" %(human3.name,human3.h,human3.w,human3.color))
print(human3.getusuasay())
    
