
import math

from mujoco_py import load_model_from_path, MjSim, MjViewer
from mujoco_py.modder import TextureModder

import os

model = load_model_from_path("gym_agent/assets/model.xml")
sim = MjSim(model)
viewer = MjViewer(sim)
t=0

while True:
    #   sim.data.ctrl[1] = math.cos(t / 10.) * 0.01
    sim.step()
    viewer.render()
    if t > 100 and os.getenv('TESTING') is not None:
        break



#env = gym.make('model-v0')
#env.reset()

#for i in range(1000):
#    env.render()
#    action = [0, 0, 0, 0]
#    state, reward, done, info = env.step(action)
#    print(state)
