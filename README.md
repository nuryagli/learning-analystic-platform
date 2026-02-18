# Learning Analytics Platform
### Personal Data Analysis Project | Python

## Problem
Online eğitim platformlarında öğrencilerin gerçekten öğrenip öğrenmediklerini anlamak zordur.  
Derslere katılım tek başına öğrenme kalitesini ölçmek için yeterli değildir.  
Eğitmenlerin ve eğitim ürünleri geliştiren ekiplerin, öğrenci performansını veriyle analiz edebileceği
temel metriklere ihtiyacı vardır.

## Purpose
Bu proje, öğrenci performans verilerini analiz ederek:
- Genel başarı seviyesini ölçmeyi
- Konu bazlı öğrenme zayıflıklarını tespit etmeyi
- Zaman içinde gelişim trendlerini incelemeyi
amaçlayan basit bir learning analytics prototipidir.

Proje, **veri analizi ve raporlama mantığını** göstermek amacıyla geliştirilmiştir.

## Target Users
- Eğitmenler
- Online eğitim içerik üreticileri
- Eğitim ürünleri geliştiren ekipler

## Dataset
Projede örnek (mock) eğitim verileri kullanılmıştır:
- Öğrenci kimlik bilgileri
- Quiz sonuçları
- Konu bazlı başarı skorları
- Zaman damgalı performans kayıtları

Veri yapısı, gerçek bir eğitim platformundan elde edilebilecek temel analiz ihtiyaçlarını
yansıtacak şekilde tasarlanmıştır.

## Key Metrics & Analysis
Projede hesaplanan temel analizler:
- **Student-level average score** (öğrenci bazlı ortalama başarı)
- **Class-level performance average**
- **Topic-based weakness analysis** (konu bazlı zayıflık tespiti)
- **Performance trend analysis over time** (başlangıç – bitiş karşılaştırması)

Bu metrikler, eğitim içeriğinin hangi konularda iyileştirilmesi gerektiğini
göstermeyi hedefler.

## Output
Analiz sonuçları:
- Python fonksiyonları ile hesaplanır
- JSON formatında raporlanır
- Konsol çıktısı olarak özetlenir

Üretilen raporlar, ileride dashboard veya BI araçlarıyla
görselleştirilebilecek şekilde yapılandırılmıştır.

## Technologies
- Python
- Standard Library (datetime, json)
- Data aggregation & analysis logic

## Notes
Bu proje bir **production sistemi değildir**.  
Amaç:
- Veri analizi yaklaşımını
- Metrik tanımlama ve yorumlama becerisini
- Temiz ve okunabilir analiz kodu yazımını
göstermektir.

Gelecekte:
- SQL tabanlı veri kaynağı
- Basit bir dashboard
- Daha gelişmiş istatistiksel metrikler
eklenebilir.
