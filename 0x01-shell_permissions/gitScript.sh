#!/bin/bash
echo $(git add .)
echo "Enter commit message"
read message
echo $(git commit -m "$message")
echo $(git push)
