from MyImage import MyImage
from MyModel import MyModel
from PIL import Image


def task_18():
    model = MyModel('C:\\Users\\m-tar\\Desktop\\4LabCG\\resources\\rabbit.obj')
    print("loop started")
    # image = LabImage(1000, 1000)
    # model.draw_trianlges(image, magnification=1500)
    # image.save(3, 16, 1)
    frames = []
    for i in range(20):
        image = MyImage(1000, 1000)
        model.rotate(0, i, 0)
        model.draw_trianlges(image, magnification=1500)
        image.save(4, 18, i)
        frames.append(Image.open(fr'results\task_18_image_{i}.png'))
        print(f'page {i} done')
    print("after loop")
    frames[0].save(
        'rabbit.gif',
        save_all=True,
        append_images=frames[1:],
        optimize=True,
        duration=300,
        loop=0
    )
    print("after save")


task_18()
