#!/usr/bin/env bash
find ./tests ./com -type d -name "__pycache__" | xargs rm -rf
echo "ALL __pycache__ directories have been deleted."
