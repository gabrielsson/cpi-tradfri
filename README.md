# ![Clock Work Pi Tradfri](cpi-tradfri.png)
Install this either on your computer or your GameSH>

## Install pygame on python3 
```
sudo apt-get update

sudo apt-get build-dep python-pygame

pip3 install pygame
```

## Install lib coap
https://github.com/ggravlingen/pytradfri/blob/master/script/install-coap-client.sh

but with ``sudo make install`` in the last step

## Install py tradfri
```
pip3 install pytradfri
```
## Install on GameSH>
ssh to your gameshell
```
cd apps/launcher/Menu/GameShell
git clone https://github.com/gabrielsson/cpi-tradfri.git
```
## Properties file
Make sure to fill out the tradfri.properties file with IP and key to your IKEA gateway
```
cd cpi-tradfri
nano tradfri.properties
```
