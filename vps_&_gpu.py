# -*- coding: utf-8 -*-
"""vps & GPU

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/kopen1/mining/blob/main/VPS_%26_GPU.ipynb
"""

#@title ** CHECK GPU **
gpu_info = ! nvidia-smi
gpu_info = '\n'.join(gpu_info)
if gpu_info.find('V100') >=0:
  print(gpu_info)
elif gpu_info.find('P100') >=0:
  print(gpu_info)
elif gpu_info.find('T4') >=0:
  print(gpu_info)
elif gpu_info.find('P4') >=0:
  print(gpu_info)
elif gpu_info.find('K80') >=0:
  print("YAAH DAPET K80")
else :
  print("GPU HARI INI HABIS | BESOK LAGI COK")

from IPython.display import clear_output
 
#@title **install ssh/vps**
 
! apt install --yes ssh screen nano htop ranger git > /dev/null
 
! echo "root:irkop" | chpasswd
 
! echo "PasswordAuthentication yes" > /etc/ssh/sshd_config
 
! echo "PermitUserEnvironment yes" >> /etc/ssh/sshd_config
 
! echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
 
! service ssh restart > /dev/null
 
#ngrok
 
from pathlib import Path
my_file = Path("ngrok")
if my_file.is_file():
    print ("ada")
else:
 ! wget  https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip 
 ! unzip *.zip
 
 
clear_output()
 
# Run ngrok
 
authh = "" #@param {type:"string"}
 
get_ipython().system_raw('./ngrok authtoken $authh && ./ngrok tcp 22 &')
 
! sleep 3
 
# Get the address for SSH
 
import requests
 
from re import sub
 
r = requests.get('http://localhost:4040/api/tunnels')
 
str_ssh = r.json()['tunnels'][0]['public_url']
 
str_ssh = sub("tcp://", "", str_ssh)
 
str_ssh = sub(":", " -p ", str_ssh)
 
str_ssh = "ssh root@" + str_ssh
 
print(str_ssh)

#@title **CPU**
! wget https://github.com/xmrig/xmrig/releases/download/v6.14.1/xmrig-6.14.1-linux-x64.tar.gz && tar -zxf xmrig-6.14.1-linux-x64.tar.gz && cd xmrig-6.14.1 && ./xmrig -o randomxmonero.eu-west.nicehash.com:3380 -u 32iEJV5mhEZmybiLXcLWYDQvhTrv53PJnG.cpu --randomx-1gb-pages -p x -k -a rx/0 -t 8 --nicehash --max-cpu-usage 70 --cpu-priority 5

#@title **GPU**
! wget https://github.com/NebuTech/NBMiner/releases/download/v39.1/NBMiner_39.1_Linux.tgz && sudo tar -xvf NBMiner_39.1_Linux.tgz && cd NBMiner_Linux && sudo ./nbminer  -a ethash -o stratum+tcp://daggerhashimoto.eu-west.nicehash.com:3353 -u 32iEJV5mhEZmybiLXcLWYDQvhTrv53PJnG.irkop

#@title ** Sleep **
from IPython.display import clear_output
 
  
j = 23
while j > 0 :
  clear_output(j)
  m = 59
  while m > 0:
   clear_output(m)
   s = 59
   while s > 0:
     clear_output(s)
     ! sleep 1
     print("Sleeping ",j,":",m,":",s)
     s -= 1
   m -= 1
  j -=1