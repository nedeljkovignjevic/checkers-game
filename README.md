# Checkers game
Implementation of checkers (draughts) strategy board game with AI based bot

![check](https://user-images.githubusercontent.com/54076398/78457052-dac23c80-76a7-11ea-8d28-89a322a5bdc7.jpg)
</br></br>

## Dataset used for training
 -> http://www.fierz.ch/download.php
 
 About 20000 games, results are mostly draw (about 14000) - not so great dataset for neural nets but i can't find better one.
 Currently AI bot (CNN) is pretty bad so heuristic value is used for evalution.  
 Need to try some other options (reinforcement learning, temporal difference learning, neuroevolution)
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
At this phase game does not support (interface) validation and multiple jumps so dont use it right now :)
1. python main.py  # runs web server on localhost:5000
2. Web browse to localhost:5000
```

## References
- Dataset -> http://www.fierz.ch/download.php
- Format -> http://www.bobnewell.net/filez/reinfeld2ndedition.pdf
- ML update -> http://www.bobnewell.net/nucleus/checkers.php?itemid=1177
- TD -> https://www.researchgate.net/publication/221185124_Temporal_Difference_Approach_to_Playing_Give-Away_Checkers
- TD -> http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.80.6366&rep=rep1&type=pdf
- https://www.researchgate.net/publication/3302690_Evolving_neural_networks_to_play_checkers_without_expert_knowledge
