import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset=pd.read_csv("TCS.NS.csv")
dataset_processed=dataset.iloc[:, 1:2].values
#print(len(dataset_processed))
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler(feature_range=(0, 1))
dataset_scaled=scaler.fit_transform(dataset_processed)


features_set=[]
labels=[]
for i in range(60, 2470):
    features_set.append(dataset_scaled[i-60:i, 0])
    labels.append(dataset_scaled[i,0])
features_set, labels=np.array(features_set), np.array(labels)
features_set=np.reshape(features_set, (features_set.shape[0], features_set.shape[1], 1))

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from keras.layers import Dropout

model=Sequential()
model.add(LSTM(units=50, return_sequences=True, input_shape=(features_set.shape[1], 1)))
model.add(Dropout(0.2))
model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=50, return_sequences=True))
model.add(Dropout(0.2))

model.add(LSTM(units=50))
model.add(Dropout(0.2))

model.add(Dense(units=1))

model.compile(optimizer='adam', loss='mean_squared_error')
model.fit(features_set, labels, epochs=100, batch_size=32)

dataset_complete_test=pd.read_csv("TCS.TEST.csv")
#print(dataset_complete_test)

dataset_testing_processed=dataset_complete_test.iloc[:, 1:2].values

dataset_total=pd.concat((dataset['Open'], dataset_complete_test['Open']),axis=0)
#print(len(dataset_total))

test_inputs=dataset_total[len(dataset_total)-len(dataset_complete_test)-60:].values

test_inputs=test_inputs.reshape(-1, 1)
test_inputs=scaler.transform(test_inputs)

test_features=[]
for i in range(60, 80):
    test_features.append(test_inputs[i-60:i, 0])


test_features=np.array(test_features)
print(test_features.shape)
test_features=np.reshape(test_features,(test_features.shape[0], test_features.shape[1],1))


predictions=model.predict(test_features)
predictions=scaler.inverse_transform(predictions)
#print(predictions.shape)

plt.figure(figsize=(10,6))
plt.plot(dataset_testing_processed, color='blue', label='Actual TCS price')
plt.plot(predictions, color='red' , label='Predicted TCS stock price')
plt.title('TCS stock price prediction')
plt.xlabel('Date')
plt.ylabel('TCS Stock Price')
plt.legend()
#plt.show()