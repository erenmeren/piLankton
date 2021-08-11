# PiLankton

Open source something

## Installation

1-) Copy `"ssh"` and `"wpa_supplicatint.conf"` files inside the boot folder.

2-) Find raspberry pi ip address. Example => "nmap -sP 192.168.43.0/24"

3-) Time to connect Raspi. Open terminal and run `"ssh pi@{RP_IP_ADDRESS}"`. Default password is `"raspberry"`. After connection run these commands.
* `sudo apt update`
* `sudo apt upgrade`
* `sudo apt install python3-pip python3-pil`
* `pip3 install boto3 RPi.GPIO`
* `sudo raspi-config => Interface Options => Enable SPI and I2C`
* `sudo reboot`

4-) Connect to raspi again copy any folder under the pi dicrectory.

Folders :
* inky-wHat-v1
* ...

## [Create Discovery and Printer Services](https://thepihut.com/blogs/raspberry-pi-tutorials/auto-starting-programs-on-the-raspberry-pi)

Don't forget to change folder paths inside service files !!!

1-) Copy piLankton-discovery and piLankton-printer services inside `"home/pi"`
* `sudo mv piLankton-discovery.service piLankton-printer.service /lib/systemd/system/`
* `sudo chmod 644 /lib/systemd/system/piLankton-discovery.service`
* `sudo chmod 644 /lib/systemd/system/piLankton-printer.service`
* `sudo systemctl daemon-reload`

* `sudo systemctl enable piLankton-discovery.service`
* `sudo systemctl status piLankton-discovery.service`
* `sudo service piLankton-discovery start`
* Check service again => `sudo systemctl status piLankton-discovery.service`

* `sudo systemctl enable piLankton-printer.service`
* `sudo systemctl status piLankton-printer.service`
* `sudo service piLankton-printer start`
* Check service again => `sudo systemctl status piLankton-printer.service`


## AWS installation

### Raspberry

Create AWS configuration files

1-) Create the directory ~/.aws directory

2-) Create the ~/.aws/credentials file
```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```

3-) Create the /root/.aws/config file
```
[default]
region=eu-west-2
```

### Lamnda, S3 and IoT

Maybe later