from MyImage import MyImage
from MyModel import MyModel


def task_16():
    model = MyModel('C:\\Users\\m-tar\\Desktop\\4LabCG\\resources\\rabbit.obj')
    print("0")
    image = MyImage(1000, 1000)
    print("1")
    model.bend(10, 10, 0.15, 0.15, 0.01)
    print("2")
    model.draw_trianlges(image, magnification=1500)
    print("3")
    image.save(3, 16, 1)


def task_17():
    model = MyModel('C:\\Users\\m-tar\\Desktop\\4LabCG\\resources\\rabbit.obj')
    print("0")
    image = MyImage(1000, 1000)
    print("1")
    model.rotate(0, 30, 0)
    print("2")
    model.draw_trianlges(image, magnification=1500)
    print("3")
    image.save(3, 17, 1)

task_16()
task_17()
