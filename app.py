import psutil
import os
import time

def check_power_connection():
    battery = psutil.sensors_battery()
    return battery.power_plugged

def shutdown_system():
    print("Power disconnected! Shutting down system...")
    os.system("sudo shutdown now")

def main():
    while True:
        if not check_power_connection():
            shutdown_system()
        time.sleep(5)  

if __name__ == "__main__":
    main()
    