#14.3
#Import microbit module
from microbit import *

#14.5
#Import radio module
import radio

#14.3
#Read digital data from pin 0 to set it up
pin0.read_digital()

#14.5
#Enable radio hardware on microbit
radio.on()

#14.5
#Configure radio channel to 16
radio.config(channel=16)

#14.4
#Define custom function get_temp() with parameters adc_reading, x1, y1, x2, and y2
def get_temp(adc_reading, x1, y1, x2, y2):
    
    #14.4
    #Set value of adc_reading to x
    x = adc_reading
    
    
    #14.4
    #Subtract y1 from y2 and subtract x1 from x2
    #Divide result of y by result of x
    #This gives the value of the slope, assign this to m
    m = (y2 - y1) / (x2 - x1) 
    
    #14.4
    #Muliply x1 and m
    #Subtract resulting value from y1
    #Set final value to b
    b = y1 - m * x1
    
    #14.4
    #Multiply x and m
    #Add resulting value to b
    #Set final value to y
    y = m * x + b
    
    #14.4
    #Return value of y to calling code
    return y

#14.3
#Infinitely loop indented code
while True:
    
    #14.3
    #Read analog data from pin 0
    #Set value of data to variable value
    value = pin0.read_analog()

    #14.4
    #Call function get_temp() with parameters value, 320, 32, 535, and 72 passed in respectively
    #Set returned value to temp
    temp = get_temp(value, 320, 32, 535, 72)

    #14.4
    #Round value of temp
    #Set rounded value to temp
    temp = round(temp) # ← New

    #14.5
    #Send converted string value of temp with radio
    radio.send(str(temp))

    #14.4
    #Scroll converted string value of temp across screen
    display.scroll(str(temp))
