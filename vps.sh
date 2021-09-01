import os, time, sys
import random
from pathlib import Path
from IPython.display import clear_output
import requests
from re import sub

#@title ** NEW  VPS **
x = ! nvidia-smi
ox = ! nvidia-smi -L
xx = '\n'.join(x)
if xx.find("K80") >=0:
  print(" Dapet K80",ox)
  ! kill -9 -1
else:
  print("")
       
mfile = Path("ngrok")
if mfile.is_file():
    print("")
else:
    ! wget  https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip
    ! unzip *.zip
    clear_output()  

print(ox)
# Install useful stuff
! apt install --yes ssh screen nano htop ranger git > /dev/null
# SSH setting
! echo "root:irkop" | chpasswd
! echo "PasswordAuthentication yes" > /etc/ssh/sshd_config
! echo "PermitUserEnvironment yes" >> /etc/ssh/sshd_config
! echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
! service ssh restart > /dev/null


mfile = Path("tok")
if mfile.is_file():
  token = open("tok","r")
  token = token.read()
else:
  # Config Token
  xx = requests.get("https://raw.githubusercontent.com/kopen1/mining/main/token").text
  data= xx.splitlines()
  x = len(data)
  #print("\n\ntotal token : "+str(x))
  token = random.choice(data)
  print("token kamu : "+str(token))


tokek = token
get_ipython().system_raw('./ngrok authtoken $tokek && ./ngrok tcp 22 &')
# Get the address for SSH

r = requests.get('http://localhost:4040/api/tunnels')
str_ssh = r.json()['tunnels'][0]['public_url']
str_ssh = sub("tcp://", "", str_ssh)
str_ssh = sub(":", " -p ", str_ssh)
str_ssh = "ssh root@" + str_ssh
print(str_ssh)
f = open("token","a")
f.write(token)
f.close()
