import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv

df=pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
print("Population Mean:- ",statistics.mean(data))
mean=statistics.mean(data)
def setup_random_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index=random.randint(0,len(data))
        value = data[random_index]
        dataset.append(value)
    mean=statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df],["reading_time"], show_hist=False)
    fig.show()

def setup():
    data_list=[]
    for i in range(0,50):
        setup_random= setup_random_mean(10)
        data_list.append(setup_random)
    show_fig(data_list)
    print("Sampling Mean :-", statistics.mean(data_list))

    mean3=statistics.mean(data_list)
    std_deviation3=statistics.stdev(data_list)

    z_score2=(mean3-mean)/std_deviation3
    print("Z-Score :- " + str(z_score2))
setup()

