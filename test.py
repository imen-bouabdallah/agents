#
#using mujoco
#
#
#
#
import math
import mujoco


import os


#load the model
model =  mujoco.MjModel.from_xml_path("gym_agent/assets/model.xml")
data = mujoco.MjData(model)

ctx = mujoco.GLContext(250, 250)
ctx.make_current()
v = mujoco.MjvScene(model,5)
v.render()

while data.time <1:
    mujoco.mj_step(model, data)
    #print(data.geom_xpos)


ctx.free()





#for i in range(1000):
#    env.render()
#    action = [0, 0, 0, 0]
#    state, reward, done, info = env.step(action)
#    print(state)
