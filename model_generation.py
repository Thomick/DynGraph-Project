import random

def generate_edge_markovian(nb_nodes,p,d,duration):
    contacts_splitted = []
    current_links = [[False]*nb_nodes for _ in range(nb_nodes)]
    for t in range(duration):
        for i in range(nb_nodes):
            for j in range(i+1, nb_nodes):
                if current_links[i][j]:
                    if random.random() < p:
                        contacts_splitted.append([t,i,j,0])
                else:
                    if random.random() < d:
                        contacts_splitted.append([t,i,j,1])
    return contacts_splitted
