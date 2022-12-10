import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 

#define figure and axes
fig, ax = plt.subplots()

#create values for table
table_data=[
    ["Y", 0,1,2],
    ["Probability",0.58,0.23,0.11]
    
]

#create table
table = ax.table(cellText=table_data, loc='center')

#modify table
table.set_fontsize(14)
table.scale(1,4)
ax.axis('off')

#display table
plt.show()
