import subprocess
def main(ip_siem,port_siem):
    data=f'''$ModLoad imfile

# dns request log
$InputFileName /var/log/dns-sinkhole/*.log
$InputFileTag dns-request:
$InputFileStateFile state_file_dns_request
$InputFileFacility local6
$InputFileSeverity info
$InputRunFileMonitor
$InputFilePollInterval 10

if $programname == "dns-request" then @@{ip_siem}:{port_siem}
& stop'''
    f = open("/etc/rsyslog.d/10-dnsfile.conf", "w+")
    f.write(data)
    f.close()
    subprocess.getoutput(f"systemctl restart rsyslog.service")