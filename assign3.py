USERNAME = "dgonz348"  # define your MRU username here



def get_beverage_type(a_enabled: bool, b_enabled: bool) -> str:
    """
    Returns the beverage type defined by the switches.
    """

    if a_enabled == 'y':
        a_enabled = True
    else: 
        a_enabled = False
    
    if b_enabled == 'y':
        b_enabled = True
    else:
        b_enabled = False

    a_enabled = True
    b_enabled = True



    if a_enabled == True:
        beverage = 'water'
    elif b_enabled == True:
        beverage = 'milk, 2%'
    elif a_enabled  == False and b_enabled == False:
        beverage = 'coffee, americano'

    # it compares the values for the switches A and B and assigns the values depending  what the users chooses
    # this is basic code and needs to be improved
    print(beverage)



def get_temperature_desc(slider_value: int) -> str:
    """
    Returns the temperature description defined by the slider value.
    Assume the value is always an integer between 0 and 100 (inclusive).
    """
    slider_value = int(input('enter number'))
    if slider_value == 0:
        print('frozen')
    elif slider_value <= 15:
        print('cold')    
    elif slider_value <=41:
        print('warm') 
    elif slider_value <= 99:
        print('hot')
    elif slider_value == 100:
        print('boiling')
    # It compares the values of what the user chooses and print a state of the beverage depending on what the user chose
    # this is basic code and needs to be improved

def get_switch_value(switch_name: str) -> bool:
    """
    Prompts the user for the state of the specified switch.
    Returns true if the specified switch is enabled and false otherwise.
    """


def main() -> None:
    """
    Prompts the user for the state of switches A and B and
    the value of the numeric slider. Using the various provided
    function headers, duplicate the functionality of the
    abandoned replicator at https://mru-replicator.fly.dev.
    """


is_a_enabled = input('Is the switch A enabled?(y for yes and n for no) ')
a_enabled = True

if is_a_enabled == 'y':
    a_enabled = True
elif is_a_enabled == 'n':
    a_enabled = False 

print(a_enabled)

