# Replication

## Installing the OS

### There are two options to install the operating system onto your raspberry pi.
1. NOOBS
2. Manual disk dumping. 

### NOOBS:

https://www.raspberrypi.org/downloads/noobs/

### Manual disk dumping:

Download the raspberry pi linux image or a supported OS.

If you have a linux machine, the process is fairly easy, otherwise you will need to use something like Balena Etcher to write the given Img to a MicroSD card, or 
use the Raspberry Pi Imager.

For Linux:

1.  First, unzip the downloaded file if it is in a zip folder.
2. Run the following commands with your file, the drive path you are writing to, and the path to your file. 
First get your drive path with
```
$ lsblk -p
```
Find which drive is your MicroSD card with the header /dev/

Now run this command: 
```
$ sudo dd bs=4M if=(filepath for iso) of=(filepath of sdcard) conv-fdatasync status=progress
```
Example:
```
$ sudo dd bs=4M if=/home/user/Downloads/2020-08-20-raspios-buster-armhf-full.img of=/dev/mmcblk0 conv=fdatasync status=progress
```
If you do not have dd installed, install it to your system. 

Now, eject the microSD card in your OS and remove it from your computer.

Insert the microSD card inside of your Raspberry Pi and hook up a Keyboard, Mouse, and Monitor, then give the Pi power.

When you boot up, go through the "Welcome to Raspberry Pi" screen and let it run its path until it's done.

If you are going to always use peripherals with your Raspberry Pi, you can skip the next set of instructions as we will be setting up the Remote Desktop via VNC.

### Setting up VNC via Ethernet, although Wifi can be used. 

If you are using Raspbian Jessie or newer, VNC server is installed at default. 
1. Connect both devices together with an Ethernet cord. *Optional if you are using Wifi* 
2. Set the target Pi eth0/wlan0 Manual IP Address to something like 192.168.1.1.  *Use wlan0 if using Wifi*
3. Depending on your OS, this will be a little different. Since I know the Linux route, we will go through that, but I suggest looking online for a different guide for a different OS. I am using Manjaro XFCE, a wing of Arch Linux, so it's a little different. The next set of instructions will be on your personal machine, not the Pi so skip to instruction 6.
4. On Manjaro, go to your "Advanced Network Configuration" and either edit the ethernet that you and your Pi are connected to, or the same Wifi network. 
5. Go to your Ipv4 settings and select a free static IP address like 192.168.1.2, just make sure it's not the same one as your Pi.
6. Make it so the VNC Server starts on bootup by typing these into the terminal of your Pi:
```
$ sudo vncinitconfig --install-defaults
$ sudo systemctl enable sudo vncserver-x11-serviced
```
7. On the device you want to connect with download and open VNC Viewer. Then connect to the set IP on the Pi (192.168.1.1 in this example).

Note: If you use ethernet for your Pi, the Pi will lose it's true internet connection and will be local only, this is not the case for over wifi I believe. 
This can be adjusted by using Wifi while you are VNC'd into the Pi with a trick below. 

Note: If your Pi does not autostart VNCServer on boot, try the other way below.
### Other option for autostart if other doesnt work.

Create a VncServer.desktop file in /home/pi/.config/autostart

you may have to create the autostart directory: 
```
$ mkdir autostart
```
Desktop File to be created:
```
[Desktop Entry]
Type=Application
Name=VncServer
Exec=sudo vncserver-x11-serviced
StartupNotify=false
```
### To have ethernet as local and wifi to access the rest of the world on your Pi
go to /etc/dhcpcd.conf

Insert:
```
interface eth0
metric 300
interface wlan0
metric 200
```
Lower metric prioritizes one over other, so when we are connected to the pi over ethernet, we can then turn on the wifi when connected to it. 

