# unified_enum.py

import requests
import threading
import dns.resolver
import os
from datetime import datetime

# Config
default_records = ['A', 'AAAA', 'MX', 'TXT', 'SOA', 'CNAME']
thread_limit = 20
output_dir = 'reports'

# Globals
discovered_subdomains = []
dns_records = {}
lock = threading.Lock()

os.makedirs(output_dir, exist_ok=True)

def check_subdomain(subdomain, domain):
    for protocol in ['http', 'https']:
        url = f"{protocol}://{subdomain}.{domain}"
        try:
            res = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
            if res.status_code < 400:
                with lock:
                    discovered_subdomains.append(f"{subdomain}.{domain}")
                break
        except requests.RequestException:
            continue

def enumerate_subdomains(domain, subdomains_file='subdomains.txt'):
    discovered_subdomains.clear()
    with open(subdomains_file) as f:
        sub_list = f.read().splitlines()

    threads = []
    for sub in sub_list:
        while threading.active_count() > thread_limit:
            pass
        t = threading.Thread(target=check_subdomain, args=(sub, domain))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
    return discovered_subdomains

def enumerate_dns(domain):
    dns_records.clear()
    resolver = dns.resolver.Resolver()

    for record in default_records:
        try:
            answers = resolver.resolve(domain, record)
            dns_records[record] = [str(rdata) for rdata in answers]
        except Exception:
            dns_records[record] = []
    return dns_records

def generate_markdown(domain):
    filename = os.path.join(output_dir, f"{domain}.md")
    with open(filename, 'w') as f:
        f.write(f"# Recon Report for `{domain}`\n")
        f.write(f"_Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}_\n\n")

        # Subdomains
        f.write("## 🛰️ Discovered Subdomains\n")
        if discovered_subdomains:
            for sub in discovered_subdomains:
                f.write(f"- http://{sub}\n")
        else:
            f.write("No subdomains found.\n")
        f.write("\n")

        # DNS
        f.write("## 🌐 DNS Records\n")
        for rtype, records in dns_records.items():
            f.write(f"### {rtype} Records\n")
            if records:
                for r in records:
                    f.write(f"- {r}\n")
            else:
                f.write("- No records found\n")
            f.write("\n")
    return filename

