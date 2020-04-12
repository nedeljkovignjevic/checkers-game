# Checkers game
Implementation of checkers (draughts) strategy board game with AI based bot

![check](https://user-images.githubusercontent.com/54076398/78457052-dac23c80-76a7-11ea-8d28-89a322a5bdc7.jpg)

This project is intended to showcase the ability of neural networks to learn to play a game of checkers.</br>
The trained network is used to guide a search algorithm - minimax with alpha-beta pruning</br>
to select the most promising moves in games.</br>

Neural network is used for evaluating the board state, it takes board state as input and outputs value between -1 and 1</br>
(values close to -1 -> white wins, values close to 1 -> black wins). AlphaZero introduced this as "value network".</br></br>
Currently, neural network is just MLP (multilayer perceptron) model with 6 hidden layers:</br>
-> 32 neurons for input layer | 64, 64, 128, 128, 256, 256 for hidden layers and 1 neuron for output layer
</br></br>
I'm working on temporal difference learning method (TD leaf) that seems way better then MLP atm</br>
(need some time to fully-train the model).</br></br>
Main idea is to use supervised learning to (pre)train some model and then to improve that model with self-play, what DeepMind did with AlphaZero.
</br></br>

## Dataset used for training
 -> http://www.fierz.ch/download.php
 
 About 20000 games, results are mostly draw (about 14000) - not so great for neural nets but i can't find better one atm.
 </br></br>

## Requirements
1. python 3
2. python-chess
3. flask
4. numpy
5. pytorch
<br /><br />

## Usage
```
1. python main.py  # runs web server on localhost:5000
2. Web browse to localhost:5000

At this phase game does not support (interface) validation and multiple jumps so dont use it right now :)
Console version is fully featured (it supports validation and multiple jumps)
```

## References
- Dataset -> http://www.fierz.ch/download.php
- Format -> http://www.bobnewell.net/filez/reinfeld2ndedition.pdf
- ML update -> http://www.bobnewell.net/nucleus/checkers.php?itemid=1177
- TD -> https://www.researchgate.net/publication/221185124_Temporal_Difference_Approach_to_Playing_Give-Away_Checkers
- TD -> http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.80.6366&rep=rep1&type=pdf
- https://www.researchgate.net/publication/3302690_Evolving_neural_networks_to_play_checkers_without_expert_knowledge
