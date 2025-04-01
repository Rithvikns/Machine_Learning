# Explanation of the code
The Python program in the implementation for the soft actor critic explanation is provided here.

## Installing Libraries
```console
pip install stable_baseline3
pip install SAC
pip install gym
```

## Importing Libraries

- The script starts by importing necessary libraries such as gym, torch, numpy, and matplotlib.

- stable_baselines3 is used to implement the Soft Actor-Critic (SAC) algorithm.

- Google Colab’s files module is used to download the trained model.

## Setting Up the Environment

- The environment Pendulum-v1 is initialized using make_vec_env().

- This environment is continuous-action based, making it a good testbed for SAC.

- The script also checks if a GPU is available for training to accelerate computation.

## Initializing the SAC Model

- The SAC algorithm is initialized with the "MlpPolicy", meaning it uses a feedforward neural network for function approximation.

- The training logs are directed to TensorBoard for monitoring progress.

## Training the Agent

- The agent is trained for 100,000 timesteps using .learn().

- During training, the agent interacts with the environment, optimizing its policy to maximize rewards while balancing exploration via entropy.

## Saving and Downloading the Trained Model

- The trained SAC model is saved as sac_pendulum.zip.

- In Google Colab, the script automatically downloads the model so it can be reused later.

## Evaluating the Trained Agent

- The model is tested on the environment for 5 episodes to assess its performance.

- The script computes the mean and standard deviation of episode rewards to measure consistency.

## Plotting Training Progress

- The script extracts TensorBoard logs and plots the mean episode reward over training steps.

- This helps visualize learning progress and convergence.

## Visualizing the Agent’s Behavior

- The trained agent interacts with the environment for a few steps.

- It renders the environment to showcase how the agent behaves after training.

- This step-by-step structure ensures that SAC is implemented efficiently while being fully c

# Understanding What’s Happening in Training

## What is the input?

- The input to the model is the state of the environment (Pendulum-v1).

- The state includes information about the pendulum, such as angle, angular velocity, and torque applied.

- The model takes this state and decides how much force to apply to balance the pendulum.

## What is the model trying to do?

- The model is learning to control the pendulum so that it remains upright (instead of swinging randomly).

- It does this by adjusting the amount of force applied at each step.

- The goal is to maximize rewards, which means stabilizing the pendulum in an upright position.

## Breaking Down the Training Log
```console
Training SAC agent...
Logging to ./sac_tensorboard/SAC_1
---------------------------------
| rollout/           |          |
|    ep_len_mean     | 200      |
|    ep_rew_mean     | -1.3e+03 |
| time/              |          |
|    episodes        | 4        |
|    fps             | 34       |
|    time_elapsed    | 23       |
|    total_timesteps | 800      |
| train/             |          |
|    actor_loss      | 20.4     |
|    critic_loss     | 0.301    |
|    ent_coef        | 0.812    |
|    ent_coef_loss   | -0.34    |
|    learning_rate   | 0.0003   |
|    n_updates       | 699      |
---------------------------------
```

Metric	                                 Meaning
-------------------------------------------------------------------------------------------------
ep_len_mean = 200	            |     On average, an episode lasts 200 timesteps (max allowed for Pendulum-v1).
ep_rew_mean = -1300	          |     The average reward per episode is -1300 (lower means the agent is still learning). A perfect agent would have a higher reward.
episodes = 4	                |     The agent has completed 4 episodes so far.
fps = 34	                    |     Training speed: 34 frames per second.
time_elapsed = 23	            |     The model has been training for 23 seconds.
total_timesteps = 800	        |     The agent has interacted with the environment 800 times.

4. What is happening with the loss values?
Loss Metric	Meaning
actor_loss = 20.4	The actor network is still adjusting its policy (a high value means it's still exploring).
critic_loss = 0.301	The critic network is stabilizing its value predictions (low loss is good).
ent_coef = 0.812	The entropy coefficient controls exploration vs. exploitation (higher means more exploration).
ent_coef_loss = -0.34	The model is slightly reducing entropy, meaning it's starting to exploit learned behaviors.
learning_rate = 0.0003	The rate at which the model is learning.
n_updates = 699	The model has updated its parameters 699 times so far.
What is the model learning here?
At this point, the agent is still in the early stages of training.

The reward is very negative (-1300), meaning the agent has not yet learned good control.

Over time, as actor loss decreases and critic loss stabilizes, the agent will start making better decisions, and rewards will improve.
