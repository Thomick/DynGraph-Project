import numpy as np
import utils

def get_avg_degree(contacts_splitted):
    duration = int(np.max(contacts_splitted[:, 0]) - np.min(contacts_splitted[:, 0]))
    degrees = [0]*duration
    current_total_degree = 0
    current_entry = 0
    for i in range(duration):
        while current_entry < contacts_splitted.shape[0] and contacts_splitted[current_entry,0] <= i:
            current_total_degree += 2 - 4*contacts_splitted[current_entry,3]
            current_entry += 1
        degrees[i] = current_total_degree
    nb_node = len(set.union(set(contacts_splitted[:, 1]), set(contacts_splitted[:, 2])))
    return np.array(degrees)/nb_node

def get_created_deleted_fraction(contacts_splitted):
    duration = int(np.max(contacts_splitted[:, 0]) - np.min(contacts_splitted[:, 0]))
    nb_node = len(set.union(set(contacts_splitted[:, 1]), set(contacts_splitted[:, 2])))
    max_edge_count = int(nb_node*(nb_node-1)/2)
    current_edge_count = 0
    fraction_created = [-1]*duration
    fraction_deleted = [-1]*duration
    current_entry = 0
    for i in range(duration):
        deleted = 0
        created = 0
        while current_entry < contacts_splitted.shape[0] and contacts_splitted[current_entry,0] <= i:
            deleted += contacts_splitted[current_entry,3]
            created += 1 - contacts_splitted[current_entry,3]
            current_entry += 1
        if current_edge_count != max_edge_count:
            fraction_created[i] = created/(max_edge_count-current_edge_count)
        if current_edge_count != 0:
            fraction_deleted[i] = deleted/current_edge_count
        current_edge_count += created - deleted
    return np.array(fraction_created),np.array(fraction_deleted)

def get_node_avg_degree(contacts_splitted):
    duration = int(np.max(contacts_splitted[:, 0]) - np.min(contacts_splitted[:, 0]))
    nb_node = len(set.union(set(contacts_splitted[:, 1]), set(contacts_splitted[:, 2])))
    mean_degrees = np.zeros(nb_node)
    degrees = np.zeros(nb_node)
    current_entry = 0
    for i in range(duration):
        while current_entry < contacts_splitted.shape[0] and contacts_splitted[current_entry,0] <= i:
            degrees[contacts_splitted[current_entry,1]-1] += 1- 2*contacts_splitted[current_entry,3]
            degrees[contacts_splitted[current_entry,2]-1] += 1- 2*contacts_splitted[current_entry,3]
            current_entry += 1
        mean_degrees += degrees/duration
    return mean_degrees

def get_unique_moving_node_count(contacts_splitted):
    duration = int(np.max(contacts_splitted[:, 0]) - np.min(contacts_splitted[:, 0]))
    unique_moving_node_count = np.zeros(duration)
    current_entry = 0
    for i in range(duration):
        moving_nodes = set()
        while current_entry < contacts_splitted.shape[0] and contacts_splitted[current_entry,0] <= i:
            moving_nodes.add(contacts_splitted[current_entry,1])
            moving_nodes.add(contacts_splitted[current_entry,2])
            current_entry += 1
        unique_moving_node_count[i] += len(moving_nodes)
    return unique_moving_node_count

def get_unique_meeting_count(contacts_splitted):
    nb_node = len(set.union(set(contacts_splitted[:, 1]), set(contacts_splitted[:, 2])))
    seen = np.zeros((nb_node,nb_node))
    move_counter = np.zeros(nb_node)
    for current_entry in range(contacts_splitted.shape[0]):
        seen[contacts_splitted[current_entry,1]-1,[contacts_splitted[current_entry,2]-1]] =1
        seen[contacts_splitted[current_entry,2]-1,[contacts_splitted[current_entry,1]-1]] =1
    return seen.sum(axis=0)

