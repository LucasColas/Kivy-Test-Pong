

import gym

#
#pip install gym
#pip install gym[box2d]
#env = gym.make("BipedalWalker-v2")
env = gym.make("BipedalWalker-v3", render_mode="human")

observation = env.reset()

#print(observation)
print("action space : ", env.action_space) #Box(-1.0, 1.0, (4,), float32)
print("action space shape : ", env.action_space.shape)
"""
for _ in range(1000):
    observation, reward, terminated, truncated, info = env.step(env.action_space.sample())

    if terminated or truncated:
        observation, info = env.reset()



for i in range(20):
    terminated, truncated = False, False
    while not terminated and not truncated:
        observation, reward, terminated, truncated, info = env.step(env.action_space.sample())

    env.reset()
"""
