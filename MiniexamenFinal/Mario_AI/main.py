# -*- coding: utf-8 -*-
from main_mario import deploy

def main():
    "--------Training---------"
    # deploy(num_episodes=1000, training_mode=True, pretrained=False, mario_world_level='2-2')
    "-------Test_learn--------"
    deploy(num_episodes=100, training_mode=False, pretrained=True, mario_world_level='2-2')

main()