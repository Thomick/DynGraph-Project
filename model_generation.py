import random
import utils
import numpy as np

def generate_edge_markovian(nb_nodes,p,d,duration):
    contacts_splitted = []
    current_links = [[False]*nb_nodes for _ in range(nb_nodes)]
    for t in utils.progressbar(range(duration),"    "):
        for i in range(nb_nodes):
            for j in range(i+1, nb_nodes):
                if current_links[i][j]:
                    if random.random() < d:
                        contacts_splitted.append([t,i,j,1])
                        current_links[i][j] = False
                else:
                    if random.random() < p:
                        contacts_splitted.append([t,i,j,0])
                        current_links[i][j] = True
    return contacts_splitted

def generate_connection_dependant_model(nb_nodes,p_con,d_con,p_dis,d_dis,duration):
    contacts_splitted = []
    current_graph = np.zeros((nb_nodes,nb_nodes))
    for t in utils.progressbar(range(duration),"    "):
        graph_2 = np.matmul(current_graph,current_graph)
        for i in range(nb_nodes):
            for j in range(i+1, nb_nodes):
                if current_graph[i,j] > 0:
                    if graph_2[i,j] > 0:
                        if random.random() < d_con:
                            contacts_splitted.append([t,i,j,1])
                            current_graph[i,j] = 0
                    else:
                        if random.random() < d_dis:
                            contacts_splitted.append([t,i,j,1])
                            current_graph[i,j] = 0
                else:
                    if graph_2[i,j] > 0:
                        if random.random() < p_con:
                            contacts_splitted.append([t,i,j,0])
                            current_graph[i,j] = 1
                    else:
                        if random.random() < p_dis:
                            contacts_splitted.append([t,i,j,0])
                            current_graph[i,j] = 1
    return contacts_splitted