```python
def hesap_makinesi():
  """
  Basit bir hesap makinesi. Kullanıcıdan iki sayı ve bir işlem türü alır,
  sonucu döndürür.

  Desteklenen işlemler:
    - Toplama (+)
    - Çıkarma (-)
    - Çarpma (*)
    - Bölme (/)
  """

  try:
    # Kullanıcıdan ilk sayıyı al
    sayi1 = float(input("İlk sayıyı girin: "))

    # Kullanıcıdan ikinci sayıyı al
    sayi2 = float(input("İkinci sayıyı girin: "))

    # Kullanıcıdan işlem türünü al
    islem = input("İşlem türünü girin (+, -, *, /): ")

    # İşlem türüne göre hesaplama yap
    if islem == "+":
      sonuc = sayi1 + sayi2
    elif islem == "-":
      sonuc = sayi1 - sayi2
    elif islem == "*":
      sonuc = sayi1 * sayi2
    elif islem == "/":
      # Sıfıra bölme hatasını kontrol et
      if sayi2 == 0:
        print("Hata: Sıfıra bölme!")
        return  # Fonksiyonu sonlandır
      else:
        sonuc = sayi1 / sayi2
    else:
      print("Hata: Geçersiz işlem türü!")
      return  # Fonksiyonu sonlandır

    # Sonucu yazdır
    print("Sonuç:", sonuc)

  except ValueError:
    print("Hata: Geçersiz sayı girişi!")
  except Exception as e:
    print("Bir hata oluştu:", e)


# Hesap makinesini çalıştır
hesap_makinesi()
```

**Kodun Açıklaması:**

1.  **`hesap_makinesi()` fonksiyonu:**
    *   Hesap makinesinin tüm işlevlerini içeren ana fonksiyon.
    *   `try...except` bloğu ile hataları ele alır. Bu, programın kullanıcı hataları veya beklenmedik durumlar nedeniyle çökmesini önler.
    *   Docstring (üç tırnak içindeki metin) fonksiyonun ne yaptığını açıklar.

2.  **Kullanıcıdan Giriş Almak:**
    *   `input()` fonksiyonu, kullanıcıdan girdi almak için kullanılır.
    *   `float()` fonksiyonu, kullanıcının girdiği metni ondalıklı sayıya dönüştürür. Bu, toplama, çıkarma vb. gibi matematiksel işlemleri yapabilmemiz için gereklidir.
    *   Hata durumunda (kullanıcı sayı yerine metin girerse), `ValueError` hatası oluşur ve ilgili `except` bloğu çalışır.

3.  **İşlem Türünü Kontrol Etmek ve Hesaplama Yapmak:**
    *   `if...elif...else` blokları, kullanıcının girdiği işlem türüne göre farklı hesaplamalar yapmak için kullanılır.
    *   Bölme işleminde, `sayi2`'nin sıfır olup olmadığını kontrol ederek "Sıfıra bölme" hatasını önler.

4.  **Sonucu Yazdırmak:**
    *   `print()` fonksiyonu, hesaplamanın sonucunu kullanıcıya göstermek için kullanılır.

5.  **Hata Yönetimi:**
    *   `try...except` bloğu, olası hataları yakalamak ve programın çökmesini önlemek için kullanılır.
    *   `ValueError` hatası, kullanıcının sayı yerine metin girmesi durumunda oluşur.
    *   `Exception` hatası, diğer beklenmedik hataları yakalamak için kullanılır.

6.  **Fonksiyonu Çağırmak:**
    *   `hesap_makinesi()` fonksiyonu, programın sonunda çağrılır ve hesap makinesi çalışmaya başlar.

**Kodun Çalışma Şekli:**

1.  Program çalıştırıldığında, `hesap_makinesi()` fonksiyonu çağrılır.
2.  Fonksiyon, kullanıcıdan ilk sayıyı, ikinci sayıyı ve işlem türünü girmesini ister.
3.  Girilen bilgilere göre, doğru hesaplama yapılır.
4.  Hesaplama sonucu ekrana yazdırılır.
5.  Hata oluşursa, ilgili hata mesajı yazdırılır.

**Bu kodu daha da geliştirmek için:**

*   Daha fazla işlem türü ekleyebilirsiniz (örneğin, üs alma, karekök alma).
*   Kullanıcıya daha iyi bir arayüz sunabilirsiniz (örneğin, menü tabanlı bir arayüz).
*   Sonuçları kaydetme özelliği ekleyebilirsiniz.
*   Daha karmaşık işlemleri desteklemek için kütüphanelerden yararlanabilirsiniz (örneğin, `math` kütüphanesi).
