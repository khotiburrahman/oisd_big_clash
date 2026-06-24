import urllib.request
import tldextract
import re

url = "https://raw.githubusercontent.com/sjhgvr/oisd/refs/heads/main/oisd_big.txt"
output_file = "oisd_big.yaml"

try:
    print("Mengunduh file oisd_big.txt...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        # Menggunakan ignore untuk menghindari error karakter non-utf8
        raw_data = response.read().decode('utf-8', errors='ignore')
        lines = raw_data.splitlines()

    unique_domains = set()

    print(f"Total baris mentah yang diunduh: {len(lines)}")
    print("Menganalisa dan mengekstrak domain utama (Apex Domain)...")
    
    for line in lines:
        line = line.strip()
        
        # Abaikan komentar, baris kosong, atau baris penanda syntax adblock
        if not line or line.startswith("#") or line.startswith("!") or line.startswith("["):
            continue
            
        # Bersihkan baris jika ada spasi atau karakter aneh di ujungnya
        # Mengambil kata pertama saja jika dalam satu baris ada spasi (misal format hosts file)
        domain_match = re.search(r'^([a-zA-Z0-9\.\-_]+)', line)
        if not domain_match:
            continue
            
        clean_line = domain_match.group(1).strip().lower()
        
        # Ekstrak domain utama menggunakan tldextract
        ext = tldextract.extract(clean_line)
        if ext.domain and ext.suffix:
            apex_domain = f"{ext.domain}.{ext.suffix}"
            unique_domains.add(apex_domain)

    # Urutkan secara alfabetis
    sorted_domains = sorted(list(unique_domains))

    print(f"Menulis {len(sorted_domains)} domain utama ke {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("payload:\n")
        for domain in sorted_domains:
            f.write(f"  - '+.{domain}'\n")
            
    print("Selesai! File berhasil diperbarui.")

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
