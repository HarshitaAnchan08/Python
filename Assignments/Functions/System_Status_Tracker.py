system_status="offline"

def start_system():
    global system_status  #Accessing global variable
    system_status="online"
    print("System started.")
    
def stop_system():
    global system_status   #Accessing global variable
    system_status="offline"
    print("System stopped.")
    
def check_system_status():
    #Accessing global variable without modification
    print(f"The system is currently : {system_status}")
    
check_system_status()
start_system()
check_system_status()
stop_system()
check_system_status()
    
