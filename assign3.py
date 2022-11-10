USERNAME = "dgonz348"  # define your MRU username here



def get_beverage_type(a_enabled: bool, b_enabled: bool) -> str:
    """
    Returns the beverage type defined by the switches.
    """
    is_a_enabled = a_enabled # set the variable to the parameter's value
    is_b_enabled = b_enabled # set the variable to the parameter's value

    if is_a_enabled:
        beverage = 'water '
    # Since water is obtained by the switch A being enabled, whether B is enabled or not, 
    # then there is no need to care for B being True or False

    elif not is_a_enabled and is_b_enabled:
        beverage = 'milk, 2%'
    else:
        beverage = 'coffee, americano'
    # it compares the values of is_a_enabled and is_b_enabled and depending on 
    # the values it sets the variable to a string from above

    return beverage
    


def get_temperature_desc(slider_value: int) -> str:
    """
    Returns the temperature description defined by the slider value.
    Assume the value is always an integer between 0 and 100 (inclusive).
    """

    if slider_value == 0:
        state = """frozen
         _.-.  
       ,'/ //\ 
      /// // /)
     /// // //|
    /// // /// 
   /// // ///  
  (`: // ///   
   `;`: ///    
   / /:`:/     
  / /  `'      
 / /           
(_/  
                """       
    elif slider_value < 16: # From 1 to 15 
        state = """cold
        
    .   *   ..  . *  * 
*  * @()Ooc()*   o  .  
    (Q@*0CG*O()  ___   
    |\_________/|/ _ \ 
    |  |  |  |  | / | |
    |  |  |  |  | | | |
    |  |  |  |  | | | |
    |  |  |  |  | | | |
    |  |  |  |  | | | |
    |  |  |  |  | \_| |
    |  |  |  |  |\___/ 
    |\_|__|__|_/|      
     \_________/  
                """    
    elif slider_value < 42: # From 16 to 41
        state = """warm
     ____     
    |    |    
    |    |    
    |____|    
    |    |    
    (    )    
    )    (    
  .'      `.  
 /          \ 
|------------|
|            |
|   /----\   |
|  |      |  |
|  |      |  |
|  |      |  |
|   \----/   |
|            |
|------------|
|____________|
                """ 
    elif slider_value < 100: # From 42 to 99
        state = """hot
    (  )  (   )  )      
     )(    ) (  (       
    (  )  (   )  )       
     _____________       
    <_____________> ___  
    |             |/ _ \ 
    |               | | |
    |               |_| |
 ___|             |\___/ 
/    \___________/    \  
\_____________________/  
                """
    else:
        state = """boiling
                
                       ( )    (  )
                 (  )              
               _.----""()""()---._ 
 .------.___  (     ()     ()     )
(        ___|-|`""----..(_)__..-""|
 \------/     |                   |
              |                   |
              |                   |
              |                   |
               `""----..____..---"" 
                """
    # Depending on the user's choice, it assigns a value to the variable state 

    return state



def get_switch_value(switch_name: str) -> bool:
    """
    Prompts the user for the state of the specified switch.
    Returns true if the specified switch is enabled and false otherwise.
    """
      

    is_user_input = input(f"Is switch {switch_name} enabled?(y/n): ").lower() == 'y'
    #it prompts the user for the state of the swicth and it  compare that input to make it  a boolean 
    # and it assigns that to the variable
    return is_user_input
    # It compares the value and depending on the string it returns either True or False



def main() -> None:
    """
    Prompts the user for the state of switches A and B and
    the value of the numeric slider. Using the various provided
    function headers, duplicate the functionality of the
    abandoned replicator at https://mru-replicator.fly.dev.
    """
    is_switch_a = get_switch_value("A")
    # Calls in "get_switch_value" for the switch A and then it assigns what the function returned to switch_a
    
    is_switch_b = get_switch_value("B")
    # Calls in "get_switch_value" for the switch B and then it assigns what the function returned to switch_b
    
    slider_value = int(input("What's the value of the slider?(0-100): "))
    # set the variable to the user's input, the input should be an integer
    

    print(f'Result: {get_beverage_type(is_switch_a, is_switch_b)}, {get_temperature_desc(slider_value)}')
    # calls in the functions "get_beverage_type" and "get_temperature_desc" using 
    # the values from the previous variables as arguments and then it prints the result  
    while slider_value <= 100:
        slider_value += 1
        main()

main() # calls in main to execute program

# How to do multiline strings: 
# https://www.techbeamers.com/python-multiline-string/#:~:text=Use%20triple%20quotes%20to%20create%20a%20multiline%20string&text=You%20will%20need%20to%20enclose,and%20second%20in%20the%20end.&text=Anything%20inside%20the%20enclosing%20Triple,part%20of%20one%20multiline%20string.


