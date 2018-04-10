import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv('info.csv')
df[:2].plot()
plt.show()
