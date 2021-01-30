import yaml


class Animal:
    name: str = None
    colour: str = None
    age: int = 0
    gender = "公"

    def __init__(self, name, colour, age, gender):
        self.name = name
        self.colour = colour
        self.age = age
        self.gender = gender

    def calling(self):
        print(f"{self.name}会叫")

    def running(self):
        print(f"{self.name}会跑")


class Cat(Animal):
    def __init__(self, hair, name, colour, age, gender):
        self.hair = hair
        super().__init__(name, colour, age, gender)

    def micecatching(self):
        print(f"{self.name}会抓老鼠")

    def calling(self):
        super().calling()
        print(f"{self.name}喵喵叫")


class dog(Animal):
    def __init__(self, hair, name, colour, age, gender):
        self.hair = hair
        super().__init__(name, colour, age, gender)

    def housekeeping(self):
        print(f"{self.name}会看家")

    def calling(self):
        super().calling()
        print(f"{self.name}汪汪叫")


if __name__ == '__main__':
    with open('demo_animal2.yml', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        print(datas['Cat'])
        print(datas["dog"])
        # hair = datas['Cat']['hair']
        # name = datas['Cat']['name']
        # colour = datas['Cat']['colour']
        # colour = datas['Cat']['colour']
        # colour = datas['Cat']['colour']
        # colour = datas['Cat']['colour']
        # colour = datas['Cat']['colour']

    bosimao = Cat("短发", "波斯猫", "白色", 4, "母")
    print(
        f"{bosimao.name}的毛发是{bosimao.hair}，{bosimao.name}的毛色是{bosimao.colour}，{bosimao.name}的年龄是{bosimao.age},{bosimao.name}的性别是{bosimao.gender}")
    bosimao.micecatching()

    jinmao = dog("金色", "金毛", "黄色", 5, "公")
    print(
        f"{jinmao.name}的毛发是{jinmao.hair}，{jinmao.name}的毛色是{jinmao.colour}，{jinmao.name}的年龄是{jinmao.age},{jinmao.name}的性别是{jinmao.gender}")

    jinmao.housekeeping()
