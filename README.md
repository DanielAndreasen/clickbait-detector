# clickbait-detector
Small CLI to detect clickbait

# Installation
Download/clone the folder. If you want to train the data yourself, run `pip install -r requirements.txt` first.

# Usage
Simple run

    python clickbait.py -h  # See available commands
    python clickbait.py Some title of an article goes here
    python clickbait.py Some title of an article goes here -t  # To retrain the model

Press `q` to exit. It will keep asking for new article titles otherwise.

# Data
The data is from [this repository](https://github.com/bhargaviparanjape/clickbait).
