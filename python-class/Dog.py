class Dog:
    d_type = "京巴"  # 属性，类属性，类变量，公共属性

    def __init__(self, name, age):  # 初始化方法，构造方法，构造函数， 实例化时会自动执行，进行一些初始化工作。
        print("hahahahha", name, age)
        # 要想把name，age这两个值，真正的存储到实例里，那就需要把这两个值跟实例绑定
        self.name = name  # 绑定参数值到实例上
        self.age = age

    def say_hi(self):  # 方法，函数，第一个参数，必须是self，self代表实例本身
        print("hello, i am a dog, my type is ", self.d_type)
        print("hello, i am a dog, my type is ", self.d_type, self.name, self.age)


d = Dog("mjj", 3)  # 生成一个实例
d2 = Dog("毛蛋", 5)

d.say_hi()  # 调用方法
d2.say_hi()

print(Dog.d_type)
print(d.d_type)

Dog.d_type = "金毛"

print(Dog.d_type)
print(d.d_type)

print(d.name)
print(d.age)
