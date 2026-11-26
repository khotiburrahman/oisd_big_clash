# Combined Ads, Trackers, & Reject Rules

### 📊 Statistik Pembaruan Terakhir
* **Waktu Pembaruan:** 2026-11-26 06:57:29 UTC
* **Total Domain Unik:** **377413 domain**
* **Aturan Path Diabaikan (Anti False-Positive):** 20805 baris

### 📁 File Output & Kompatibilitas

#### Sing-box Rule-Set (.srs)
| File | Compiler Version | Kompatibel dengan |
|---|---|---|
| `geosite-ads-all-v1.srs` | sing-box 1.9.7 (SRS v1) | sing-box 1.8.0 – 1.9.x |
| `geosite-ads-all-v2.srs` | sing-box 1.10.7 (SRS v2) | sing-box 1.10.x |
| `geosite-ads-all.srs` | sing-box 1.11.5 (SRS v3) | sing-box 1.11.0+ / 1.12+ / terbaru |

#### Format Lain
| File | Format | Untuk |
|---|---|---|
| `geosite.dat` | Protobuf v2fly (tag `ads`) | Xray, V2Ray, V2RayNG |
| `oisd_big.yaml` | Clash Modern (`+.domain`) | OpenClash, Clash Meta, Mihomo |
| `oisd_big_old.yaml` | Clash Legacy (`DOMAIN-SUFFIX`) | Clash lama |
| `rules.txt` | Plain Text | AdGuard Home / Pi-hole / Dnsmasq |

