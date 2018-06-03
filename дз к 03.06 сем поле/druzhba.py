import sys
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim, logging, wget

from gensim import corpora, models, similarities
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
w = ['дружба_NOUN', 'благожелатель_NOUN', 'друг_NOUN', 'дружелюбие_NOUN', 'дружественность_NOUN', 'дружество_NOUN', 'дружок_NOUN', 'дружочек_NOUN', 'кореш_NOUN', 'подруга_NOUN', 'подруженька_NOUN', 'подружка_NOUN', 'приятель_NOUN', 'приятельница_NOUN', 'товарищ_NOUN', 'товарищество_NOUN', 'товарка_NOUN', 'дружелюбно_ADV', 'дружески_ADV', 'дружеский_ADJ', 'дружественный_ADJ', 'дружить_VERB', 'дружиться_VERB', 'дружно_ADV', 'дружный_ADJ', 'по-дружески_ADV', 'подружиться_VERB', 'по-приятельски_ADV', 'приятельский_ADJ', 'раздружиться_VERB', 'сдружить_VERB', 'сдружиться_VERB', 'удружить_VERB']
#model_url = 'http://rusvectores.org/static/models/rusvectores4/RNC/ruscorpora_upos_skipgram_300_5_2018.vec.gz'
#modelfile = wget.download(model_url)
m = 'ruscorpora_upos_skipgram_300_5_2018.vec.gz'
if m.endswith('.vec.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=False)
elif m.endswith('.bin.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=True)
else:
    model = gensim.models.Word2Vec.load(m)
model.init_sims(replace=True)

import networkx as nx

labels = ['дружба', 'благожелатель', 'друг', 'дружелюбие', 'дружественность', 'дружество', 'дружок', 'дружочек', 'кореш', 'подруга', 'подруженька', 'подружка', 'приятель', 'приятельница', 'товарищ', 'товарищество', 'товарка', 'дружелюбно', 'дружески', 'дружеский', 'дружественный', 'дружить', 'дружиться', 'дружно', 'дружный', 'по-дружески', 'подружиться', 'по-приятельски', 'приятельский', 'раздружиться', 'сдружить', 'сдружиться', 'удружить']
G = nx.Graph()
for i in range(len(labels)-1):
    if w[i] in model:
        G.add_node(i, label=labels[i])
for i in range(len(w)-1):
    for j in range(i + 1, len(w)-1):
        if w[i] in model and w[j] in model:
            sim = model.similarity(w[i],w[j])
            if sim > 0.5:
                G.add_edge(i,j, weight = sim)

nx.write_gexf(G, 'graph_file.gexf')
f = open('graph_info.txt', 'w')
print('Узлы', G.nodes())
f.write('Узлы '+str( G.nodes()))
print('Рёбра', G.edges())
f.write('\nРёбра ' + str(G.edges()))
print(G.number_of_nodes(), 'узлов')
f.write('\nУзлов '+str(G.number_of_nodes()))
print(G.number_of_edges(), 'рёбер')
f.write('\nРёбер '+str(G.number_of_edges()))
print('Радиус:')
f.write('\nРадиус компонент связности:\n')
components = list(nx.connected_component_subgraphs(G))
for comp in sorted(components, key=lambda c: c.size(), reverse=True):
    print(nx.radius(comp))
    f.write(str(nx.radius(comp))+'\n')
print('Центральные вершины:')
f.write('Центральные вершины:\n')
deg = nx.degree_centrality(G)
for nodeid in sorted(deg, key=deg.get, reverse=True):
    if nodeid<=len(labels):
        print(nodeid, labels[nodeid])
        f.write(str(nodeid)+' '+labels[nodeid])
        f.write('\n')
print('Кластерный коэффициент:')
print (nx.average_clustering(G))
f.write('Кластерный коэффициент:\n'+str(nx.average_clustering(G)))
print(nx.transitivity(G))
f.write('\n'+str(nx.transitivity(G)))
f.close()

import matplotlib.pyplot as plt

pos=nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_color='red', node_size=10) 
nx.draw_networkx_edges(G, pos, edge_color='blue')
nx.draw_networkx_labels(G, pos, font_size=14, font_family='Arial')
plt.axis('off') 
plt.show()

        
