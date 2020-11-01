import numpy as np
import matplotlib.pyplot as plt

train_acc = [61.073,86.020,90.023,91.817,93.047,93.993,94.880,95.217,95.707,96.300]
val_acc = [43.338,84.794,86.971,89.603,89.765,90.809,91.132,92.765,91.926,91.279]
epochs = np.arange(1,11,1)

line1,line2 = plt.plot(epochs, train_acc, 'r', val_acc, 'b')
plt.legend([line1, line2], ['train', 'validation'])
plt.gca().invert_yaxis()
plt.title('accuracy vs epochs')
plt.show()
