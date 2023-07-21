import re
import requests

def regex_dns(domain):
    regex_dns = r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&//=]*)"
    regex_ip = r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"


    matches = re.finditer(regex_dns, domain, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        match = match.group()
        # matches = re.finditer(regex_ip, match, re.MULTILINE)
        x = re.search(regex_ip, match)
        if  x==None:
            # print (f"{match}")
            return str(match)
            