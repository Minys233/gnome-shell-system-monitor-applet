#!/bin/bash

set -e

mkdir -pv ~/.ssh
ssh-keyscan github.com >> ~/.ssh/known_hosts

git remote add upstream git@github.com:paradoxxxzero/gnome-shell-system-monitor-applet.git
git fetch upstream
git rebase upstream/master || {
    echo "Couldn't rebase against upstream :(. Please rebase manually."
    exit 1
}
git push --force origin master
