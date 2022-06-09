import numpy as np
from gym import utils
from gym import spaces
from gym.envs.mujoco import mujoco_env
from collections import defaultdict
#from gym_agent.controller.MujocoController import MJ_Controller

import os
from pathlib import Path

import random




class WorldEnv(mujoco_env.MujocoEnv, utils.EzPickle):
    def __init__(self, FILE='/gym_agent/assets/model.xml'):
        path = os.path.realpath(__file__)
        path = str(Path(path).parent.parent.parent)
        path += FILE

        mujoco_env.MujocoEnv.__init__(self, path, 5)

        utils.EzPickle.__init__(self)


        #action space, move, open door, hold key
        self.action_space = spaces.Discrete(3)
        #self.controller = MJ_Controller(self.model, self.sim, self.viewer)

    def step(self, action):
        self.do_simulation(action, self.frame_skip)
        obs = self.get_observation()
        reward = 0
        done = False

        info = {}
        return obs, reward, done, info

    def get_observation(self, show=True):
        """
        Uses the controllers get_image_data method to return an top-down image (as a np-array).
        Args:
            show: If True, displays the observation in a cv2 window.
        """
        #rgb, depth = self.controller.get_image_data(
        #width=self.IMAGE_WIDTH, height=self.IMAGE_HEIGHT, show=show
        #)
        #depth = self.controller.depth_2_meters(depth)
        observation = defaultdict()
        #observation["rgb"] = rgb
        #observation["depth"] = depth

        return observation
    def reset_model(self):
        qpos = self.init_qpos
        qvel = self.init_qvel
        self.set_state(qpos,qvel)
        return self.get_observation()

    def viewer_setup(self):
        pass

    #def render(self):
    #pass
