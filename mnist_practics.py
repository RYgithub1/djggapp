from sklearn import datasets, svm
from sklearn.model_selection import train_test_split



# Download data-sets.
mnist = datasets.fetch_openml('mnist_784', data_home='image/')
X = mnist.data / 255
y = mnist.target


# Divede date into for training and tests.
X_train, X_test, y_train, y_test = train_test_split(
    X, y, train_size=1000, test_size=300
)


# Learn with the training-data.
clf = svm.SVC()
clf.fit(X_train, y_train)


# Test the data with test-data.
score = clf.score(X_test, y_test)
print(score)
