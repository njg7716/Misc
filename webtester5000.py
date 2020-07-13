#!/usr/bin/python3

import subprocess
#Uses cURL to get the status code back from a list of newline separated websites
#It then prints out the website with the status code it got
#I originally did this with the requests library but that can only be redirected 30 times
#cURL can be redirected 50

def main():
    f = open("websites.csv","r")
    f2 = open('results.csv', 'w')
    for site in f:
        site = site.strip()
        cmd = "curl -L --connect-timeout 5 -s -o /dev/null -w \"%{http_code}\" http://" + site
        output = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE)
        output = output.stdout.decode('utf-8')
        if output == '000':
            f2.write(site + "," + "FAILED\n")
        else:
            f2.write(site + "," + output + "\n")
    f2.close()
    f.close()
        
main()
