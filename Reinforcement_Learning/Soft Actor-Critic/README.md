# Soft Actor-Critic (SAC)

## Overview
Soft Actor-Critic (SAC) is an advanced reinforcement learning (RL) algorithm that optimizes both efficiency and stability. It is an off-policy, model-free algorithm that combines maximum entropy reinforcement learning with actor-critic methods, allowing it to achieve state-of-the-art performance on continuous control tasks.

Key features of SAC:
- **Off-policy training** enables efficient sample reuse.
- **Entropy maximization** encourages exploration and robustness.
- **Stability** due to two Q-networks (Double Q-learning) and target smoothing.

## Installation
To set up SAC, install the necessary dependencies:

```bash
pip install gym numpy torch stable-baselines3
```

If you want to use Mujoco-based environments:

```bash
pip install mujoco-py
```

## Usage
### Training SAC on OpenAI Gym Environment
To train an agent using SAC on a Gym environment like `Pendulum-v1`, run:

```python
import gym
from stable_baselines3 import SAC

# Create environment
env = gym.make("Pendulum-v1")

# Instantiate the SAC agent
model = SAC("MlpPolicy", env, verbose=1)

# Train the agent
model.learn(total_timesteps=100000)

# Save the model
model.save("sac_pendulum")
```

### Loading and Evaluating the Trained Model

```python
# Load the model
model = SAC.load("sac_pendulum")

done = False
obs = env.reset()
while not done:
    action, _states = model.predict(obs)
    obs, reward, done, _ = env.step(action)
    env.render()
```

## Theoretical Background
SAC optimizes a trade-off between maximizing reward and entropy. The objective function is:

\[ J(\pi) = \sum_t \mathbb{E}_{(s_t, a_t) \sim \rho_\pi} \left[ r(s_t, a_t) + \alpha \mathcal{H}(\pi(\cdot | s_t)) \right] \]

Where:
- \( \mathcal{H}(\pi(\cdot | s_t)) \) represents entropy to encourage exploration.
- \( \alpha \) is the temperature parameter controlling the exploration-exploitation balance.

### Components of SAC:
1. **Actor Network**: Learns a stochastic policy.
2. **Critic Networks (Two Q-functions)**: Estimate action-value functions to mitigate overestimation.
3. **Entropy Regularization**: Encourages diverse policy learning.
4. **Target Networks**: Stabilize training by smoothing Q-value updates.

## References
- Haarnoja, T., Zhou, A., Abbeel, P., & Levine, S. (2018). [Soft Actor-Critic Algorithms and Applications](https://arxiv.org/abs/1812.05905)
- OpenAI Gym: https://gym.openai.com/
- Stable-Baselines3: https://github.com/DLR-RM/stable-baselines3

## License
This project is licensed under the MIT License.

