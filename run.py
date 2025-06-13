# FILE: /algo_viewer/run.py

"""
Main launcher for the TradePanel application.
This script should be run from the 'algo_viewer' directory.
"""
from tradepanel.main import main

if __name__ == "__main__":
    # This calls the main function in tradepanel/main.py
    # All command line arguments are automatically passed along.
    main()