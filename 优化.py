from sklearn import preprocessing, neighbors, linear_model, svm
from sklearn.decomposition import PCA
from sklearn.model_selection import train_test_split, cross_val_score

from 工具 import createData1
import matplotlib.pyplot as plt


# 计算数据集得分
def score(n_neighbors=2):
    pca = PCA(n_components=1)

    X, y = createData1()
    X = pca.fit_transform(X)
    preprocessing.scale(X)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

    # clf = svm.SVC(kernel='linear', C=0.01)
    knn = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors)
    # knn = svm.SVC()
    knn.fit(X_train, y_train)
    p_test = knn.predict(X_test)
    print(knn.score(X_test, y_test))


# 选出最佳参数，k值（n_neighbors）
def pp():
    k_scores = []

    x, y = createData1()
    for k in range(1, 10):
        knn = neighbors.KNeighborsClassifier(n_neighbors=k)
        scores = cross_val_score(knn, x, y, cv=10, scoring='accuracy')  # for classification
        k_scores.append(scores.mean())
    plt.plot(range(1, 10), k_scores)
    plt.xlabel('Value of K for KNN')
    plt.ylabel('Cross-Validated Accuracy')
    plt.show()


print(score())
