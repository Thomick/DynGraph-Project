import numpy as np


def parse_data(filename):
    contacts = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            n1, n2, ts, te = line.split(sep=" ")
            contacts.append([int(n1), int(n2), int(ts), int(te)])
    return np.array(contacts, dtype=int)


def datainfo(filename):
    contacts = parse_data(filename)
    nb_node = len(set.union(set(contacts[:, 0]), set(contacts[:, 1])))
    nb_contact = contacts.shape[0]
    duration = np.max(contacts[:, 3]) - np.min(contacts[:, 3])
    return nb_node, nb_contact, duration


def format_file(filename):
    contacts = parse_data(filename)
    delta = np.min(contacts[:, 3])
    contacts[:, (2, 3)] -= delta
    np.savetxt(filename+"_formatted", contacts, fmt="%s")


def convert2splitted(filename):
    contacts = parse_data(filename)
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
