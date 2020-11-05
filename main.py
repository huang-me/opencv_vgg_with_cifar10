from mainwindow import Ui_MainWindow
from PyQt5 import QtWidgets
import matplotlib.pyplot as plt
import numpy as np
import pickle
import sys

class MainWindow(QtWidgets.QMainWindow):
	def __init__(self):
		super(MainWindow, self).__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		# CONNECT ALL BUTTONS
		self.ui.BTN_SHOWIMGS.clicked.connect(self.showimg)

	def showimg(self):
		key = ['airplane', 'automobile', 'bird', 'cat', \
				'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
		with open('cifar-10-batches/data_batch_1', 'rb') as f:
			dic = pickle.load(f, encoding='bytes')
		photos = dic[b'data']
		labels = dic[b'labels']
		photos = photos.reshape(10000, 3, 32, 32) \
			.transpose(0, 2, 3, 1) \
			.astype('uint8')
		fig, axes = plt.subplots(2, 5, figsize=(8, 8))
		for i in range(2):
			for j in range(5):
				k = np.random.choice(range(len(photos)))
				axes[i][j].set_axis_off()
				axes[i][j].title.set_text(key[labels[k:k+1][0]])
				axes[i][j].imshow(photos[k:k+1][0])
		plt.show()


if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	sys.exit(app.exec_())
