# Combined Ads, Trackers, & Reject Rules

### 📊 Statistik Pembaruan Terakhir
* **Waktu Pembaruan:** 2026-10-31 03:07:45 UTC
* **Total Domain Unik:** **297232 domain**

### 📁 File Output & Kompatibilitas

#### Sing-box Rule-Set (.srs)
| File | Rule-Set Version | Kompatibel dengan |
|---|---|---|
| `geosite-ads-all-v1.srs` | 1 | sing-box 1.8.0 – 1.9.x |
| `geosite-ads-all-v2.srs` | 2 | sing-box 1.10.x |
| `geosite-ads-all-v3.srs` | 3 | sing-box 1.11.x |
| `geosite-ads-all-v4.srs` | 4 | sing-box 1.11.0+ (1.12.x, 1.13.x, 1.14.x) |
| `geosite-ads-all.srs` | default (latest compiler) | sing-box versi terbaru |

#### Sing-box Rule-Set Source (.json)
Tersedia `geosite-ads-all-v1.json` s/d `geosite-ads-all-v4.json` dan `geosite-ads-all.json` (default version 2).

#### Format Lain
| File | Format | Untuk |
|---|---|---|
| `geosite.dat` | Protobuf v2fly (tag `ads`) | Xray, V2Ray, V2RayNG **saja** — tidak untuk sing-box 1.12+ |
| `oisd_big.yaml` | Clash Modern (`+.domain`) | OpenClash, Clash Meta, Mihomo |
| `oisd_big_old.yaml` | Clash Legacy (`DOMAIN-SUFFIX`) | Clash lama |
| `rules.txt` | Plain Text | Universal |

### 💡 Rekomendasi per Aplikasi
* **NekoBox 1.4.x (sing-box 1.12+)** → gunakan `geosite-ads-all-v4.srs` via Custom Config `rule_set`
* **NekoBox lama (sing-box 1.8–1.9)** → gunakan `geosite-ads-all-v1.srs`
* **SFA / SFI / SFM (sing-box)** → gunakan `geosite-ads-all-v2.srs` atau `.srs` default
* **V2RayNG / Xray** → gunakan `geosite.dat` (tag `ads`)
* **OpenClash / Clash Meta** → gunakan `oisd_big.yaml`
