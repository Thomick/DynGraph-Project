from utils import *
import numpy as np
import matplotlib.pyplot as plt
from model_generation import *
from graph_analysis import *

generate_new_models = False # Set to False to speed up the execution if the model were previously generated

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
    '''
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
    inter_dur = get_intercontact_duration(contacts)
    print("    Maximum intercontact duration :",np.max(inter_dur))
    plot_distrib(inter_dur,"Intercontact duration distributon for Infocom06")
    print("    Plotting intercontact duration distributon for RollerNet ...")
    contacts = parse_raw_data("data/RollerNet")
    inter_dur = get_intercontact_duration(contacts)
    print("    Maximum intercontact duration :",np.max(inter_dur))
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
    plt.ylabel("Average degree")
    plt.show()
    print("    Plotting evolution of average degree for RollerNet ...")
    contacts = parse_splitted_data("data/RollerNet_formatted_splitted")
    avg_degree = get_avg_degree(contacts)
    plt.plot(avg_degree)
    plt.title("Evolution of average degree for RollerNet")
    plt.xlabel("Time")
    plt.ylabel("Average degree")
    plt.show()
    
    ########## EX 8 ##############
    print("Exercise 8 :")
    contacts = parse_splitted_data("data/Infocom06_formatted_splitted")
    print("    Computing fraction of created links and fraction of deleted links for Infocom06")
    created_infocom, deleted_infocom = get_created_deleted_fraction(contacts)
    print("    Saving fraction of created links for Infocom06 in data/Infocom06_created...")
    np.savetxt("data/Infocom06_created", created_infocom)
    print("    Saving fraction of deleted links for Infocom06 in data/Infocom06_deleted...")
    np.savetxt("data/Infocom06_deleted", deleted_infocom)
    contacts = parse_splitted_data("data/RollerNet_formatted_splitted")
    print("    Computing fraction of created links and fraction of deleted links for RollerNet")
    created_rollernet, deleted_rollernet = get_created_deleted_fraction(contacts)
    print("    Saving fraction of created links for RollerNet in data/RollerNet_created...")
    np.savetxt("data/RollerNet_created", created_rollernet)
    print("    Saving fraction of deleted links for RollerNet in data/RollerNet_deleted...")
    np.savetxt("data/RollerNet_deleted", deleted_rollernet)
    
    ########## EX 9 ############## -> See model_generation.py
    ########## EX 10 ##############
    print("Exercise 10 :")
    print("    Edge markovian parameters for Infocom06 :")
    p,d = np.mean(created_infocom[created_infocom != -1]),np.mean(deleted_infocom[deleted_infocom != -1])
    print("        Probability that a new link is created p :",p)
    print("        Probability that an existing link is deleted d :",d)
    print("        Number of nodes :", nb_node_info)
    print("        Number of time steps :",duration_info)
    if generate_new_models:
        print("    Generating model ...")
        contacts_model = np.array(generate_edge_markovian(nb_node_info, p, d, duration_info))
        print(contacts_model)
        save_splitted("data/Infocom06_markovian_model", contacts_model)
    print("    Plotting evolution of average degree ...")
    contacts_model = parse_splitted_data("data/Infocom06_markovian_model")
    contacts = parse_splitted_data("data/Infocom06_formatted_splitted")
    avg_degree = get_avg_degree(contacts)
    avg_degree_model = get_avg_degree(contacts_model)
    plt.plot(avg_degree,label="Infocom06")
    plt.plot(avg_degree_model,label="Edge-Markovian model")
    plt.title("Evolution of average degree")
    plt.xlabel("Time")
    plt.ylabel("Average degree")
    plt.legend()
    plt.show()

    print("    Edge markovian parameters for Rollernet :")
    p,d = np.mean(created_rollernet[created_rollernet != -1]),np.mean(deleted_rollernet[deleted_rollernet != -1])
    print("        Probability that a new link is created p :",p)
    print("        Probability that an existing link is deleted d :",d)
    print("        Number of nodes :", nb_node_roller)
    print("        Number of time steps :",duration_roller)
    if generate_new_models:
        print("    Generating model ...")
        contacts_model = np.array(generate_edge_markovian(nb_node_roller, p, d, duration_roller))
        save_splitted("data/RollerNet_markovian_model", contacts_model)
    print("    Plotting evolution of average degree ...")
    contacts_model = parse_splitted_data("data/RollerNet_markovian_model")
    contacts = parse_splitted_data("data/RollerNet_formatted_splitted")
    avg_degree = get_avg_degree(contacts)
    avg_degree_model = get_avg_degree(contacts_model)
    plt.plot(avg_degree,label="Rollernet")
    plt.plot(avg_degree_model,label="Edge-Markovian model")
    plt.title("Evolution of average degree")
    plt.xlabel("Time")
    plt.ylabel("Average degree")
    plt.legend()
    plt.show()
    ########## EX 11 ############## -> See report

    ########## EX 12 ##############
    # Distribution of mean degree
    contacts = parse_splitted_data("data/Infocom06_formatted_splitted")
    mean_degrees = get_node_avg_degree(contacts)
    plot_distrib(mean_degrees,nb_bucket = 15)
    contacts = parse_splitted_data("data/RollerNet_formatted_splitted")
    mean_degrees = get_node_avg_degree(contacts)
    plot_distrib(mean_degrees,nb_bucket =15)
    

    # Unique moving nodes count
    contacts = parse_splitted_data("data/Infocom06_formatted_splitted")
    contacts_model = parse_splitted_data("data/Infocom06_markovian_model")
    unique_moving_node_count = get_unique_moving_node_count(contacts)
    unique_moving_node_count_model = get_unique_moving_node_count(contacts_model)
    plt.plot(unique_moving_node_count_model)
    plt.plot(unique_moving_node_count)
    plt.show()

    contacts = parse_splitted_data("data/RollerNet_formatted_splitted")
    contacts_model = parse_splitted_data("data/RollerNet_markovian_model")
    unique_moving_node_count = get_unique_moving_node_count(contacts)
    unique_moving_node_count_model = get_unique_moving_node_count(contacts_model)
    plt.plot(unique_moving_node_count_model)
    plt.plot(unique_moving_node_count)
    plt.show()

    contacts = parse_splitted_data("data/Infocom06_formatted_splitted")
    contacts_model = parse_splitted_data("data/Infocom06_markovian_model")
    move_counter = get_unique_meeting_count(contacts)
    move_counter_model = get_unique_meeting_count(contacts_model)
    plt.figure()
    plot_distrib(move_counter,nb_bucket=20)
    plt.figure()
    plot_distrib(move_counter_model,nb_bucket=20,range=(30,100))
    plt.show()
    contacts = parse_splitted_data("data/RollerNet_formatted_splitted")
    contacts_model = parse_splitted_data("data/RollerNet_markovian_model")
    move_counter = get_unique_meeting_count(contacts)
    move_counter_model = get_unique_meeting_count(contacts_model)
    plt.figure()
    plot_distrib(move_counter,nb_bucket=20)
    plt.figure()
    plot_distrib(move_counter_model,nb_bucket=20,range=(53,61))
    plt.show()

    
    contacts = parse_splitted_data("data/Infocom06_formatted_splitted")
    contacts_model = parse_splitted_data("data/Infocom06_markovian_model")
    move_counter = get_per_node_average_created_deleted_fraction(contacts)
    move_counter_model = get_per_node_average_created_deleted_fraction(contacts_model)
    plt.figure()
    plot_distrib(move_counter,nb_bucket=20)
    plt.figure()
    plot_distrib(move_counter_model,nb_bucket=20)
    plt.show()

    contacts = parse_splitted_data("data/RollerNet_formatted_splitted")
    contacts_model = parse_splitted_data("data/RollerNet_markovian_model")
    created_rollernet, deleted_rollernet = get_created_deleted_fraction(contacts)
    created_model, deleted_model = get_created_deleted_fraction(contacts_model)
    plt.plot(created_rollernet)
    plt.figure()
    plt.plot(created_model)
    plt.show()

    mean_fraction_created,mean_fraction_deleted = get_per_node_average_created_deleted_fraction(contacts)
    mean_fraction_created_model,mean_fraction_deleted_model = get_per_node_average_created_deleted_fraction(contacts_model)

    plt.figure()
    plot_distrib(mean_fraction_created,nb_bucket=20)
    plt.figure()
    plot_distrib(mean_fraction_created_model,nb_bucket=20,range = (0.002,0.0045))
    plt.show()
    plt.figure()
    plot_distrib(mean_fraction_deleted,nb_bucket=20,range = (0.06,0.11))
    plt.figure()
    plot_distrib(mean_fraction_deleted_model,nb_bucket=20,range = (0.06,0.11))
    plt.show()

    '''

    contacts = parse_splitted_data("data/RollerNet_formatted_splitted")
    contacts_model = parse_splitted_data("data/RollerNet_markovian_model")

    fraction_created_con,fraction_deleted_con,fraction_created_dis,fraction_deleted_dis = get_created_deleted_fraction_wconnection(contacts)
    fraction_created_con_model,fraction_deleted_con_model,fraction_created_dis_model,fraction_deleted_dis_model = get_created_deleted_fraction_wconnection(contacts_model)

    print(f"Data: fraction_created_con {np.mean(fraction_created_con[fraction_created_con>=0])},fraction_deleted_con {np.mean(fraction_deleted_con[fraction_deleted_con>=0])},fraction_created_dis {np.mean(fraction_created_dis[fraction_created_dis>=0])},fraction_deleted_dis {np.mean(fraction_deleted_dis[fraction_deleted_dis>=0])}")
    print(f"Model: fraction_created_con {np.mean(fraction_created_con_model[fraction_created_con_model>=0])},fraction_deleted_con {np.mean(fraction_deleted_con_model[fraction_deleted_con_model>=0])},fraction_created_dis {np.mean(fraction_created_dis_model[fraction_created_dis_model>=0])},fraction_deleted_dis {np.mean(fraction_deleted_dis_model[fraction_deleted_dis_model>=0])}")

    if generate_new_models:
        print("    Generating model ...")
        p_con = np.mean(fraction_created_con[fraction_created_con>=0])
        d_con = np.mean(fraction_deleted_con[fraction_deleted_con>=0])
        p_dis = np.mean(fraction_created_dis[fraction_created_dis>=0])
        d_dis = np.mean(fraction_deleted_dis[fraction_deleted_dis>=0])
        contacts_model = np.array(generate_connection_dependant_model(nb_node_roller, p_con, d_con, p_dis, d_dis, duration_roller))
        save_splitted("data/RollerNet_connection_dependant_model", contacts_model)

    contacts_model = parse_splitted_data("data/RollerNet_connection_dependant_model")
    fraction_created_con_model,fraction_deleted_con_model,fraction_created_dis_model,fraction_deleted_dis_model = get_created_deleted_fraction_wconnection(contacts_model)
    print(f"New model: fraction_created_con {np.mean(fraction_created_con_model[fraction_created_con_model>=0])},fraction_deleted_con {np.mean(fraction_deleted_con_model[fraction_deleted_con_model>=0])},fraction_created_dis {np.mean(fraction_created_dis_model[fraction_created_dis_model>=0])},fraction_deleted_dis {np.mean(fraction_deleted_dis_model[fraction_deleted_dis_model>=0])}")

    print("    Plotting evolution of average degree ...")
    contacts_model = parse_splitted_data("data/RollerNet_connection_dependant_model")
    contacts = parse_splitted_data("data/RollerNet_formatted_splitted")
    avg_degree = get_avg_degree(contacts)
    avg_degree_model = get_avg_degree(contacts_model)
    plt.plot(avg_degree,label="Rollernet")
    plt.plot(avg_degree_model,label="Connection dependant model")
    plt.title("Evolution of average degree")
    plt.xlabel("Time")
    plt.ylabel("Average degree")
    plt.legend()
    plt.show()