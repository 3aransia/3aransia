#!/bin/zsh
# chmod +x deploy.sh
# Update software version in Setup.py first
rm -rf dist/* 
python setup.py sdist 
twine upload dist/*    
git add . 
git commit -m $1 
git push 3aransia develop 
git checkout master
git merge develop
git checkout develop
sleep 5m
cd ../3aransia.api
source venv/bin/activate   
pip install --upgrade aaransia    
pip freeze > requirements.txt
git add . 
git commit -m $1 
git push 3aransia develop 
git checkout master
git merge develop
git checkout develop
cd ../3aransia