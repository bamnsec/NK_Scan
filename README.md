README

Welcome to NKscan, a simple python script, mostly drawn from the python-libnmap documentation
in an attempt to work through the process of actually learning how to write effective code.
The initial version of this script was written in python-nmap, but the python-libnmap 
library is much more flexible and generates better output, it is also runs on parallel
threads, according to the documentation, which may explain the vast speed improvement when
running scans.

This project is the result of months of research and scanning of the externally facing
North Korean internet, which is around 1500 IP addresses.  The wider project was undertaken 
both to learn how to more effectively learn to use nmap on large networks, but also to explore
 the uses of technical tools in developing political analysis, even in conditions where 
information is often distorted and limited.

Through this project I have collected dozens of scan results, using various nmap
option configurations, and have come to what I have found to be the most bountiful 
and robust results.  These scans have a number of hurdles to overcome.  Firstly, 
information on North Korea is extremely limited, and the information about technical
infrastructure is even more limited.  Secondly, at times of heightened tensions on the
Korean peninsula certain types of scans tend to be blocked, systems are taken off line, 
and firewalls become tightened up, making the extraction of results difficult. 
This and other complications have made this project difficult to undertake, and many weeks
of experimentation has gone into the development of the scan process outlined in this script.


When these obstacles are overcome, however, the results can provide an interesting insight
into the mentalities, conflictual posture and security approaches of a regime that those
on the outside have little understanding of.  Often these scans are done around times of 
tension, and a lot of oddly numbered open ports are observed coming from limited IP ranges.  
When compared to scans that attempted to geolocate these IPs, which are located outside of
Pyongyang and near a large military base, and when compared to scans in times of lower 
tension, where the same number of open onddly numbered ports do not appear, this can provide 
the basis to examine past North Korean digital operations, and correlate data.  This is one
of many points of data that came from this research


Some notes on the options selected:

-n : Prevents nmap from attempting to resolve DNS for each IP.  Given the internal structure of 
what can aptly be described as an intranet in North Korea, there are few DNS entries to begin 
with, and this option makes the scan significantly more efficient.

-sT : TCP scans seem to work better than SYN or ACK scans.  This is likely due to a security
configuration that blocks all SYN and ACK scans, and only allows full TCP connections.  It is 
less stealthy, but it works more consistently than other options.

-A : Information can be difficult to gather, due to specific configurations, odd ports, out
of date software and so on, and using aggressive scanning allows for the maximum amount of
information to be gathered without resorting to using numerous NSE scripts (though awesome, NSE 
scripts take a long time to run, depending on the script and number being run)

-p 1-65535: I scan the entire port range for a simple reason, sketchy stuff tends to run on high
numbered ports outside of common ports.  Part of this project is to understand North Korean digital
operations in relation to the outside world, and to understand internal technical infrasture, and 
this work often involves anomaly detection and comparative analysis.  Scanning uncommon ports is 
useful in this sort of analysis.

-vvv : Often these scans will terminate without warning, and it is important to understand why this 
may be the case.  Though the output will not display when running the script, it will display errors
in the text file output file that is generated during the scan.  The use of robust verbosity during 
scans helped identify forms of blocking, delays in traffic, the blocking of IP addresses I was scanning
from and so on.

-T4 : Throttling the scan to level 4 is purely for efficiency.  I have also found that the scan is less 
likely to be blocked if it runs quickly.

Unfortunately the python-libnmap library does not like text output, which is important for the differential
study that I have been running.  So, to still get the output in txt format run:
python nk_scan.py >> output.txt


Also, feel free to change the options, modify the script and use it to scan other port ranges, and improve the
script as you see fit.

Note: Expect scans to take a significant amount of time, sometimes up to a day, to run.  This depends on a number 
of factors, including internal political situation (whether they are taking evasive measures or blocking scans), 
whether the user is using a VPN (which is recommended unless scanning from a VPS), and connection speed.

Dependencies
python-libnmap

pip install python-libnmap

Usage

git clone repository into directory of one's choosing
cd NKscan
python NKscan.py
