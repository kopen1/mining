# mining 

<h2>create ssh/vps account</h2>

<a href="https://bit.ly/web_vps"> Click Me </a>



script gpu minerhash :
apt update && apt upgrade && apt install screen && wget https://dl.nbminer.com/NBMiner_39.7_Linux.tgz && tar -xvf NBMiner_39.7_Linux.tgz && cd NBMiner_Linux && screen -d -m ./nbminer -a ethash -o nicehash+tcp://daggerhashimoto.eu.nicehash.com:3353 -u 34Z39DUDyM3z9vpawosH2ScWSpoYvMSZYV.kpn_ -lhr-mode 1 -lhr 74 && screen -ls
