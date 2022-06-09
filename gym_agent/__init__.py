from gym.envs.registration import register
register(
    id='model-v0',
    entry_point='gym_agent.envs:WorldEnv',
    max_episode_steps=1000,
)
