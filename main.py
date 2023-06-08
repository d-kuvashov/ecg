import matplotlib.pyplot as plt
import wfdb


record = wfdb.rdrecord('C:/Users/ctaka/PycharmProjects/wfdb-python/sample-data/a103l')
plt.plot(record.p_signal[0:500,0])
plt.plot(record.p_signal[500:1000,1])
plt.plot(record.p_signal[49500:50000,2])
plt.show()