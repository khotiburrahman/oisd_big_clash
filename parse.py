import urllib.request
import tldextract

url = "https://raw.githubusercontent.com/sjhgvr/oisd/refs/heads/main/oisd_big.txt"
output_file = "oisd_big.yaml"

try:
    print("Mengunduh file oisd_big.txt...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        lines = response.read().decode('utf-8').splitlines()

    unique_domains = set()

    print("Menganalisa dan mengekstrak domain utama (Apex Domain)...")
    for line in lines:
        line = line.strip()
        # Lewati baris kosong, komentar (#), atau aturan kosmetik (!)
        if not line or line.startswith("#") or line.startswith("!"):
            continue
        
        # Ekstrak domain utama menggunakan tldextract
        ext = tldextract.extract(line)
        if ext.domain and ext.suffix:
            apex_domain = f"{ext.domain}.{ext.suffix}"
            unique_domains.add(apex_domain)

    # Urutkan secara alfabetis agar rapi
    sorted_domains = sorted(list(unique_domains))

    print(f"Menulis hasil ke {output_file}...")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("payload:\n")
        for domain in sorted_domains:
            # Format Clash Rule Provider (Domain)
            f.write(f"  - '+.{domain}'\n")
            
    print(f"Selesai! Berhasil menyaring menjadi {len(sorted_domains)} domain utama.")

except Exception as e:
    print(f"Terjadi kesalahan: {e}")
