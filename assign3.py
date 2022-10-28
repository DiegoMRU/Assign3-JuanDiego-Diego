USERNAME = "dgonz348"  # define your MRU username here



def get_beverage_type(a_enabled: bool, b_enabled: bool) -> str:
    """
    Returns the beverage type defined by the switches.
    """
    is_a_enabled = a_enabled # set the variable to the parameter's value
    is_b_enabled = b_enabled # set the variable to the parameter's value

    if (is_a_enabled == True):
        beverage = 'water'
    # Since water is obtained by the swicth A being enabled, either B is enabled or not, 
    # there is no need to care for B being True or False

    elif (is_a_enabled == False) and (is_b_enabled == True):
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
        state = """ frozen
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
    elif slider_value < 16:
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
    elif slider_value < 42:
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
    elif slider_value < 100:
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
    # It compares the value the user chose and then it assigns a string to state variable 

    return state



def get_switch_value(switch_name: str) -> bool:
    """
    Prompts the user for the state of the specified switch.
    Returns true if the specified switch is enabled and false otherwise.
    """
      

    is_switch_name = input(f"Is switch {switch_name} enabled?(y/n): ").lower() == 'y'
    #it prompts the user for the state of the swicth and it  compare that input to make it  a boolean 
    # and it assigns that to the variable
    
    if is_switch_name == True:
        return True
    else:
        return False
    # It compares the value and depending on the string it returns either True or False



def main() -> None:
    """
    Prompts the user for the state of switches A and B and
    the value of the numeric slider. Using the various provided
    function headers, duplicate the functionality of the
    abandoned replicator at https://mru-replicator.fly.dev.
    """
    switch_a = get_switch_value("A")
    # Calls in "get_switch_value" for the switch A and then it assigns what the function returned to switch_a
    
    switch_b = get_switch_value("B")
    # Calls in "get_switch_value" for the switch B and then it assigns what the function returned to switch_b
    
    slider_value = int(input("What's the value of the slider?(0-100): "))
    # set the variable to the user's input, the value is a integer
    

    print(f'result: {get_beverage_type(switch_a, switch_b)}, {get_temperature_desc(slider_value)}')
    # calls in the functions "get_beverage_type" and "get_temperature_desc" using 
    # the values from the previous variables as arguments and then it prints the result  

main() # calls in main to execute program

# How to do multiline strings: 
# https://www.techbeamers.com/python-multiline-string/#:~:text=Use%20triple%20quotes%20to%20create%20a%20multiline%20string&text=You%20will%20need%20to%20enclose,and%20second%20in%20the%20end.&text=Anything%20inside%20the%20enclosing%20Triple,part%20of%20one%20multiline%20string.


