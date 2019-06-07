
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class linear_regression():
    def __init__(self):
        self.data = None
        return

    def load_data_csv(self, filename):
        self.data = pd.read_csv(filename)

        print(self.data.head())
        print(self.data.describe())
        return

    

def main():
    regressor = linear_regression()
    file = 'auto_csv.csv'

    regressor.load_data_csv(filename=file)
    return

if __name__=='__main__':
    main()
