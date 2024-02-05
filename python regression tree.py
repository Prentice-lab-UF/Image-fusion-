# -*- coding: utf-8 -*-
"""
Code used to construct the regression tree model
"""

import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
 
# input IMS data 
IMS= pd.read_csv(r"z:\Liang\matlab\12-22-2022 cory 250\IMS_flat.csv")

# input the H&E data (with 120 features) and select the number of H&E features(the example here is using 30 features)
HE= pd.read_csv(r"z:\Liang\matlab\12-22-2022 cory 250\HE_flat_low.csv")
HE_30 = HE.iloc[:,:30]
X= np.float32(HE_30.values)
Y= np.float32(IMS.values)

# create a regressor object, n_estimators refers to the number of decision trees included in model
regressor = RandomForestRegressor(n_estimators = 1, random_state = 0) 

# fit the regressor with X and Y data
regressor.fit(X, Y)

#generation of and saving predicted image 
result=regressor.predict(X)
np.savetxt(r"z:\Liang\matlab\12-22-2022 cory 250\Cory_tree_low_30_100.csv",result,fmt='%.4e',delimiter=',')