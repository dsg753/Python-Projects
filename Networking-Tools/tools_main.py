# Import necessary modules
import subprocess
import tools


# Function for displaying menu
def Display_Menu():
    header = """
    ___________________________
    |                          |
    |  Basic Networking Tools  |
    |_____________   __________|
                          \  \                 
                            ^_ _^              
                            (o o)\_________    
                            (_ _)\         )/\/
                              U   ||----W||    
                                  ||     ||    

    ### Available Tools:
        [1] Locate an IP address
        [2] Get the IP address of a domain
        [3] Ping a host or IP address
        [4] Port Scanner
        [5] Traceroute
        [6] Exit 
    
    * Type <clear> to clear previous commands
    * Type <q> or to abort operation of a tool

    """
    print(header)


# Functionality of every option
# Each option operates the tool related to the option number.
def option_1():
    """
    Option 1 --> IP Locater
    """
    tools.locate_ip()
    Display_Menu()
    Home()


def option_2():
    """
    Option 2 --> IP Finder
    """
    tools.get_ip()
    Display_Menu()
    Home()


def option_3():
    """
    Option 3 --> Pinging
    """
    tools.ping()
    Display_Menu()
    Home()


def option_4():
    """
    Option 4 --> Port Scanner
    """
    tools.port_scanner()
    Display_Menu()
    Home()


def option_5():
    """
    Option 5 --> Traceroute
    """
    tools.traceroute()
    Display_Menu()
    Home()

def option_6():
    """
    Option 6 --> Exit
    """
    quit()

# Function for selecting options
def Home():
    """
    Home of the program is selecting an option from available options.
    """
    # Available options' numbers as shown in the menu
    available_options = (1, 2, 3, 4, 5, 6)
    while True:
        try:
            selected_option = input("\nEnter your option\n>>> ")
            # Clear screen command
            if selected_option == 'clear':
                subprocess.call('cls', shell=True)
                Display_Menu()
                continue
            else:
                selected_option = int(selected_option)
        except ValueError:
            print("Please enter the number of the option")
            continue
        else:
            # Validate the selected option
            if selected_option not in available_options:
                print("The option is not available.\nTry another one.")
                continue
            else:
                break
    # Map options to their respective functions
    if selected_option == 1:
        option_1()
    elif selected_option == 2:
        option_2()
    elif selected_option == 3:
        option_3()
    elif selected_option == 4:
        option_4()
    elif selected_option == 5:
        option_5()
    elif selected_option == 6:
        option_6()



if __name__ == "__main__":
    Display_Menu()
    Home()
