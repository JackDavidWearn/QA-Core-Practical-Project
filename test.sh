#!/bin/bash
sudo apt update && sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venv
source venv/bin/activate
pip3 install -r test_requirements.txt

declare -a services=(front-end cardvalue-api cardsuit-api card-api)
for dir in "${services[@]}"; do
  cd ${dir}
  python3 -m pytest -p no:warnings --cov=application term-missing --cov-report=html
  cd ..
done