import pandas as pd
import matplotlib.pyplot as plt
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
from matplotlib import rc

# font_path = './malgun.ttf'
# font_name = font_manager.FontProperties(
#     fname=font_path).get_name()

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus'] = False

embedding_model = Word2Vec.load('./rec_sys_model/wanted/model/post_rec_model.model')
key_word = '유연'
sim_word = embedding_model.wv.most_similar(key_word, topn=10)
print(sim_word)

vectors = []
labels = []

for label, _ in sim_word:
    labels.append(label)
    vectors.append(embedding_model.wv[label])
print(vectors[0])
print(len(vectors[0]))

df_vectors = pd.DataFrame(vectors)
print(df_vectors.head())

tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=2500)
new_value = tsne_model.fit_transform(df_vectors)
df_xy = pd.DataFrame({'words':labels,
                      'x':new_value[:, 0],
                      'y':new_value[:, 1]})
print(df_xy)
print(df_xy.shape)
df_xy.loc[df_xy.shape[0]] = (key_word, 0, 0)

plt.figure(figsize=(8, 8))
plt.scatter(0, 0, s=1500, marker='*')

for i in range(len(df_xy) - 1):
    a = df_xy.loc[[i, 10]]
    plt.plot(a.x, a.y, '-D', linewidth=1)
    plt.annotate(df_xy.words[i], xytext=(1, 1),
                 xy=(df_xy.x[i], df_xy.y[i]),
                 textcoords='offset points',
                 ha='right', va='bottom')

plt.show()