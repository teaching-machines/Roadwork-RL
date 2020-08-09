#!/bin/bash
# Install dependencies
apt-get install -y libglu1-mesa-dev libgl1-mesa-dev libosmesa6-dev xvfb ffmpeg curl patchelf libglfw3 libglfw3-dev cmake zlib1g zlib1g-dev swig

# Install OpenAI in /opt (which is meant for OS unbundled packages)
git clone https://github.com/teaching-machines/gym.git /opt/openai-gym-machineteachingio

# Install dependencies
cd /opt/openai-gym-machineteachingio
pip3 install -e '.[box2d]'