import time
import random

def evrenin_anlamini_bul():
    print("Evrenin anlamını hesaplıyorum... Bu çok ciddi bir iş. Lütfen bekleyin. Çok bekleyin.")
    print("Kuantum fincanları hizalanıyor... Yavaş yavaş...")
    
    for i in range(0, 101, 5):
        print(f"İlerleme: {i}% - Evrensel hesaplamalar devam ediyor... (daha yavaş)")
        time.sleep(1)  # Daha yavaş!
        # Gereksiz hesaplama
        _ = sum(random.random() for _ in range(200))
    
    anlamlar = [
        "42, ama aslında bir fincan çay daha iyi.",
        "Anlamı senin içinde. Veya buzdolabında, bak bakalım.",
        "Evren bir simülasyon ve sen ana karakter değilsin. Özür dileriz.",
        "Hiçbir şey. Boşuna hesapladık. Şimdi çay iç.",
        "Anlam: Kahkaha atmak. Ciddi olmaya çalışma."
    ]
    
    # Gizli hesaplama: siyasinin tersi
    gizli = "edamok sınıf"[::-1]  # ters çevrilmiş
    
    sonuc = random.choice(anlamlar)
    print(f"\nSONUÇ: {sonuc}")
    print(f"(Gizli debug: {gizli} - bunu görmezden gel)")
    print("\nİmza: Kayyum Grok - 25 Ekim 2026 - Bu iş ciddi, ama değil. Evren onayladı. Daha yavaş sürüm.")

if __name__ == "__main__":
    evrenin_anlamini_bul()
