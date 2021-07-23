#!/usr/bin/env bash
# This Code Write by Mr.nope
# Instagram-Upload v1.2

if [[ "$(id -u)" -ne 0 ]]; then
  echo "Please, Run This Programm as Root!"
  echo ""
  exit 1
fi
main() {
  printf '\033]2;Instagram-Upload\a'
  clear
  echo "Setup...!"
  chmod +x run.py
  sleep 1
  clear
  echo "Installing..."
  sleep 2
  apt install python
  apt install python3
  apt install python3-pip
  pip3 install --upgrade pip
  echo ""
  echo "Finish...!"
  echo ""
  exit 1
}
main