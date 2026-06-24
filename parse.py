import urllib.request
import re
import os

# Memastikan file disimpan di direktori kerja GitHub Actions yang aktif
current_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(current_dir, "oisd_big.yaml")

url = "https://raw.githubusercontent.com/sjhgvr/oisd/refs/heads/main/oisd_big.txt"

def extract_apex_domain(domain_str):
    domain_str = domain_str.strip().lower()
    parts = domain_str.split('.')
    if len(parts) > 2:
        if parts[-2] in ['com', 'co', 'net', 'org', 'gov', 'ac', 'sch', 'web', 'my', 'or', 'edu']:
            return '.'.join(parts[-3:])
        else:
            return '.'.join(parts[-2:])
    return domain_str

try:
    print("Mengunduh file oisd_big.txt...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        raw_data = response.read().decode('utf-8', errors='ignore')
        lines = raw_data.splitlines()

    unique_domains = set()
    print(f"Total baris masuk: {len(lines)}")
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith(("#", "!", "[")):
            continue
            
        domain_match = re.search(r'^([a-zA-Z0-9\.\-_]+)', line)
        if not domain_match:
            continue
            
        clean_domain = domain_match.group(1).strip('.')
        apex = extract_apex_domain(clean_domain)
        if apex and '.' in apex:
            unique_domains.add(apex)

    sorted_domains = sorted(list(unique_domains))
    print(f"Menemukan {len(sorted_domains)} domain utama yang unik.")

    # Tulis ulang file secara total (mengganti isi lama)
    print(f"Menulis hasil ke: {output_file}")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("payload:\n")
        for domain in sorted_domains:
            f.write(f"  - '+.{domain}'\n")
            
    print("Proses penulisan skrip selesai dengan sukses.")

except Exception as e:
    print(f"Terjadi error: {e}")
