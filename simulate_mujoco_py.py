from mujoco_py import load_model_from_path, MjSim, MjViewer
from mujoco_py.modder import TextureModder
import mujoco_py as mp

import os
import time
import math
import numpy as np

model = load_model_from_path("gym_agent/assets/model.xml")
sim = MjSim(model)
viewer = MjViewer(sim)
t=0
while True:
    #   sim.data.ctrl[1] = math.cos(t / 10.) * 0.01
    sim.step()
    #t = time.time()
    #x, y = math.cos(t), math.sin(t)
    #viewer.add_marker(pos=np.array([x, y, 1]))
    #print(sim.data.qpos)
    viewer.render()
    if t > 100 and os.getenv('TESTING') is not None:
        break
