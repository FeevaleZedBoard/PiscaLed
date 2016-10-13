def export_gpio(pino):
    try:
        file = open("/sys/class/gpio/export","w")
        file.write(str(pino))
        file.close()
    except IOError:
        print "GPIO %s already Exists, so skipping export gpio" % (str(pino), )

def unexport_gpio(pino):
    try:
        file = open("/sys/class/gpio/unexport","w")
        file.write(str(pino))
        file.close()
    except IOError:
        print "GPIO %s is not found, so skipping unexport gpio" % (str(pino), )

def setpindirection(pin_num, pin_direction):
    gpiopin = "gpio%s" % (str(pin_num), )
    file = open("/sys/class/gpio/"+gpiopin+"/direction","w")
    file.write(pin_direction)
    file.close()

def write_pino(pin_num, pin_value):
    gpiopin = "gpio%s" % (str(pin_num), )
    file = open("/sys/class/gpio/"+gpiopin+"/value","w")
    if pin_value == 1:
      file.write("1")
    else:
      file.write("0")
    file.close()

def read_gpio(pin_num):
    gpiopin = "gpio%s" % (str(pin_no), )
    file = open("/sys/class/gpio/"+gpiopin+"/value","r")
    value = pin.read()
    print "The value on the PIN %s is : %s" % (str(pin_num), str(value))
    file.close()
    return int(value)

if __name__ == '__main__':
    import time
    
    pin = int(input("Digite o numero da gpio:"))
    export_gpio(pin)
    setpindirection(pin, "out")

    while(1):
      try:	
      	write_pino(pin, 1)
      	time.sleep(1)
      	write_pino(pin, 0)
      	time.sleep(1)
      except:
	print("Removendo dependencias")
	write_pino(pin,0)
	unexport_gpio(pin)
	time.sleep(1)
	exit()
