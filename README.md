# Python3 JetPack Joyride <!-- omit in toc -->

## Table of Contents <!-- omit in toc -->
- [Running](#running)
- [Controls](#controls)
- [Requirements Implemented](#requirements-implemented)
  - [OOPS Concepts](#oops-concepts)
  - [Movement](#movement)
  - [Background](#background)
  - [Enemy](#enemy)
  - [Obstacles](#obstacles)
  - [Score and Lives](#score-and-lives)
  - [Power-Ups](#power-ups)
    - [Speed boost](#speed-boost)
    - [Shield](#shield)
  - [Bonus](#bonus)

## Running
- Module dependencies that may need to be installed:
  * time
  * colorama
  * random
- Use `pip3 install <module_name>` to install any, if required.
- Run game using `python3 main.py`

## Controls

| Key   | Function        |
| ----- | --------------- |
| W     | Up Movement     |
| A     | Left Movement   |
| D     | Right Movement  |
| Q     | Quit game       |
| M     | Shoot Bullet    |
| E     | Speed UP!
| V     | Activate Shield |

## Requirements Implemented

### OOPS Concepts

- Inheritance
  - Mando and Devil classes are derived from Carbon Class
- Polymorphism
  - Devil class has a method render() which overrides Carbon.render()
- Encapsulation
  - Class based approach to construct the game
- Abstraction
  - Mechanisms like move, gravity, bullets, etc. are implemented as defined methods.

### Movement

- W for UP
- A for LEFT
- D for RIGHT
- M for Bullets
- Gravity

### Background

- Progressive screen
- Scenery, obstacles change as player moves
- No going back!
- Cave-like

### Enemy

- Demon (Boss Enemy): Follows players coordinates and shoots a barrage of bullets at Mando, each bullet taken costs 1 life. Can sustain 20 bullets before dying.

### Obstacles

- Fire Beams will incinerate Mando on contact costing 1 life.
- Magnets will attempt to stagger Mando by attracting him.

### Score and Lives

- Score is increased by 1 when player collects a coin
- Player has 15 lives (too much? met the boss yet?)

### Power-Ups

#### Speed boost

- Game speed will be increased by 33%
- Lasts for 5s

#### Shield

- Lasts for 10s
- Passes through beams and enemies, but can still collect coins

### Bonus

- Implemented Colors