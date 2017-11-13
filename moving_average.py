import numpy as np
import pandas as pd
import os
DATA_DIR =  "data/djia_20150101_20171101/"

class MovingAverage(object):
    def __init__(self, directory, wealth):
        self.directory = directory
 

        self.assets = [f.split(".")[0].upper() for f in os.listdir(directory)]
        self.stocks = {s.lower(): pd.read_csv(directory+s.lower()+".csv") for s in self.assets}
        self.moving_averages = {} 
        self.decisions = {}
             
    def compute_moving_averages(self, N=100): 
        for stock in self.stocks:
            self.moving_averages[stock] = pd.rolling_mean(
                self.stocks[stock]['adj_open'],
                window=N
            )

    def decide_to_buy(self, slack=1.0):
        for stock in self.stocks:
            self.decisions[stock] = np.greater(
                self.stocks[stock]['adj_open'],
                (slack * self.moving_averages[stock])
            )

    def run(self): 
        self.compute_moving_averages()
        self.decide_to_buy()
        for stock in self.stocks:
            pass


expert = MovingAverage(DATA_DIR, 10000)         
expert.run()
