import os
import numpy as np
from PIL import Image as img


def create_results_folder(lab: int):
    create_folder_if_not_exists(f'labs/lab_{lab}/results')


def create_folder_if_not_exists(path: str):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass


def save_im(data: np.ndarray, task: int, lab: int, number_of_image: int):
    if lab > 4 or lab < 1:
        raise ValueError('Wrong lab input: ', lab)
    if task > 18 or task < 1:
        raise ValueError('Wrong task: ', task)
    if task < 1:
        raise ValueError('Wrong number of image: ', number_of_image)
    #create_results_folder(lab)
    if len(data.shape) < 2:
        data = img.fromarray(data)
    else:
        data = img.fromarray(data).convert('RGB')
    data.save(f'results/task_{task}_image_{number_of_image}.png')


def baricentrical(x: int, y: int, x0: float, y0: float, x1: float, y1: float, x2: float, y2: float):
    lambda0 = ((x1 - x2) * (y - y2) - (y1 - y2) * (x - x2)) / ((x1 - x2) * (y0 - y2) - (y1 - y2) * (x0 - x2))
    lambda1 = ((x2 - x0) * (y - y0) - (y2 - y0) * (x - x0)) / ((x2 - x0) * (y1 - y0) - (y2 - y0) * (x1 - x0))
    lambda2 = ((x0 - x1) * (y - y1) - (y0 - y1) * (x - x1)) / ((x0 - x1) * (y2 - y1) - (y0 - y1) * (x2 - x1))
    return [lambda0, lambda1, lambda2]


def normal(x0, y0, z0, x1, y1, z1, x2, y2, z2):
    return np.cross(np.array([x1 - x0, y1 - y0, z1 - z0]), np.array([x1 - x2, y1 - y2, z1 - z2]))


def find_cos(n: np.ndarray, l0=0, l1=0, l2=1):
    l_vec = np.array([l0, l1, l2])
    return n.dot(l_vec) / (np.linalg.norm(n) * np.linalg.norm(l_vec))
