#IT WORKS!!!!!!!!!!!!!!!!!!!!!!
import nmap

print """



.__   __.  __  ___         _______.  ______     ___      .__   __. 
|  \ |  | |  |/  /        /       | /      |   /   \     |  \ |  | 
|   \|  | |  '  /        |   (----`|  ,----'  /  ^  \    |   \|  | 
|  . `  | |    <          \   \    |  |      /  /_\  \   |  . `  | 
|  |\   | |  .  \     .----)   |   |  `----./  _____  \  |  |\   | 
|__| \__| |__|\__\    |_______/     \______/__/     \__\ |__| \__| 
                                                                   





::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
                                                                                                                        
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~       ~       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~        ~~~        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~         ~~~         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~         ~~~~~         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~          ~~~~~          ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~     ~~~~~~~~~~~~~~~~~     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~       ~~~~~~~~~~~~~       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~         ~~~~~~~~~         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~       ~~~~~~~~~~~       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~       ~~~~~~~~~~~       ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~     ~~~~      ~~~     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~     ~~         ~~    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~                   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~               ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~         ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                                                                                                                        
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::


"""





nm = nmap.PortScanner()

nm.scan(hosts='175.45.176.0/22 210.52.109.0/24 77.94.35.0/24', arguments='-n -sT -A -p 1-65535 -vvv -T4 -oN output.txt')
#insert NK ranges into hosts

for host in nm.all_hosts():
  print('----------------------------------------------------')
  print('Host : %s (%s)' % (host, nm[host].hostname()))
  print('State : %s' % nm[host].state())

for proto in nm[host].all_protocols():
  print('----------')
  print('Protocol : %s' % proto)

  lport = nm[host][proto].keys()
  lport.sort()
  for port in lport:
    print('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))

print('----------------------------------------------------')
print ""
print ""
print "The Scan Has Completed"
print ""
print "The Great Leader Honors and Praises You"
print """

                                                                           
                                   `.'''''.                                
                              .@@@@@@@@@@@@@;                              
                             :@@@;@@;    @@@@'                             
                            @@@.@ .`,+` '.@@@@                             
                           @@:  @@@@@@@@; .;@@+                            
                          ;@@'#@#     :+@@`@@@;                            
                          @@# @`          @@@@+                            
                          #@@@:           @@@@@                            
                           #@@             ,@@@                            
                   #@       @@              .@@                            
                  @@@      ,@   `   '@;;     @@                            
                 @@#@@     :@         `     ;@@@                           
                 @ :@@     :@  :@@  @.`..`  ;;@@                           
                @@ @#@     +@ ..'; + ,     ;@ @@                           
               #@ ;'@@     #@      #`     @+  @@                           
              `@ .':@      #@   `. ' @    ` , @@                           
              @+ +;,@:     #@   @',#@ #  +   :@                            
             ;@ @#`'@@@    #@  ,.     :    `@@                             
             @; ;  `@@@;   +@, `'''+.@;    `@@                             
            ;@  .# @ `@`   '@@   ';+.     . @@                             
            @# :@' , ;@     @@    . `   @ @ @@                             
           .@,  @    @:     @@'   @@#,  .` `@@                             
           :@   @   ++      ,@@+.      @   @@@                             
           ;@   @   @.       @@@@'   :@  `@.:@+,                           
           @'      @.         ;@#; +'   :@   @@@@@@@+                      
           @+ ,`',@@:           @@`@@@ @'    @,,,#@@@@@@                   
          #@.  `'@@       :+'#@@; @  '#     @      .'@@@@@,                
         ;@@   `@@   `:+@@@@@@@@   :#      ,+          +@@@@               
         @ #;  ,@@``@@@@@@'..`+,  :@@;    `@             ,@@               
        @    ';@@@ ;@        @`   @;@@   '@               #@`              
       ,'  , @@ @; @+       +@`  '@:@@@:'`               :@@@`             
       @   `.:  @# @        @@@@;#   @@@                 @ @@@             
      +#  .'#  .@@@@.        +@@@                       '  #@@@            
      @   `;@ `'@@@:                                    ;@'  @@            
     .@     ,` `;@`                       #@@'        `@@  , @@#           
     +@    ` `: '                ,:      @`  '@       :# ,'   @@,          
     #@    '@  .                 # '.    @,   @       @`@`    '@@          
     @@   #@   +    `@@;         ;#      ;+@@##       @,       @@@         
     @@  @@     ;  :@@@@@@@@`            :@@@@@@@@@@ .@;        @@@        
     @@ .'      +  @,  :'@@@@           :#++';###+@@``@@         @@;       
     @#   :+ +  +  @       @@           @'        `@. @@         `@@       
     @@ @.  @ . # '@@`     @:           @@         @  ;@,         @@,      
     @@@   @#,  #  @@@@@@@@;            @@@@@@@@@@@'  @@@         .@@      
     @@@ :@' `  @   +####'               +'''''++::   @@@          @@:     
    ``@@@@@#@,,:@               #'                     @@      ##:.:@@     
       +@@@@@@@'               ' ,'                    @+:          @@;    
            .@@@@                                                   :@+    
              '@@@                                                   @@    
                @#                                                   @     
"""

