#!/bin/bash

x=1

ip='10.8.0.1'
#ip='wp.pl'
#ip='8.8.8.8'

#ToDo='reboot'
ToDo='/bin/bash /home/aibree_eNOS/_runose/sakisreload.sh'


for i in {1..2}
do
  sleep 1
  if ping -c 1 $ip &> /dev/null
  then
    echo 1 $(date) >> /home/aibree_eNOS/_runose/1.log
  else
    echo 0 $(date) >> /home/aibree_eNOS/_runose/1.log
    if ping -c 1 $ip &> /dev/null
    then
      echo 01--- $(date) >> /home/aibree_eNOS/_runose/1.log
      ((x++))
    else
      echo 00--- $(date) >> /home/aibree_eNOS/_runose/1.log
      ((x--))
    fi
  fi

if [ $x -lt 0 ]
then
  echo 000----- $(date) >> /home/aibree_eNOS/_runose/1.log
  sudo $ToDo
else
  echo 111----- $(date) >> /home/aibree_eNOS/_runose/1.log
fi

done
