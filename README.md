```markdown
# python-caltest: Basit Bir Python Hesap Makinesi

python-caltest, temel matematiksel işlemleri gerçekleştirebilen basit bir Python hesap makinesidir. Amacı, yeni başlayanlar için Python programlama pratiği yapmak ve basit bir komut satırı aracı örneği sunmaktır.

## Kurulum

### Gerekli Python Sürümü

Bu proje Python 3.6 ve üzeri sürümleriyle uyumludur.

### Kurulum Adımları

1.  **Depoyu klonlayın:**

    ```bash
    git clone <bu_deponun_urlsi>
    cd python-caltest
    ```

2.  **(İsteğe Bağlı) Sanal ortam oluşturun:**

    Bu, projenin bağımlılıklarını sistem genelindeki paketlerden izole etmenize yardımcı olur.

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate.bat  # Windows
    ```

3.  **Bağımlılıkları yükleyin:**

    Bu proje için herhangi bir harici bağımlılık gerekmemektedir. Ancak, `pip`'i güncel tutmanız önerilir.

    ```bash
    pip install --upgrade pip
    ```

### Çalıştırma

Hesap makinesini çalıştırmak için aşağıdaki komutu kullanın:

```bash
python caltest.py
```

Bu komut, hesap makinesini komut satırında başlatacaktır.

## Kullanım Örneği

Hesap makinesi başladıktan sonra, matematiksel ifadeler girerek işlemleri gerçekleştirebilirsiniz.

**Örnek:**

1.  Hesap makinesi konsolunda `2 + 2` yazın ve Enter tuşuna basın.
2.  Sonuç olarak `4` çıktısını almalısınız.
3.  Diğer işlemleri deneyebilirsiniz: `-`, `*`, `/`, `**` (üst alma), `%` (mod alma).

**Örzel Durumlar:**

*   Geçersiz bir ifade girdiğinizde, hata mesajı alırsınız.
*   Hesap makinesinden çıkmak için `exit` yazın ve Enter tuşuna basın.

## Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz, lütfen aşağıdaki adımları izleyin:

1.  Projenin bir kopyasını (fork) oluşturun.
2.  Kendi dalınızı (branch) oluşturun: `git checkout -b yeni-ozellik`
3.  Değişikliklerinizi yapın ve commit'leyin: `git commit -m "Yeni özellik eklendi"`
4.  Değişikliklerinizi uzak depoya gönderin: `git push origin yeni-ozellik`
5.  Bir çekme isteği (pull request) oluşturun.

Katkılarınızın aşağıdaki hususlara dikkat etmesi önemlidir:

*   Kodun temiz ve okunabilir olması
*   Yorum satırlarıyla açıklanmış olması
*   Yeni özellikler için testler yazılması
*   Mevcut testlerin geçmesi

## Lisans

Bu proje MIT Lisansı altında lisanslanmıştır. Lisans metninin tamamı için [LICENSE](LICENSE) dosyasına bakın.

**MIT Lisansı:**

Copyright (c) [YIL] [AD SOYAD]

Bu yazılımın ve ilgili dökümanların bir kopyasını elde eden herkese, kısıtlama olmaksızın, bu yazılımı kullanma, kopyalama, değiştirme, birleştirme, yayınlama, dağıtma, alt lisansını verme ve/veya satma ve bu yazılımın sağlandığı kişilere izin verme hakkı ücretsiz olarak verilir, ancak aşağıdaki koşullara tabidir:

Yukarıdaki telif hakkı bildirimi ve bu izin bildirimi, tüm kopyalarda veya yazılımın önemli kısımlarında yer almalıdır.

YAZILIM "OLDUĞU GİBİ" SAĞLANIR, HERHANGİ BİR AÇIK VEYA ZIMNİ GARANTİ YOKTUR, TİCARİ OLARAK SATILABİLİRLİK, BELİRLİ BİR AMACA UYGUNLUK VE İHLAL ETMEME GARANTİLERİ DAHİL ANCAK BUNLARLA SINIRLI DEĞİLDİR. YAZARLAR VEYA TELİF HAKKI SAHİPLERİ, YAZILIMDAN VEYA YAZILIMIN KULLANIMINDAN VEYA DİĞER İŞLEMLERDEN KAYNAKLANAN, SÖZLEŞMEDE, HAKSIZ FİİLDE VEYA BAŞKA BİR ŞEKİLDE OLMAK ÜZERE, HİÇBİR ZARARDAN, ZARARDAN VEYA DİĞER YÜKÜMLÜLÜKLERDEN SORUMLU DEĞİLDİR.
```
