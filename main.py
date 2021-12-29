from utils import *
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
    ######## EX 1 #############
    print("Exercise 1 :")
    print("\tInfocom06 :")
    nb_node, nb_contact, duration = datainfo("data/Infocom06")
    print("\t\tNumber of nodes : ", nb_node)
    print("\t\tNumber of contacts : ", nb_contact)
    print("\t\tTotal duration : ", duration)
    print("\tRollerNet :")
    nb_node, nb_contact, duration = datainfo("data/RollerNet")
    print("\t\tNumber of nodes : ", nb_node)
    print("\t\tNumber of contacts : ", nb_contact)
    print("\t\tTotal duration : ", duration)

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
    print("Exercice 5 :")
    print("    Plotting intercontact duration distributon for Infocom06 ...")
    contacts = parse_raw_data("data/Infocom06")
    inter_dur = get_intercontact_duration(contacts)
    plot_distrib(inter_dur,"Intercontact duration distributon for Infocom06")
    print("    Plotting intercontact duration distributon for RollerNet ...")
    contacts = parse_raw_data("data/RollerNet")
    inter_dur = get_intercontact_duration(contacts)
    plot_distrib(inter_dur,"Intercontact duration distributon for RollerNet")

    ########## EX 6 -> see get_avg_degree ###############
    ########## EX 7 ##############
    print("Exercice 7 :")
    print("    Plotting evolution of average degree for Infocom06 ...")
    contacts = parse_splitted_data("data/Infocom06_formatted_splitted")
    timesteps, avg_degree = get_avg_degree(contacts)
    plt.step(timesteps, avg_degree, where='post')
    plt.title("Evolution of average degree for Infocom6")
    plt.xlabel("Time")
    plt.show()
    print("    Plotting evolution of average degree for RollerNet ...")
    contacts = parse_splitted_data("data/RollerNet_formatted_splitted")
    timesteps, avg_degree = get_avg_degree(contacts)
    plt.step(timesteps, avg_degree, where='post')
    plt.title("Evolution of average degree for RollerNet")
    plt.xlabel("Time")
    plt.show()
