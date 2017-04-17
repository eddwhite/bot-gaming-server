#!/bin/bash

# check if base-con exists
lxc list base-con -c n --format json

# create base container
lxc launch ubuntu:16.04 base-con

# apt-get update, apt-get upgrade
# apt-get install python

lxc stop base-con

lxc profile copy default game-bot

lxc profile set game-bot limits.memory 80%
lxc profile set game-bot limits.cpu.allowance 80%

lxc profile apply base-con game-bot