# NGTraining
Projects for the National Guard

# webLogAnalyzer

The webLogAnalyzer.py script will run against a web server log and output the top ten IPs, Paths and Request Types.  

TO DO:
1. Pull out all of the POST commands that had a success code of 200.
2. Pull any base64 encoded commands.
3. Add base64 decode functionality.
4. Output results to .log or .txt.
5. Add argparse so input flags can be used.


Sample output (1/9/2019)

Top Ten IPs
Count		    IPs
411453    	216.86.147.105
155113    	66.249.79.52
33943     	52.7.141.1
22517     	50.200.217.246
17976     	52.4.143.42
17225     	125.10.238.32
16135     	50.206.111.54
15409     	66.249.79.55
11601     	66.249.79.246
11136     	216.244.66.239



Top Ten Paths
Count		    Paths
67721     	/
55644     	/autodiscover/autodiscover.xml
22502     	/misc/jquery.once.js?v=1.2
21774     	/sites/all/themes/aaaa/images/logo.png
20663     	/sites/all/themes/aaaa/images/translate.png
20657     	/sites/all/modules/extlink/extlink_s.png
20570     	/sites/all/themes/aaaa/images/youtube-menu-icon.png
20528     	/sites/all/themes/aaaa/images/facebook-menu-icon.png
20527     	/sites/all/themes/aaaa/images/twitter-menu-icon.png
15159     	/system/ajax



Top Ten Request Types
Count		    Request Types
2586513   	GET
120644    	POST
13627     	-
4539      	HEAD
69        	OPTIONS
43        	PROPFIND
36        	
6         	TRACE
4         	PUT
3         	quit
