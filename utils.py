import numpy as np
import matplotlib.pyplot as plt


def parse_raw_data(filename):
    contacts = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            n1, n2, ts, te = line.split(sep=" ")
            contacts.append([int(n1), int(n2), int(ts), int(te)])
    return np.array(contacts, dtype=int)


def parse_splitted_data(filename):
    contacts = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            t, n1, n2, a = line.split(sep=" ")
            a = 0 if a[0] == "C" else 1
            contacts.append([int(t), int(n1), int(n2), int(a)])
    return np.array(contacts, dtype=int)


def datainfo(filename):
    contacts = parse_raw_data(filename)
    nb_node = len(set.union(set(contacts[:, 0]), set(contacts[:, 1])))
    nb_contact = contacts.shape[0]
    duration = np.max(contacts[:, 3]) - np.min(contacts[:, 3])
    return nb_node, nb_contact, duration


def format_file(filename):
    contacts = parse_raw_data(filename)
    delta = np.min(contacts[:, 3])
    contacts[:, (2, 3)] -= delta
    np.savetxt(filename+"_formatted", contacts, fmt="%s")


def convert2splitted(filename):
    contacts = parse_raw_data(filename)
    zeros = np.zeros((contacts.shape[0], 1), dtype=int)
    creation = np.concatenate((contacts[:, (2, 0, 1)], zeros), axis=1)
    suppression = np.concatenate((contacts[:, (3, 0, 1)], zeros+1), axis=1)
    suppression[:, 0] += 1
    merged = np.concatenate((creation, suppression), axis=0)
    merged = merged[merged[:, 0].argsort()]
    with open(filename+"_splitted", 'w') as f:
        for i in range(merged.shape[0]):
            f.write(
                f"{merged[i,0]} {merged[i,1]} {merged[i,2]} {'C' if merged[i,3]==0 else 'S'}\n")


def get_intercontact_duration(contacts):
    inter_duration = []
    for i in range(contacts.shape[0]-1):
        if contacts[i+1, 0] == contacts[i, 0] and contacts[i+1, 1] == contacts[i, 1]:
            inter_duration.append(contacts[i+1, 2]-contacts[i, 3]-1)
    return inter_duration


def plot_distrib(data,title=""):
    plt.hist(data,200)
    plt.title(title)
    plt.show()

def get_avg_degree(contacts_splitted):
    last = 0
    degrees = [0]
    timesteps = [0]
    for i in range(contacts_splitted.shape[0]):
        if contacts_splitted[i][0] != timesteps[-1]:
            degrees.append(degrees[-1])
            timesteps.append(contacts_splitted[i][0])
        degrees[-1] += 1-2*contacts_splitted[i][3]
    nb_node = len(set.union(set(contacts_splitted[:, 1]), set(contacts_splitted[:, 2])))
    return np.array(timesteps),np.array(degrees)/nb_node