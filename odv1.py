import streamlit as st

st.title("Ev Yatırımı Simülasyonu")

ev_fiyati = st.number_input("Ev Fiyatı (₺)", value=1250000, step=50000)
kira = st.number_input("Aylık Kira Geliri (₺)", value=8000, step=500)
birikim = st.number_input("Aylık Birikim (₺)", value=3000, step=500)
pesinat_orani = st.slider("Peşinat Oranı (%)", 10, 50, 20) / 100
kredi_suresi = st.number_input("Kredi Süresi (yıl)", value=15, step=1)


baslangic_yasi = st.number_input("Birikime Başlangıç Yaşı", min_value=15, max_value=80, value=25, step=1)
bitis_yasi = st.number_input("Birikimin Bitiş Yaşı", min_value=baslangic_yasi+1, max_value=100, value=65, step=1)


toplam_ay = (bitis_yasi - baslangic_yasi) * 12
pesinat = ev_fiyati * pesinat_orani
kalan_kredi = ev_fiyati - pesinat
kredi_taksit = kalan_kredi / (kredi_suresi * 12)

aylik_nakit = 0
birikim_miktari = 0
ev_sayisi = 0
aktif_krediler = []

for ay in range(1, toplam_ay + 1):
    kira_toplam = ev_sayisi * kira
    kredi_odeme = sum(aktif_krediler)
    aylik_nakit = birikim + kira_toplam - kredi_odeme
    birikim_miktari += aylik_nakit

    if birikim_miktari >= pesinat:
        ev_sayisi += 1
        birikim_miktari -= pesinat
        aktif_krediler.append(kredi_taksit)

    if ay % (kredi_suresi * 12) == 0 and aktif_krediler:
        aktif_krediler.pop(0)

st.success(f"{baslangic_yasi} yaşında başlayıp {bitis_yasi} yaşına geldiğinde {ev_sayisi} eve sahip olursun.")
st.info(f"Aylık toplam kira getirisi: {ev_sayisi * kira:,.0f} ₺")
