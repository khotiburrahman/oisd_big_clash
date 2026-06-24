# OISD Big & LoyalSoldier Reject Combined for Clash

Repositori ini otomatis mengunduh, menggabungkan, dan menyaring data dari **OISD Big** dan **LoyalSoldier Reject List** menjadi satu file aturan (*Rule Provider*) Clash.

### 📊 Statistik Pembaruan Terakhir
* **Waktu Pembaruan:** 2026-06-24 22:27:26 UTC
* **Total Domain Mentah Diunduh:** 333399 domain
* **Total Domain Identik/Duplikat yang Dibuang:** 84149 domain
* **Total Domain Unik Akhir (di file YAML):** **249250 domain**

### 🔗 Link Rule Provider Clash
```yaml
rule-providers:
  oisd_big:
    type: http
    behavior: domain
    url: "https://raw.githubusercontent.com/khotiburrahman/oisd_big_clash/main/oisd_big.yaml"
    path: ./providers/oisd_big.yaml
    interval: 3600
```
