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
