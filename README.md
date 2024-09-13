# Check Power Connection 



## Installation

Install necessary packages: You'll need the psutil library to check the power status. Install it using pip



```bash
sudo apt install python3-pip
pip3 install psutil
```

## How the Script Works

The psutil.sensors_battery() function checks the power status of the battery.


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.


## Installation

Install necessary packages: You'll need the psutil library to check the power status. Install it using pip



```bash
sudo apt install python3-pip
pip3 install psutil
```

## How the Script Works

1. The psutil.sensors_battery() function checks the power status of the battery.
2. If the power is not connected (battery.power_plugged is False), the system will shut down using the shutdown command.
3. The script runs in an infinite loop, checking the power connection every 5 seconds.

## Steps to Run

```bash
chmod +x power_check.py
```
```bash
sudo python3 power_check.py
```


