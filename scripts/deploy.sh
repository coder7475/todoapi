#!/bin/bash

# Navigate to your FastAPI application directory
cd ~/todoapi || exit

# Set up SSH agent for repository access (if needed)
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/tp

# Update the code from git
git checkout main
git pull

echo "Installing dependencies"
# Using pip and virtualenv (standard Python approach)
source venv/bin/activate
pip install -r requirements.txt

echo "Restarting services"
# If using systemd
sudo systemctl restart todoapi

# If using Gunicorn behind Nginx
sudo systemctl reload nginx

echo "Deployment complete"
echo "API available at: https://api.yourdomain.com"
