# import dataset

import pandas as pd
wd = pd.read_csv ('./file.csv', delimiter = ',')  # read warflight csv file into Pandas dataframe

print("Total WiFi AP entries: " + str(len(wd)))
wd.sample(4000)  # 4000 random networks
