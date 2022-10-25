USERNAME = "dgonz348"  # define your MRU username here



def get_beverage_type(a_enabled: bool, b_enabled: bool) -> str:
    """
    Returns the beverage type defined by the switches.
    """
    is_a_enabled = a_enabled # set the variable to the parameter's value
    is_b_enabled = b_enabled # set the variable to the parameter's value

    if (is_a_enabled == True) and (is_b_enabled == True):
        beverage = 'water'
    elif (is_a_enabled == True) and (is_b_enabled == False):
        beverage = 'water'
    elif (is_a_enabled == False) and (is_b_enabled == True):
        beverage = 'milk, 2%'
    elif (is_a_enabled == False) and (is_b_enabled == False):
        beverage = 'coffee, americano'
    # it compares the values of is_a_enabled and is_b_enabled and depending on 
    # the values it sets the variable to a string from above
    
    message = beverage # it sets the message variable to what the beverage was set for
    return message
    



def get_temperature_desc(slider_value: int) -> str:
    """
    Returns the temperature description defined by the slider value.
    Assume the value is always an integer between 0 and 100 (inclusive).
    """
    is_slider_value = slider_value # sets the variable to the parameter's value

    if is_slider_value == 0:
        state = 'frozen'
    elif is_slider_value <= 15:
        state = 'cold'    
    elif is_slider_value <=41:
        state = 'warm' 
    elif is_slider_value <= 99:
        state = 'hot'
    elif is_slider_value == 100:
        state = 'boiling'
    # It compares the value the user chose and then it assigns a string to state variable 
    
    message = state # assigns variable to state
    return message

def get_switch_value(switch_name: str) -> bool:
    """
    Prompts the user for the state of the specified switch.
    Returns true if the specified switch is enabled and false otherwise.
    """
    is_switch_name = switch_name # sets the variable to the parameter's value 

    if is_switch_name == 'y':
        switch_name = True
    elif is_switch_name == 'n':
        switch_name = False
    # It compares the value and depending on the string it sets switch_name to either True or False

    return switch_name

def main() -> None:
    """
    Prompts the user for the state of switches A and B and
    the value of the numeric slider. Using the various provided
    function headers, duplicate the functionality of the
    abandoned replicator at https://mru-replicator.fly.dev.
    """
    
    switch_a = get_switch_value(input("Is switch A enabled?(y/n): "))
    # it sets the argument to what the user input and then calls in the function 
    # to then set the variable to what the function returned
    
    switch_b = get_switch_value(input("Is switch B enabled?(y/n): "))
    # it sets the argument to what the user input and then calls in the function 
    # to then set the variable to what the function returned

    slider_value = int(input("What's the value of the slider?(0-100): "))
    #set the variable to what the user input, the value is a integer
    

    print(f'result: {get_beverage_type(switch_a, switch_b)}, {get_temperature_desc(slider_value)}')
    # calls in the functions "get_beverage_type" and "get_temperature_desc" using the values from the previous variables
    # as arguments and then it prints the result  

main()