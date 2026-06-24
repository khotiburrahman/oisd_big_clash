import urllib.request
import re

url = "https://raw.githubusercontent.com/sjhgvr/oisd/refs/heads/main/oisd_big.txt"
output_file = "oisd_big.yaml"

def extract_apex_domain(domain_str):
    """
    Memotong subdomain dan hanya mengambil domain utamanya saja (Apex Domain)
    Menggunakan regex mandiri tanpa perlu library pihak ketiga.
    """
    domain_str = domain_str.strip().lower()
    
    # Pisahkan tiap bagian berdasarkan tanda titik
    parts = domain_str.split('.')
    if len(parts) > 2:
        # Daftar akhiran ganda yang sangat umum (misal: co.id, com.br, net.uk)
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
    print("Mengekstrak Apex Domain secara manual...")
    
    for line in lines:
        line = line.strip()
        
        # Abaikan komentar atau syntax adblock
        if not line or line.startswith(("#", "!", "[")):
            continue
            
        # Ambil susunan karakter domain yang valid saja
        domain_match = re.search(r'^([a-zA-Z0-9\.\-_]+)', line)
        if not domain_match:
            continue
            
        clean_domain = domain_match.group(1).strip('.')
        
        # Ekstrak domain utama
        apex = extract_apex_domain(clean_domain)
        if apex and '.' in apex: # Pastikan hasil ekstraksi valid membentuk domain
            unique_domains.add(apex)

    # Urutkan secara alfabetis
    sorted_domains = sorted(list(unique_domains))

    print(f"Menulis {len(sorted_domains)} domain ke {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("payload:\n")
        for domain in sorted_domains:
            f.write(f"  - '+.{domain}'\n")
            
    print("Selesai! Konversi berhasil dilakukan.")

except Exception as e:
    print(f"Terjadi error: {e}")
