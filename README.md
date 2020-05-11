# DeepRL-LTLf
The repository implements a Reinforcement Learning Task on a custom environment using temporal logic specifications. The project is based on the paper "[Modular Deep Reinforcement Learning with Temporal Logic Specifications](https://arxiv.org/abs/1909.11591)" (Lim Zun Yuan et al.) using a modified Soft-Actor-Critic algorithm based on the Py-Torch implementation provided at [Py-Torch SAC](https://github.com/pranz24/pytorch-soft-actor-critic).

[Project Webpage](https://rickymexx.github.io/DeepRL-LTLf/)

<br>

## Table Of Contents
*   [The Environment](#the-environment)
*   [Results](#results)
*   [Installation](#installation)
*   [References](#references)

<br>

## The Environment
The task is performed on a custom environment developed using Gym-OpenAI and consists in the agent (the ball) going through the two circles in a specified order: bottom-left, top-right. The 6-dimensional state consists of the position and velocity along the x and y axes and two binary values (one for each circle) specifying whether the agent has gone through a circle.   

<br>

## Results
Two agents have been trained on the task: one given by the "classic" SAC algorithm with no modification, while a second one trained as described in the paper (Lim Zun Yuan et al. [1]) with a modular design that separates the task in two sub-goals. 

![Reward](/img/reward.png)
<br><br>

---------------------

We show how SAC alone (on the left) can easily reach the first goal but fails to reach the second even though the state provides the agent with the information about having reached the first circle. The modular agent (on the right), instead, is able to completely solve the specified task.


![sac_only](/img/sac_only.gif)
![sac_modular](/img/sac_modular.gif)


<br>

## Installation

<br>

### Requirements
*   [gym](https://github.com/openai/gym)
*   [TensorboardX](https://github.com/lanpa/tensorboardX)
*   [PyTorch](http://pytorch.org/)

<br>

### Installation of RAEnv

```
cd ra-gym
pip install -e .
```

### Installation of SAC

```
git clone https://github.com/pranz24/pytorch-soft-actor-critic
cp sac_modular.py pytorch-soft-actor-critic
```

### Train Classic SAC

```
cd pytorch-soft-actor-critic
python sac_modular.py --batch_size 64 --automatic_entropy_tuning True
```

### Train Modular SAC

```
cd pytorch-soft-actor-critic
python sac_modular.py --batch_size 64 --automatic_entropy_tuning True --modular
```

<br><br>

## Credits
- [Caprari Riccardo](https://github.com/RickyMexx)
- [Giacomini Emanuele](https://github.com/EmanueleGiacomini)
- [Ragno Alessio](https://github.com/spideralessio)
- [Savoia Dylan](https://github.com/dylansavoia)


<br>


## References
- Lim Zun Yuan, Mohammadhosein Hasanbeig, Alessandro Abate, and Daniel Kroening. Modular Deep Reinforcement Learning with Temporal Logic Specifications. Department of Computer Science, University of Oxford.
- Icarte, R. T., Klassen, T., Valenzano, R., & McIlraith, S. (2018, July). Using reward machines for high-level task specification and decomposition in reinforcement learning. In International Conference on Machine Learning (pp. 2107-2116).
- Camacho, A., Icarte, R. T., Klassen, T. Q., Valenzano, R., & McIlraith, S. A. (2019, August). LTL and beyond: Formal languages for reward function specification in reinforcement learning. In Proceedings of the 28th International Joint Conference on Artificial Intelligence (IJCAI) (pp. 6065-6073).
- Toro Icarte, R., Klassen, T. Q., Valenzano, R., & McIlraith, S. A. (2018, July). Teaching multiple tasks to an RL agent using LTL. In Proceedings of the 17th International Conference on Autonomous Agents and MultiAgent Systems (pp. 452-461). International Foundation for Autonomous Agents and Multiagent Systems.
- De Giacomo, G., Iocchi, L., Favorito, M., & Patrizi, F. (2019, July). Foundations for restraining bolts: Reinforcement learning with LTLf/LDLf restraining specifications. In Proceedings of the International Conference on Automated Planning and Scheduling (Vol. 29, No. 1, pp. 128-136).
- Hasanbeig, M., Yogananda Jeppu, N., Abate, A., Melham, T., & Kroening, D. (2019). DeepSynth: Automata Synthesis for Automatic Task Segmentation in Deep Reinforcement Learning. arXiv, arXiv-1911.
- Quint, E., Xu, D., Dogan, H., Hakguder, Z., Scott, S., & Dwyer, M. (2019). Formal Language Constraints for Markov Decision Processes. arXiv preprint arXiv:1910.01074.
