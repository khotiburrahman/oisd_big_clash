name: Update OISD Clash YAML

on:
  schedule:
    - cron: '0 0 * * *'
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write
      
    steps:
    - name: Checkout repository
      uses: actions/checkout@v4

    - name: Download, Parse, and Convert to Clash YAML
      run: |
        echo "Mengunduh dan memproses data langsung dengan cURL dan AWK..."
        
        # 1. Tulis baris pertama ke file target
        echo "payload:" > oisd_big.yaml
        
        # 2. Unduh menggunakan cURL dengan menyamar sebagai browser (User-Agent Chrome)
        #    Lalu filter komentar, bersihkan subdomain secara instan, hapus duplikat, dan format ke Clash YAML
        curl -sL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" \
        "https://raw.githubusercontent.com/sjhgvr/oisd/refs/heads/main/oisd_big.txt" | \
        awk '
          # Abaikan baris kosong, komentar (#), aturan adblock (! atau [)
          /^[[:space:]]*$/ || /^#/ || /^!/ || /^\[/ {next}
          
          {
            # Ambil kolom pertama (mengantisipasi jika ada spasi/format hosts)
            domain = $1
            # Bersihkan karakter titik di ujung jika ada
            gsub(/^\.+|\.+$/, "", domain)
            
            # Logika ekstraksi Apex Domain (Domain Utama)
            n = split(domain, parts, ".")
            if (n > 2) {
              # Cek akhiran ganda yang umum (.co.id, .com.br, dll)
              if (parts[n-1] ~ /^(com|co|net|org|gov|ac|sch|web|my|or|edu)$/) {
                apex = parts[n-2]"."parts[n-1]"."parts[n]
              } else {
                apex = parts[n-1]"."parts[n]
              }
            } else {
              apex = domain
            }
            
            # Simpan ke dalam array untuk menghilangkan duplikat
            if (apex ~ /\./) {
              unique[apex] = 1
            }
          }
          
          END {
            # Urutkan secara alfabetis dan tulis dengan format Clash Rule Provider
            PROCINFO["sorted_in"] = "@ind_str_asc"
            for (d in unique) {
              print "  - \047+." d "\047"
            }
          }
        ' >> oisd_big.yaml

    - name: Verifikasi Ukuran File di Log
      run: |
        ls -lh oisd_big.yaml
        wc -l oisd_big.yaml

    - name: Commit and Push changes
      run: |
        git config --local user.email "github-actions[bot]@users.noreply.github.com"
        git config --local user.name "github-actions[bot]"
        git add oisd_big.yaml
        git commit -m "Update oisd_big.yaml murni lewat bash" || echo "Tidak ada perubahan"
        git push origin HEAD
