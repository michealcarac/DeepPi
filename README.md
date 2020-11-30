# Initial Setup
## Installing the OS
Note: Please be cautious and refer to any online resource if you feel this guide is inadequate or inaccurate. 
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

**MAKE ABSOLUTE SURE THE DRIVE IS CORRECT AS THIS COMMAND WILL OVERWRITE THE GIVEN DRIVE**

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
### Some Housekeeping on the Pi
Go to your Raspberry Pi Configuration by clicking on the Raspberry in the top left > Preferences > Raspberry Pi Configuration > Interfaces

Enable **everything** for this Project. SSH is optional, but is handy if you want to SSH in instead of using VNC. 

NOTE: If you are going to always use peripherals with your Raspberry Pi, you can skip to [Project](https://github.com/michealcarac/DeepPi/blob/main/README.md#project) as we will be setting up the Remote Desktop via VNC.
## VNC 
### ***PLEASE READ THIS BEFORE SETTING UP VNC***
I by no means am a professional with networks so my instructions may not be the best nor the most accurate, but it written to how I understand it. 

Setting up VNC has a few caveats. 

Dynamic: When you turn on VNC Server on your Pi, the Pi is designated a dynamic IP address that you can then enter into any device that is on the same network into VNC Viewer. This is nice, however, that IP may change. Now, if you don't want to plug your peripherals back in, this can be fixed simply by installing a tool to surf your network for an IP address thats assigned to the Pi, or you can try raspberrypi.local but that may not work. Now, this method is the best for keeping internet connectivity on your Pi, but could lead into issues requiring you to put peripherals back into the Pi.  

Static: Another way is to set up a Static IP on your Pi which will make your Pi lose connection to the world wide web on that internet module (Ethernet or Wifi). That is the way that is described in full in this guide as that is what I personally prefer, but you can look up any sort of way to use your Raspberry Pi via VNC. At the time of writing this section, I have decided to use the dynamic way for the Pi Zero W as it only has one internet module, but I prefer the static method on my full sized Raspberry Pi for full control over the network side of the Pi. 

If you decide to go the Dynamic route as most people will, skip to the Dynamic portion. My instructions to setting up the OS and networking may not be the best, but they are here if wanted to be used.  
### Setting up Static VNC via Ethernet, although Wifi can be used. -Static

If you are using Raspbian Jessie or newer, VNC server is installed at default. 
1. Connect both devices together with an Ethernet cord. *Connect both devices to same Wifi if you are using Wifi* 
2. Set the target Pi eth0/wlan0 Manual IP Address to something like 192.168.1.1.  *Use wlan0 if using Wifi*
3. Depending on your OS, this will be a little different. Since I know the Linux route, we will go through that, but I suggest looking online for a different guide for a different OS. I am using Manjaro XFCE, a wing of Arch Linux, so it's a little different. The next set of instructions will be on your personal machine, not the Pi so skip to instruction 6.
4. On Manjaro, go to your "Advanced Network Configuration" and either edit the ethernet that you and your Pi are connected to, or the same Wifi network. 
5. Go to your Ipv4 settings and select a free static IP address like 192.168.1.2, just make sure it's not the same one as your Pi.
6. On the device you want to connect with download and open VNC Viewer. Then connect to the set IP on the Pi (192.168.1.1 in this example). The user/password will be the password you set on the Raspberry Pi with the user of "pi". 

Note: If you use ethernet for your Pi, the Pi will lose it's true internet connection and will be local only, same case if you are use Wi-Fi. 
This can be adjusted by using Wifi/Ethernet while you are VNC'd into the Pi with a trick below. 

Note: If your Pi does not autostart VNCServer on boot, try the way below, it also may automatically start if you enable VNC in your interfaces. 
### To have ethernet as local and wifi to access the rest of the world on your Pi -Static
go to /etc/dhcpcd.conf

Insert:
```
interface eth0
metric 300
interface wlan0
metric 200
```
Lower metric prioritizes one over other, so when we are connected to the pi over ethernet, we can then turn on the wifi when connected to it.
Do the opposite if you are using Wifi for the static. 

### Setting up Dynamic VNC via Ethernet, although Wifi can be used. -Dynamic
Once you have VNC enabled in your interfaces, it should automatically start when the Pi is booted, if not, refer to the guide below to make sure it does.

1. Make sure VNC Server launches at startup. 
2. Open VNC Server (VNC logo next to the Wifi icon on the desktop)
3. Make note of the Connected IP Address, write it down somewhere or make a mental note.
4. Go to VNC Viewer on the machine you want to connect with, which needs to be connected to the same network, and add a new connection with either the Connected IP Adress or raspberrypi.local (this may get confusing with multiple Pi's)

Now that you did that, you _should_ be able to connect to your Pi whenever it is connected to the same network. Be weary that the IP address may change if you are on a different network, but hopefully raspberrypi.local finds it. If not, refer to the method talked about earlier. Also note that this Raspberry Pi can still access the World Wide Web. If you do not like that, I strongly encourage you to go the static method as that will be Local only. Yes, you can even access your Raspberry Pi from anywhere in the world with the dynamic option if you purchase a VNC Server license, which can be very handy.  

### Other option for autostart if other doesnt work.

Create a VncServer.desktop file in /home/pi/.config/autostart

you have to create the autostart directory if it is not already: 
```
$ cd /home/pi/.config/
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
