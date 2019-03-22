import numpy as np
import h5py
import matplotlib.pyplot as plt
import pylab
    
class lr_utils:
    def load_dataset(self):
        train_dataset = h5py.File('datasets/train_catvnoncat.h5', "r")
        train_set_x_orig = np.array(train_dataset["train_set_x"])  # your train set features
        train_set_y_orig = np.array(train_dataset["train_set_y"][:])  # your train set labels

        test_dataset = h5py.File('datasets/test_catvnoncat.h5', "r")
        test_set_x_orig = np.array(test_dataset["test_set_x"][:])  # your test set features
        test_set_y_orig = np.array(test_dataset["test_set_y"][:])  # your test set labels

        classes = np.array(test_dataset["list_classes"][:])  # the list of classes

        train_set_y_orig = train_set_y_orig.reshape((1, train_set_y_orig.shape[0]))
        test_set_y_orig = test_set_y_orig.reshape((1, test_set_y_orig.shape[0]))

        return train_set_x_orig, train_set_y_orig, test_set_x_orig, test_set_y_orig, classes


# lr_utils = lr_utils()
# train_set_x_orig  = lr_utils.load_dataset()[0]  # train_set_x_orig is a numpy-array of shape (m_train, num_px, num_px, 3)
# train_set_y = lr_utils.load_dataset()[1]
# test_set_x_orig = lr_utils.load_dataset()[2]
# test_set_y = lr_utils.load_dataset()[3]
# classes = lr_utils.load_dataset()[4]
# m_train = train_set_x_orig.shape[0]
# m_test = test_set_x_orig.shape[0]
# num_px = train_set_x_orig.shape[1]
#
# train_set_x_orig_flatten = train_set_x_orig.reshape(m_train,-1).T
# test_set_x_orig_flatten = test_set_x_orig.reshape(m_test,-1).T
#
# print("test_set_x_orig:"+str(test_set_x_orig[0, :]))
# print ("Number of training examples: m_train = " + str(m_train))
# print ("Number of testing examples: m_test = " + str(m_test))
# print ("Height/Width of each image: num_px = " + str(num_px))
# print ("Each image is of size: (" + str(num_px) + ", " + str(num_px) + ", 3)")
# print ("train_set_x shape: " + str(train_set_x_orig.shape))
# print ("train_set_y shape: " + str(train_set_y.shape))
# print ("test_set_x shape: " + str(test_set_x_orig.shape))
# print ("test_set_y shape: " + str(test_set_y.shape))
#
# print ("train_set_x_flatten shape: " + str(train_set_x_orig_flatten.shape))
# print ("train_set_y shape: " + str(train_set_y.shape))
# print ("test_set_x_flatten shape: " + str(test_set_x_orig_flatten.shape))
# print ("test_set_y shape: " + str(test_set_y.shape))
# print ("sanity check after reshaping: " + str(test_set_x_orig_flatten[0:m_test,0]))
# print(str(m_train))

# index = 208
# plt.imshow(train_set_x_orig[index])
# pylab.show()
# print ("y = " + str(train_set_y[:, index]) + ", it's a '" + classes[np.squeeze(train_set_y[:, index])].decode("utf-8") +  "' picture.")

A = np.random.randn(4,3)
B = np.sum(A, axis = 1, keepdims = True)
print (B.shape)
