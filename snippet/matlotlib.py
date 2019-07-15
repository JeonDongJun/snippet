# 차원축소
from sklearn.manifold import TSNE
x_embedded = TSNE(n_components=2).fit_transform(outputs)

# 2차원 그래프에 그리기
import matplotlib.pyplot as plt

plt.figure(figsize=[8,8])
xs = x_embedded[np.where(y_true == 'bug')[0], 0]
ys = x_embedded[np.where(y_true == 'bug')[0], 1]
plt.scatter(xs,ys, c='C1', label='bug')