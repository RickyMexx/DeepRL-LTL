from gym.envs.registration import register
register(id='RAEnv-v0',
    entry_point='ra_gym.envs.ra_env:RAEnv'
)