def get_per_node_average_created_deleted_fraction(contacts_splitted):
    duration = int(np.max(contacts_splitted[:, 0]) - np.min(contacts_splitted[:, 0]))
    nb_node = len(set.union(set(contacts_splitted[:, 1]), set(contacts_splitted[:, 2])))
    current_nb_link = np.zeros(nb_node)
    mean_fraction_created = np.zeros(nb_node)
    mean_fraction_deleted = np.zeros(nb_node)
    current_entry = 0
    for i in utils.progressbar(range(duration)):
        created = np.zeros(nb_node)
        deleted = np.zeros(nb_node)
        while current_entry < contacts_splitted.shape[0] and contacts_splitted[current_entry,0] <= i:
            deleted[contacts_splitted[current_entry,1]-1] += contacts_splitted[current_entry,3]
            created[contacts_splitted[current_entry,1]-1] += 1 - contacts_splitted[current_entry,3]
            deleted[contacts_splitted[current_entry,2]-1] += contacts_splitted[current_entry,3]
            created[contacts_splitted[current_entry,2]-1] += 1 - contacts_splitted[current_entry,3]
            current_entry += 1
        for j in range(nb_node):
            if current_nb_link[j] != nb_node-1:
                mean_fraction_created[j] += created[j]/(nb_node-1-current_nb_link[j])
            if current_nb_link[j] != 0:
                mean_fraction_deleted[j] += deleted[j]/current_nb_link[j]
        current_nb_link += created - deleted
    return np.array(mean_fraction_created)/duration,np.array(mean_fraction_deleted)/duration

def get_created_deleted_fraction_wconnection(contacts_splitted):
    duration = int(np.max(contacts_splitted[:, 0]) - np.min(contacts_splitted[:, 0]))
    nb_node = len(set.union(set(contacts_splitted[:, 1]), set(contacts_splitted[:, 2])))
    max_edge_count = int(nb_node*(nb_node-1)/2)
    current_graph = np.zeros((nb_node,nb_node))
    current_edge_count = 0
    fraction_created_con = [-1]*duration
    fraction_deleted_con = [-1]*duration
    fraction_created_dis = [-1]*duration
    fraction_deleted_dis = [-1]*duration
    current_entry = 0
    for i in range(duration):
        current_graph_2 = np.matmul(current_graph,current_graph)
        available_con_2 = np.logical_and(current_graph_2>0,current_graph==0).sum()/2
        con_link_count = (current_graph_2>0).sum()/2 - available_con_2
        deleted_con = 0
        created_con = 0
        deleted_dis = 0
        created_dis = 0
        while current_entry < contacts_splitted.shape[0] and contacts_splitted[current_entry,0] <= i:
            if current_graph_2[contacts_splitted[current_entry,1]-1,contacts_splitted[current_entry,2]-1] > 0:
                deleted_con += contacts_splitted[current_entry,3]
                created_con += 1 - contacts_splitted[current_entry,3]
            else:
                deleted_dis += contacts_splitted[current_entry,3]
                created_dis += 1 - contacts_splitted[current_entry,3]
            current_graph[contacts_splitted[current_entry,1]-1,contacts_splitted[current_entry,2]-1] = 1 - contacts_splitted[current_entry,3]
            current_graph[contacts_splitted[current_entry,2]-1,contacts_splitted[current_entry,1]-1] = 1 - contacts_splitted[current_entry,3]
            current_entry += 1
        if available_con_2 != 0:
            fraction_created_con[i] = created_con/available_con_2
        if con_link_count != 0:
            fraction_deleted_con[i] = deleted_con/con_link_count
        if current_edge_count < max_edge_count - available_con_2:
            fraction_created_dis[i] = created_dis/(max_edge_count-available_con_2-current_edge_count)
        if current_edge_count-con_link_count != 0:
            fraction_deleted_dis[i] = deleted_dis/(current_edge_count-con_link_count)
        current_edge_count += created_con + created_dis - deleted_con - deleted_dis
    return np.array(fraction_created_con),np.array(fraction_deleted_con),np.array(fraction_created_dis),np.array(fraction_deleted_dis)
