
import torch
import pickle
import gym_super_mario_bros
import numpy as np
import matplotlib.pyplot as plt
from tqdm import tqdm
from modules.image_tools import get_env_fix
from modules.agents_DQN import DQNAgent


def get_max_episode(reward_list):
    max_reward = int(max(reward_list))
    return {"max_reward":max_reward,
            "max_episode":reward_list.index(max_reward)+1}


def deploy(num_episodes, training_mode, pretrained, mario_world_level):
    path_training_info = "training_data/"+mario_world_level+"_"
    env = gym_super_mario_bros.make('SuperMarioBros-'+mario_world_level+'-v0')
    env = get_env_fix(env)  # Wraps the environment so that frames are grayscale
    observation_space = env.observation_space.shape
    action_space = env.action_space.n
    agent = DQNAgent(state_space=observation_space,
                     action_space=action_space,
                     max_memory_size=30000,
                     batch_size=32,
                     gamma=0.90,
                     lr=0.00025,
                     dropout=0.,
                     exploration_max=1.0,
                     exploration_min=0.02,
                     exploration_decay=0.99,
                     double_dq=True,
                     pretrained=pretrained,
                     path_level=path_training_info)

    graph_prop = int((num_episodes/10000)*500)
    env.reset()
    total_rewards = []

    for ep_num in tqdm(range(num_episodes)):
        state = env.reset()
        state = torch.Tensor([state])
        total_reward = 0
        steps = 0
        while True:
            if not training_mode:
                env.render()
            action = agent.act(state)
            steps += 1

            state_next, reward, terminal, info = env.step(int(action[0]))
            total_reward += reward
            state_next = torch.Tensor([state_next])
            reward = torch.tensor([reward]).unsqueeze(0)

            terminal = torch.tensor([int(terminal)]).unsqueeze(0)

            if training_mode:
                agent.remember(state, action, reward, state_next, terminal)
                agent.experience_replay()

            state = state_next
            if terminal:
                break
        total_rewards.append(total_reward)
        if (ep_num + 1) % 10 == 0:
            max_ep_rew = get_max_episode(total_rewards)
            print(" MAX Reward ===>",max_ep_rew["max_reward"],
                  "in episode",max_ep_rew["max_episode"])
        num_episodes += 1

    if training_mode:
        print("\nSaving data ......")
        with open(path_training_info+"ending_position.pkl", "wb") as f:
            pickle.dump(agent.ending_position, f)
        with open(path_training_info+"num_in_queue.pkl", "wb") as f:
            pickle.dump(agent.num_in_queue, f)
        with open(path_training_info+"total_rewards.pkl", "wb") as f:
            pickle.dump(total_rewards, f)
        if agent.double_dq:
            torch.save(agent.local_net.state_dict(), path_training_info+"dq1.pt")
            torch.save(agent.target_net.state_dict(), path_training_info+"dq2.pt")
        else:
            torch.save(agent.dqn.state_dict(), path_training_info+"dq.pt")
        torch.save(agent.STATE_MEM,  path_training_info+"STATE_MEM.pt")
        torch.save(agent.ACTION_MEM, path_training_info+"ACTION_MEM.pt")
        torch.save(agent.REWARD_MEM, path_training_info+"REWARD_MEM.pt")
        torch.save(agent.STATE2_MEM, path_training_info+"STATE2_MEM.pt")
        torch.save(agent.DONE_MEM,   path_training_info+"DONE_MEM.pt")

    env.close()
    max_ep_rew = get_max_episode(total_rewards)
    print(" MAX Reward ===>",max_ep_rew["max_reward"],
          "in episode",max_ep_rew["max_episode"])
    
    if num_episodes > graph_prop:
        plt.title("Episodes trained vs. Average Rewards")
        plt.plot([0 for _ in range(graph_prop)] +
                 np.convolve(total_rewards, np.ones((graph_prop,))/graph_prop, mode="valid").tolist())
        plt.show()
