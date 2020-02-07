from stable_baselines.deepq.policies import MlpPolicy
from stable_baselines import DQN

from spy_vs_spy.env.spy_vs_spy_ma_env import RedSpyEnv

if __name__ == '__main__':

    env = RedSpyEnv('red-spy', 'localhost:50051')
    model = DQN(MlpPolicy, env, verbose=1)
    model.learn(total_timesteps=10000)

    for i_episode in range(20):
        observation = env.reset()
        for t in range(100):
            # env.render()
            print("Observation of step {}: {}".format(t, observation))
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            if done:
                print("Episode finished after {} timesteps".format(t + 1))
                break

    env.close()