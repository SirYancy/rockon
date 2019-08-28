import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# datafile = "data/data_edit.csv"
datafile = "data/Team16_RockOn2019_Raw.csv"

time_label = 'Time Stamp (ms)'
accel_low_x = ' Accel Low X'
accel_low_y = ' Accel Low Y'
accel_low_z = ' Accel Low Z'

accel_med_x = ' Accel Med X'
accel_med_y = ' Accel Med Y'
accel_med_z = ' Accel Med Z'

accel_high_z = ' Accel Med X'

temp = ' Temp (deg C)'
press = ' Pres (Pa)'
geiger = ' Geiger (counts)'
humidity = ' Humidity'

gyro_x = ' Gyro X'
gyro_y = ' Gyro Y'
gyro_z = ' Gyro Z'

datatypes = {
    time_label : np.int32,
    accel_low_x: np.int32,
    accel_low_y: np.int32,
    accel_low_z: np.int32,
    accel_med_x: np.int32,
    accel_med_y: np.int32,
    accel_med_z: np.int32,
    accel_high_z: np.int32,
    temp: np.int32,
    press: np.int32,
    geiger: np.int32,
    humidity: np.int32,
    gyro_x: np.int32,
    gyro_y: np.int32,
    gyro_z: np.int32,
}

columns = ['Time Stamp (ms)',
           ' Accel Low X',
           ' Accel Low Y',
           ' Accel Low Z',
           ' Accel Med X',
           ' Accel Med Y',
           ' Accel Med Z',
           ' Accel High Z',
           ' Temp (deg C)',
           ' Pres (Pa)',
           ' Geiger (counts)',
           ' Humidity',
           ' Gyro X',
           ' Gyro Y',
           ' Gyro Z']
data = pd.read_csv(datafile, dtype=datatypes)

time_array = data[time_label].values
x_array = data[accel_low_x].values
y_array = data[accel_low_y].values
z_array = data[accel_low_z].values
geiger_array = data[geiger].values

# plt.plot(time_array, x_array)
plt.plot(time_array, geiger_array)

plt.show()