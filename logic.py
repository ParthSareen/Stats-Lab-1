import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math

def organize_data(data):
    time = []
    for line in data:
        line = line.split()
        if len(line) == 8:
            try:
                time.append(float(line[6].split('time=')[1]))
            except:
                print(line[6])
    return time

def plot_histogram(data_list):
    x = np.array(data_list)
    mu = np.mean(x)
    variance = np.var(x, dtype=np.float64)
    sigma = math.sqrt(variance)

    fig, ax = plt.subplots()
    num_bins = 20
    n, bins, patches = ax.hist(x, num_bins, density=1)

    y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
    ax
    ax.plot(bins, y, '--')
    ax.set_xlabel('Time in ms')
    ax.set_ylabel('Relative Frequency')
    ax.set_title(r'Histogram of Pinging Eduroam or smth')
    fig.tight_layout()
    plt.show()
