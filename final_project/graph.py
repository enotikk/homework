import re
import os
from flask import Markup
import sys
import networkx as nx
import matplotlib.pyplot as plt

def is_rus_word(word):
    r = re.findall("[а-яА-Я\-]+", word)
    if len(r) == 1 and r[0] == word:
        return True
    else:
        return False
def load_data():
    with open("data.txt", "r", encoding="utf-8") as f:
        return loads(f.read())
def graph_info(text):
    li = lemmatize(text)
    new = []
    for di in li:
        lemma = di['lemma']
        lemma_word = lemma.split("=")[0]
        if is_rus_word(di['word']):
            new.append(lemma_word)
    G = nx.Graph()
    labels = []
    if not new[0] in labels:
        labels.append(new[0])
        G.add_node(labels.index(new[0]), label=new[0])
    if not new[1] in labels:
        labels.append(new[1])
        G.add_node(labels.index(new[1]), label=new[1])
    G.add_edge(0,1)
    for i in range(len(new)-3):
        if not new[i+2] in labels:
            labels.append(new[i+2])
            G.add_node(labels.index(new[i+2]), label=new[i+2])
        G.add_edge(labels.index(new[i+1]),labels.index(new[i+2]))
        G.add_edge(labels.index(new[i]),labels.index(new[i+2]))

    pos=nx.spring_layout(G)
    nx.draw_networkx_nodes(G, pos, node_color='red', node_size=10) 
    nx.draw_networkx_edges(G, pos, edge_color='blue')
    plt.axis('off') 
    plt.show()    
    plt.savefig('figure.png')
    a = []
    a.append('Узлов '+str(G.number_of_nodes()))
    a.append('Рёбер '+str(G.number_of_edges()))
    a.append('Радиус '+str(nx.radius(G)))
    a.append('Центральные вершины:')
    deg = nx.degree_centrality(G)
    for nodeid in sorted(deg, key=deg.get, reverse=True):
        if nodeid<=len(labels):
            a.append(str(nodeid)+' '+labels[nodeid])
    a.append('Кластерный коэффициент:\n'+str(nx.average_clustering(G)))
    a.append(str(nx.transitivity(G)))
    return '\n'.join(a)
    
    
def lemmatize(text):
    with open("input.txt", "w", encoding='utf-8') as f:
        f.write(text)
    os.system(r"mystem.exe -i input.txt output.txt")
    with open("output.txt", "r", encoding='utf-8') as f:
        s = f.read()
    regLem = re.compile('([^{]+{.*?)}', re.DOTALL)
    li = regLem.findall(s)
    result = []
    for n in li:
        result.append({"lemma": n.split("{")[-1], "word": n.split("{")[0]})
    return result

