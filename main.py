from utils import *
import numpy as np

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
    print("    Converting Infocom06 -> Infocom06_splitted")
    convert2splitted("data/Infocom06")
    print("    Converting RollerNet -> RollerNet_splitted")
    convert2splitted("data/RollerNet")

    ######### EX 4  -> see get_intercontact_duration ########

    ######### EX 5 ###############
    print("Exercice 5 :")
    print("    Plotting intercontact duration distributon for Infocom06 ...")
    contacts = parse_raw_data("data/Infocom06")
    inter_dur = get_intercontact_duration(contacts)
    plot_distrib(inter_dur)
    print("    Plotting intercontact duration distributon for RollerNet ...")
    contacts = parse_raw_data("data/RollerNet")
    inter_dur = get_intercontact_duration(contacts)
    plot_distrib(inter_dur)
