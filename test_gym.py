import gym
import gym_agent

env = gym.make("model-v0")
obs = env.reset()

for i in range(1000):
    env.render()
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
