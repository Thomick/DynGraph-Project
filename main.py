from utils import *
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    ######## EX 1 #############
    print("Exercise 1 :")
    print("\tInfocom06 :")
    nb_node_info, nb_contact_info, duration_info = datainfo("data/Infocom06")
    print("\t\tNumber of nodes : ", nb_node_info)
    print("\t\tNumber of contacts : ", nb_contact_info)
    print("\t\tTotal duration : ", duration_info)
    print("\tRollerNet :")
    nb_node_roller, nb_contact_roller, duration_roller = datainfo("data/RollerNet")
    print("\t\tNumber of nodes : ", nb_node_roller)
    print("\t\tNumber of contacts : ", nb_contact_roller)
    print("\t\tTotal duration : ", duration_roller)

    ######### EX 2 ############
    print("Exercise 2 :")
    print("    Formatting Infocom06 -> Infocom06_formatted")
    format_file("data/Infocom06")
    print("    Formatting RollerNet -> RollerNet_formatted")
    format_file("data/RollerNet")

    ######### EX 3 ############
    print("Exercise 3 :")
    print("    Converting Infocom06_formatted -> Infocom06_formatted_splitted")
    convert2splitted("data/Infocom06_formatted")
    print("    Converting RollerNet_formatted -> RollerNet_formatted_splitted")
    convert2splitted("data/RollerNet_formatted")

    ######### EX 4  -> see get_intercontact_duration ########

    ######### EX 5 ###############
    print("Exercise 5 :")
    print("    Plotting intercontact duration distributon for Infocom06 ...")
    contacts = parse_raw_data("data/Infocom06")
    print("    Maximum intercontact duration :",np.max(contacts))
    inter_dur = get_intercontact_duration(contacts)
    plot_distrib(inter_dur,"Intercontact duration distributon for Infocom06")
    print("    Plotting intercontact duration distributon for RollerNet ...")
    contacts = parse_raw_data("data/RollerNet")
    print("    Maximum intercontact duration :",np.max(contacts))
    inter_dur = get_intercontact_duration(contacts)
    plot_distrib(inter_dur,"Intercontact duration distributon for RollerNet")

    ########## EX 6 -> see get_avg_degree ###############
    ########## EX 7 ##############
    print("Exercise 7 :")
    print("    Plotting evolution of average degree for Infocom06 ...")
    contacts = parse_splitted_data("data/Infocom06_formatted_splitted")
    avg_degree = get_avg_degree(contacts)
    plt.plot(avg_degree)
    plt.title("Evolution of average degree for Infocom6")
    plt.xlabel("Time")
    plt.show()
    print("    Plotting evolution of average degree for RollerNet ...")
    contacts = parse_splitted_data("data/RollerNet_formatted_splitted")
    avg_degree = get_avg_degree(contacts)
    plt.plot(avg_degree)
    plt.title("Evolution of average degree for RollerNet")
    plt.xlabel("Time")
    plt.show()

    ########## EX 7 ##############
    print("Exercise 8 :")
    contacts = parse_splitted_data("data/Infocom06_formatted_splitted")
    print("    Computing fraction of created links and fraction of deleted links for Infocom06")
    created, deleted = get_created_deleted_fraction(contacts)
    print("    Saving fraction of created links for Infocom06 in data/Infocom06_created...")
    np.savetxt("data/Infocom06_created", created)
    print("    Saving fraction of deleted links for Infocom06 in data/Infocom06_deleted...")
    np.savetxt("data/Infocom06_deleted", deleted)

