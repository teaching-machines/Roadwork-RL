#!/bin/bash
COLOR_BLUE='\033[0;34m'
COLOR_NONE='\033[0m'

for directory in sim/*; do
  if [ -d "${directory}" -a -f "${directory}/install.sh" ]; then
    echo -e "${COLOR_BLUE}==============================================================${COLOR_NONE}"
    echo -e "${COLOR_BLUE}Installing ${directory}${COLOR_NONE}"
    echo -e "${COLOR_BLUE}==============================================================${COLOR_NONE}"
    
    chmod u+x "${directory}/install.sh"
    bash "./${directory}/install.sh"
  fi
done