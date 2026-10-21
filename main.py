import pandas as pd
import streamlit as st

# ==========================================
# 1. SAYFA YAPILANDIRMASI VE ÇOCUK TEMA BİLEŞENLERİ
# ==========================================
st.set_page_config(
    page_title="Minik Âlimler - Etkinlikli İslam Portalı",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Çocuk dostu, interaktif CSS Tasarımı
st.markdown(
    """
<style>
    .main {
        background-color: #F4F7FB;
    }
    .card-container {
        background-color: #FFFFFF;
        border-radius: 20px;
        padding: 24px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.05);
        border: 2px solid #E2E8F0;
        margin-bottom: 25px;
    }
    .category-badge {
        background-color: #E0F2FE;
        color: #0369A1;
        font-size: 14px;
        font-weight: bold;
        padding: 6px 14px;
        border-radius: 30px;
        display: inline-block;
        margin-bottom: 12px;
    }
    .card-title {
        color: #1E293B;
        font-size: 24px;
        font-weight: 800;
        margin-bottom: 6px;
    }
    .source-box {
        background-color: #FEF3C7;
        color: #78350F;
        padding: 8px 14px;
        border-radius: 10px;
        font-size: 13px;
        font-weight: 600;
        margin-bottom: 16px;
        display: inline-block;
    }
    .story-text {
        color: #334155;
        font-size: 18px;
        line-height: 1.7;
        background-color: #F8FAFC;
        padding: 18px;
        border-radius: 14px;
        border-left: 5px solid #0EA5E9;
        margin-bottom: 18px;
    }
    .activity-header {
        color: #15803D;
        font-size: 18px;
        font-weight: bold;
        margin-top: 10px;
        margin-bottom: 8px;
    }
    .activity-box {
        background-color: #DCFCE7;
        color: #14532D;
        padding: 16px;
        border-radius: 14px;
        border: 1px dashed #16A34A;
        font-size: 16px;
        line-height: 1.6;
    }
    .pedagogy-info {
        background-color: #F1F5F9;
        color: #475569;
        padding: 10px 14px;
        border-radius: 10px;
        font-size: 14px;
        margin-top: 12px;
    }
    .legal-card {
        background-color: #FFFBEB;
        border: 1px solid #FCD34D;
        border-radius: 12px;
        padding: 15px;
        font-size: 12px;
        color: #78350F;
        margin-top: 15px;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Session State Hazırlığı
if "completed_activities" not in st.session_state:
    st.session_state.completed_activities = set()

if "stars" not in st.session_state:
    st.session_state.stars = 0


# ==========================================
# 2. SAHİH KAYNAKLI VE ZENGİNLEŞTİRİLMİŞ VERİ SETİ
# ==========================================
@st.cache_data
def get_activity_data():
    data = [
        # --- ALLAH'IN VARLIĞI, BİRLİĞİ VE NİMETLERİ ---
        {
            "id": 1,
            "Kategori": "Allah'ın Varlığı ve Birliği",
            "Başlık": "Boyama Kitabı ve Sevimli Ressam",
            "Kaynak": "Mülk Suresi 3-4. Ayetler",
            "Hikaye": (
                "Önündeki boyama kitabında harika bir kelebek resmi gördüğünde"
                " ne dersin? 'Bu resmi biri çok güzel çizmiş!' dersin, değil"
                " mi? Kendi kendine boyalar oraya dökülüp resmi yapamaz. İşte"
                " gökyüzündeki yıldızlar, canlı renkli kelebekler ve yemyeşil"
                " ağaçlar da o kadar mükemmel ki! Onları bizim için tasarlayan"
                " ve yaratan Yüce Allah'tır."
            ),
            "Pedagoji": "Eser-Müessir (Sanatçı-Eser) ilişkisini somutlaştırır.",
            "Etkinlik_Turu": "🎨 Çizim & Drama Etkinliği",
            "Etkinlik_Detay": (
                "1. Çocuğa boş bir kağıt ve boya kalemleri verin.\n2. 'Şimdi"
                " gözlerimizi kapatıp bekleyelim, kağıt kendi kendine"
                " boyanacak mı?' diye sorun.\n3. Boyanmadığını görünce: 'İşte"
                " bak, küçücük resim bile ustasız olmuyorsa, koca evren de"
                " Allah olmadan olamaz' diyerek sohbet edin."
            ),
            "Sorular": [
                "Boş kağıt kendi kendine boyandı mı?",
                "Dünyayı ve renkleri bizim için kim yarattı?",
            ],
        },
        {
            "id": 2,
            "Kategori": "Allah'ın Varlığı ve Birliği",
            "Başlık": "Kuru Çekirdeğin Tatlı Sürprizi",
            "Kaynak": "En'âm Suresi 95. Ayet",
            "Hikaye": (
                "Küçücük, kuru ve sert bir elma çekirdeğini toprağa koyarız."
                " İçinde ne kırmızı renk vardır ne de şeker! Ama toprakta"
                " ıslanınca o çekirdek açılır ve büyür, bize tatlı tatlı"
                " elmalar verir. Kuru bir tahta parçasına elma yapmayı öğreten"
                " ve bize ikram eden Allah'tır."
            ),
            "Pedagoji": (
                "Nimet bilinci ve topraktaki mucizeleri fark ettirir."
            ),
            "Etkinlik_Turu": "🌱 Ev İçi Tarım Etkinliği",
            "Etkinlik_Detay": (
                "1. Şeffaf bir kaba pamuk yerleştirin ve arasına birkaç fasulye"
                " koyun.\n2. Her gün birlikte su verip 'Bismillah' deyin.\n3."
                " Fasulyenin filizlenişini gün gün gözlemleyip fotoğrafını"
                " çekin."
            ),
            "Sorular": [
                "Kuru fasulyeye filizlenmeyi kim öğretti?",
                "Bitkiler büyürken onlara ne söyleriz?",
            ],
        },
        {
            "id": 3,
            "Kategori": "Allah'ın Varlığı ve Birliği",
            "Başlık": "Rüzgarın Görünmeyen Eli",
            "Kaynak": "Şûrâ Suresi 33. Ayet",
            "Hikaye": (
                "Rüzgarı gözümüzle göremeyiz değil mi? Ama yüzümüze değdiğinde"
                " serinliğini hissederiz, ağacın yapraklarını salladığını"
                " görürüz. İşte Allah'ı da gözümüzle göremeyiz ama yarattığı"
                " güzel çiçeklerden, sıcak güneşten ve sevimli hayvanlardan"
                " O'nun varlığını ve sevgisini hissederiz."
            ),
            "Pedagoji": (
                "Görünmeyen ama hissedilen güçleri Anlama (Soyuttan Somuta)."
            ),
            "Etkinlik_Turu": "🌬️ Rüzgar Gülü Oyunu",
            "Etkinlik_Detay": (
                "1. Birlikte kağıttan basit bir rüzgar gülü yapın.\n2. Önce"
                " kendiniz üfleyin, sonra rüzgara tutun.\n3. 'Rüzgarı"
                " görmüyoruz ama nasıl döndürüyor değil mi? Allah'ı da"
                " görmüyoruz ama her yerde eserlerini görürüz' deyin."
            ),
            "Sorular": [
                "Rüzgarı gözünle görebiliyor musun?",
                "Rüzgarın estiğini nereden anlıyorsun?",
            ],
        },
        {
            "id": 4,
            "Kategori": "Allah'ın Varlığı ve Birliği",
            "Başlık": "Gece ve Gündüzün Düzeni",
            "Kaynak": "Yâsîn Suresi 40. Ayet",
            "Hikaye": (
                "Güneş hiç 'Bugün çok yoruldum, doğmayacağım' der mi? Ya da Ay"
                " gündüz saatinde çıkıp Güneş'in yolunu tıkar mı? Hayır!"
                " İkisi de saat gibi düzenli çalışır. Güneş bize gündüzü,"
                " Ay ise dinlenmemiz için geceyi getirir. Bu harika düzeni"
                " Allah kurmuştur."
            ),
            "Pedagoji": "Zaman bilinci ve kütlesel düzen tefekkürü.",
            "Etkinlik_Turu": "☀️ Gece-Gündüz Fener Tiyatrosu",
            "Etkinlik_Detay": (
                "1. Odayı biraz karartın. Bir el feneri (Güneş) ve bir top"
                " (Dünya) alın.\n2. Feneri tutup topu döndürün. Işık alan yerin"
                " gündüz, karanlık yerin gece olduğunu gösterin.\n3. Allah'ın"
                " koyduğu düzen üzerine konuşun."
            ),
            "Sorular": [
                "Güneş ve Ay neden birbiriyle çarpışmaz?",
                "Gece olunca ne yaparız?",
            ],
        },
        {
            "id": 5,
            "Kategori": "Allah'ın Varlığı ve Birliği",
            "Başlık": "Vücudumuzun Süper Makinesi: Kalbimiz",
            "Kaynak": "Kâf Suresi 16. Ayet",
            "Hikaye": (
                "Elimizi göğsümüze koyalım: 'Tık-tık, tık-tık...' Duyuyor musun?"
                " Kalbimiz biz uyurken, oyun oynarken ve yemek yerken hiç"
                " durmadan çalışır. Biz ona 'çalış' demeyiz ama o bizim için"
                " kan pompalar. Bizi bizden iyi bilen ve koruyan Allah'tır."
            ),
            "Pedagoji": "Öz farkındalık ve beden mucizelerini hissetme.",
            "Etkinlik_Turu": "💓 Nabız Dinleme Deneyi",
            "Etkinlik_Detay": (
                "1. Çocuğun elini göğsüne koydurup sakin kalbini dinletin.\n2."
                " Sonra 10 saniye yerinde zıplamasını isteyin.\n3. Tekrar elini"
                " koydurun: 'Bak nasıl hızlı atıyor! Allah kalbimizi öyle güzel"
                " yaratmış ki ihtiyacımıza göre çalışıyor' deyin."
            ),
            "Sorular": [
                "Uyurken kalbimize 'çalış' dememiz gerekiyor mu?",
                "Bizi uyurken bile koruyan kimdir?",
            ],
        },
        # --- PEYGAMBER EFENDİMİZİN HAYATI VE AHLAKI ---
        {
            "id": 6,
            "Kategori": "Peygamber Efendimizin Hayatı",
            "Başlık": "Kuşu Ölen Küçük Zeyd'e Ziyaret",
            "Kaynak": "Sahihi Buhârî (Edeb 112); Sahihi Müslim (Âdâb 30)",
            "Hikaye": (
                "Peygamberimizin küçük bir arkadaşı vardı, adı Zeyd'di. Zeyd'in"
                " çok sevdiği minik kuşu öldüğünde Zeyd çok üzüldü."
                " Peygamberimiz bunu duyunca hemen Zeyd'in evine gitti, ona"
                " sarıldı, teselli etti ve üzüntüsünü paylaştı. O, çocukların"
                " duygularına çok değer verirdi."
            ),
            "Pedagoji": "Empati kurma, duygu paylaşımı ve nezaket kazandırır.",
            "Etkinlik_Turu": "🧸 Empati ve Teselli Draması",
            "Etkinlik_Detay": (
                "1. Bir oyuncak bebeği üzgünmüş gibi yapın.\n2. Çocuğunuza:"
                " 'Zeyd gibi bebeğimizin de kuşu üzülmüş, ona Peygamberimiz gibi"
                " nasıl sarılıp teselli edelim?' deyin.\n3. Çocuğun sarılmasını"
                " ve tatlı sözler söylemesini sağlayın."
            ),
            "Sorular": [
                "Peygamberimiz üzgün olan Zeyd'e ne yaptı?",
                "Biz üzgün bir arkadaşımızı görünce ne yapmalıyız?",
            ],
        },
        {
            "id": 7,
            "Kategori": "Peygamber Efendimizin Hayatı",
            "Başlık": "Sırtında Taşınan Küçük Torunlar",
            "Kaynak": "Neseî (İftitah 82); Ahmed b. Hanbel (Müsned)",
            "Hikaye": (
                "Peygamberimiz namaz kılarken küçük torunları Hz. Hasan ve Hz."
                " Hüseyin geldiler. Sevecen dedelerinin sırtına tırmandılar!"
                " Peygamberimiz onlar düşüp incinmesin diye secdesini uzattı,"
                " onları sırtından atmadı. Namaz bitince de onları kucağına"
                " alıp öptü."
            ),
            "Pedagoji": "İbadet sevgisi ve çocuk-yetişkin güven bağı.",
            "Etkinlik_Turu": "🐎 Sırtımda Taşıyorum Oyunu",
            "Etkinlik_Detay": (
                "1. Anne/Baba çocukla evde oyun oynarken onu sırtına alsın.\n2."
                " Peygamberimizin torunlarını ne kadar çok sevdiği ve onlara"
                " ne kadar nazik davrandığı üzerine sohbet edin."
            ),
            "Sorular": [
                "Torunları Peygamberimizin sırtına çıkınca O ne yaptı?",
                "Peygamberimiz çocukları sever miydi?",
            ],
        },
        {
            "id": 8,
            "Kategori": "Peygamber Efendimizin Hayatı",
            "Başlık": "Ağlayan Devenin Başını Okşamak",
            "Kaynak": "Sünen-i Ebu Davud (Cihad 44)",
            "Hikaye": (
                "Bir gün Peygamberimiz bir bahçeye girdi. Orada üstüne çok"
                " fazla yük yüklenmiş yorgun bir deve gördü. Deve ağlıyordu."
                " Peygamberimiz hemen devenin yanına gitti, sevgiyle başını ve"
                " kulaklarını okşadı. Sonra devenin sahibine 'Bu canlıya iyi"
                " bakmalı, onu fazla yormamalısın' dedi."
            ),
            "Pedagoji": "Hayvan sevgisi ve merhamet duygusunu pekiştirir.",
            "Etkinlik_Turu": "🐱 Sokak Canlılarına Kap Koyma",
            "Etkinlik_Detay": (
                "1. Bir plastik kaba su ve biraz mama/ekmek koyun.\n2. Birlikte"
                " kapının önüne veya parka götürüp koyun.\n3. 'Peygamberimiz"
                " gibi biz de hayvanları koruyalım' deyin."
            ),
            "Sorular": [
                "Deve neden ağlıyordu?",
                "Peygamberimiz deveye nasıl yardım etti?",
            ],
        },
        {
            "id": 9,
            "Kategori": "Peygamber Efendimizin Hayatı",
            "Başlık": "Tatlı Dilli ve Güler Yüzlü Peygamber",
            "Kaynak": "Sünen-i Tirmizî (Menâkıb 46)",
            "Hikaye": (
                "Peygamber Efendimiz insanlarla konuşurken her zaman gülümserdi."
                " Arkadaşı Hz. Enes diyor ki: 'Peygamberimizden daha çok"
                " gülümseyen hiç kimseyi görmedim.' Tebessüm etmek başkalarının"
                " kalbini ısıtan en güzel hediyedir."
            ),
            "Pedagoji": "Sosyal iletişim, tebessüm ve sadaka bilinci.",
            "Etkinlik_Turu": "😊 'Ayna Ol' Aile Oyunu",
            "Etkinlik_Detay": (
                "1. Karşılıklı geçip sırayla komik ve tatlı yüz ifadeleri"
                " yapın.\n2. Sonra en içten tebessümünüzü yapıp: 'Gülümsemek"
                " Peygamberimizin sünnetidir ve sadakadır' deyin."
            ),
            "Sorular": [
                "Peygamberimiz insanlara bakınca ne yapardı?",
                "Gülümseyince etrafımızdakiler nasıl hisseder?",
            ],
        },
        {
            "id": 10,
            "Kategori": "Peygamber Efendimizin Hayatı",
            "Başlık": "Enes'in 10 Yıllık Sırrı ve Nezaket",
            "Kaynak": "Sahihi Buhârî (Edeb 39); Sahihi Müslim (Fezâil 51)",
            "Hikaye": (
                "Küçük Enes, Peygamberimizin yanında tam 10 yıl büyüdü."
                " Peygamberimiz ona bir kez bile 'Of!' demedi, hiç kızmadı,"
                " bir hatası olduğunda bile tatlılıkla öğretti. O, çocuklara"
                " karşı dünyanın en sabırlı öğretmeniydi."
            ),
            "Pedagoji": "Öfke kontrolü, nezaket ve tatlı dilli olma.",
            "Etkinlik_Turu": "🌸 'Tatlı Dil Kavanozu'",
            "Etkinlik_Detay": (
                "1. Bir kavanoz süsleyin.\n2. Gün içinde kullanılan 'Teşekkür"
                " ederim', 'Rica ederim', 'Özür dilerim' gibi güzel sözler için"
                " kavanoza birer renkli boncuk atın."
            ),
            "Sorular": [
                "Peygamberimiz Enes'e hiç kızdı mı?",
                "Hata yapınca birbirimize nasıl davranmalıyız?",
            ],
        },
        # --- İSLAM DEĞERLERİ, İBADETLER VE GÜZEL AHLAK ---
        {
            "id": 11,
            "Kategori": "İslam Değerleri ve İbadetler",
            "Başlık": "Yoldaki Engeli Kenara Koymak",
            "Kaynak": "Sahihi Müslim (İman 84)",
            "Hikaye": (
                "Peygamberimiz, yolda insanların ayağına takılabilecek bir"
                " taşı, sivri bir dalı veya çöpü kenara çekmenin çok güzel"
                " bir ibadet olduğunu söylemiştir. Çevremizi temiz ve güvenli"
                " tutmak İslam'ın en tatlı kuralıdır."
            ),
            "Pedagoji": "Sorumluluk alma ve çevre bilinci geliştirir.",
            "Etkinlik_Turu": "🧹 'Temiz Yol' Avcılığı Oyunu",
            "Etkinlik_Detay": (
                "1. Evin koridoruna birkaç plastik oyuncak ve kutu dağıtın.\n2."
                " Çocuğa: 'Şimdi yoldaki engelleri temizleme görevimiz var!'"
                " deyin.\n3. Engelleri sepete topladıktan sonra tebrik edip"
                " sadaka sevabı kazandığını anlatın."
            ),
            "Sorular": [
                "Yoldaki taşı kenara koymak neden güzeldir?",
                "Çevremizi temiz tutunca kim mutlu olur?",
            ],
        },
        {
            "id": 12,
            "Kategori": "İslam Değerleri ve İbadetler",
            "Başlık": "Sihirli Anahtar: Bismillah",
            "Kaynak": "Sünen-i Ebu Davud (Edeb 18)",
            "Hikaye": (
                "Yemeğe başlarken, kapıyı açarken veya oyun oynamaya başlarken"
                " 'Bismillahirrahmanirrahim' demek, Allah'tan yardım"
                " istemektir. Bu söz, her güzel işin kapısını açan tatlı ve"
                " sihirli bir anahtar gibidir."
            ),
            "Pedagoji": "Günlük yaşamda Allah'ı hatırda tutma alışkanlığı.",
            "Etkinlik_Turu": "🔑 Kağıttan Sihirli Anahtar Yapımı",
            "Etkinlik_Detay": (
                "1. Kartondan büyük bir anahtar şekli kesin.\n2. Üzerine renkli"
                " boyalarla 'BİSMİLLAH' yazıp süsleyin.\n3. Odanın kapısına"
                " asın ve her giriş çıkışta anahtara dokunup Besmele çekin."
            ),
            "Sorular": [
                "İşe başlarken hangi sihirli sözü söyleriz?",
                "Bismillah deyince ne olur?",
            ],
        },
        {
            "id": 13,
            "Kategori": "İslam Değerleri ve İbadetler",
            "Başlık": "Su Damlasını İsraf Etmemek",
            "Kaynak": "Sünen-i İbn Mâce (Tahâret 45)",
            "Hikaye": (
                "Peygamberimiz bir gün nehir kenarında abdest alan arkadaşına:"
                " 'Suyu israf etme' buyurdu. Arkadaşı 'Nehirde bile mi?' diye"
                " sorunca, 'Evet, akıp giden bir nehirde olsan bile suyu"
                " gereksiz harcama' dedi. Su bize Allah'ın emanetidir."
            ),
            "Pedagoji": "Tasarruf, çevre koruma ve nimet kıymeti bilme.",
            "Etkinlik_Turu": "💧 'Suyu Koruyan Kahraman' Etkinliği",
            "Etkinlik_Detay": (
                "1. Musluktan damlayan suyu toplamak için altına küçük bir kap"
                " koyun.\n2. Diş fırçalarken musluğu kapatma kuralı koyun.\n3."
                " Kabın dolduğunu görünce onunla bir çiçeği sulayın."
            ),
            "Sorular": [
                "Peygamberimiz nehir kenarında bile ne yapmamızı istemedi?",
                "Diş fırçalarken musluğu ne yapmalıyız?",
            ],
        },
        {
            "id": 14,
            "Kategori": "İslam Değerleri ve İbadetler",
            "Başlık": "Paylaşmanın Bereketi ve Sadaka",
            "Kaynak": "Sahihi Müslim (Zekât 68)",
            "Hikaye": (
                "Elinde iki tane lezzetli elma olduğunu düşün. Birini çok"
                " acıkmış arkadaşına verdiğinde ne olur? Elman azalmış gibi"
                " görünür ama kalbindeki mutluluk kocaman olur! Peygamberimiz"
                " 'Paylaşmak malı eksiltmez, aksine bereketlendirir' demiştir."
            ),
            "Pedagoji": "Cömertlik, bencil olmama ve cemaat bilinci.",
            "Etkinlik_Turu": "🎁 'Paylaşım Kutusu' Hazırlama",
            "Etkinlik_Detay": (
                "1. Küçük bir kutuyu renkli kağıtlarla kaplayın.\n2. İçine"
                " kullanmadığı bir oyuncağı veya fazla bir krakeri koyun.\n3."
                " Bir arkadaşına veya ihtiyaç sahibine hediye etmesini"
                " sağlayın."
            ),
            "Sorular": [
                "Arkadaşınla bir şey paylaştığında nasıl hissedersin?",
                "Paylaşmak malımızı azaltır mı?",
            ],
        },
        {
            "id": 15,
            "Kategori": "İslam Değerleri ve İbadetler",
            "Başlık": "Teşekkür Etmek: Elhamdülillah",
            "Kaynak": "Sünen-i Tirmizî (Zühd 56)",
            "Hikaye": (
                "Biri sana güzel bir hediye verince 'Teşekkür ederim' dersin,"
                " değil mi? Bize lezzetli meyveleri, gözlerimizi, kulaklarımızı"
                " ve ailemizi veren Allah'a teşekkür etmek için ise"
                " 'Elhamdülillah' (Allah'a hamdolsun) deriz."
            ),
            "Pedagoji": "Şükür duygusu ve farkındalık geliştirme.",
            "Etkinlik_Turu": "🌳 'Şükür Ağacı' Yapımı",
            "Etkinlik_Detay": (
                "1. Kağıda bir ağaç gövdesi çizin.\n2. Yaprak şeklinde kesilmiş"
                " kağıtlara çocuğun sevdiği şeyleri (gözüm, elmam, annem)"
                " çizin/yazın.\n3. Yaprakları yapıştırıp 'Elhamdülillah' deyin."
            ),
            "Sorular": [
                "Allah'a teşekkür etmek için ne deriz?",
                "Bugün sahip olduğun hangi şey için Elhamdülillah demek istersin?",
            ],
        },
        {
            "id": 16,
            "Kategori": "İslam Değerleri ve İbadetler",
            "Başlık": "Temizlik İmanın Yarısıdır",
            "Kaynak": "Sahihi Müslim (Tahâret 1)",
            "Hikaye": (
                "Çiçekler temiz toprakta, kuşlar temiz yuvalarda yaşar."
                " Müslümanlar da ellerini, elbiselerini ve odalarını hep temiz"
                " tutarlar. Peygamberimiz 'Temizlik imanın yarısıdır' buyurarak"
                " temizliğe çok önem vermiştir."
            ),
            "Pedagoji": "Öz bakım yetenekleri, hijyen ve düzen alışkanlığı.",
            "Etkinlik_Turu": "🧼 'Köpük Oyunu' ile Doğru El Yıkama",
            "Etkinlik_Detay": (
                "1. Birlikte banyoya gidin.\n2. 20 saniye boyunca parmak"
                " aralarını ve bilekleri sabun köpükleriyle yıkayın.\n3."
                " Yıkarken 'Subhanallah, Elhamdülillah' tekerlemesini söyleyin."
            ),
            "Sorular": [
                "Peygamberimiz temizlik hakkında ne söylemiştir?",
                "Yemekten önce ne yapmalıyız?",
            ],
        },
        {
            "id": 17,
            "Kategori": "İslam Değerleri ve İbadetler",
            "Başlık": "Doğruluk En Güzel Süstür",
            "Kaynak": "Sahihi Buhârî (Edeb 69)",
            "Hikaye": (
                "Yalan söylemek, parlak bir camın üzerine çamur atmak gibidir;"
                " etrafı karartır. Doğru söylemek ise kalbimizi ışıl ışıl"
                " parlatır. Peygamberimiz hiç yalan söylemediği için herkes ona"
                " 'Muhammedü'l-Emîn' (Güvenilir Muhammed) derdi."
            ),
            "Pedagoji": "Dürüstlük, karakter gelişimi ve güvenilirlik.",
            "Etkinlik_Turu": "💎 'Işıl Işıl Doğruluk' Deneyi",
            "Etkinlik_Detay": (
                "1. Bir fener ışığını temiz bir cama tutun (doğruluk"
                " parlar).\n2. Camın önüne siyah bir kağıt koyun (yalan kapatır"
                " ve karartır).\n3. 'Doğru sözlü olunca kalbimiz hep parlar'"
                " diye açıklayın."
            ),
            "Sorular": [
                "Peygamberimize neden 'Güvenilir' derlerdi?",
                "Bir hata yaptığımızda ne söylemeliyiz?",
            ],
        },
        {
            "id": 18,
            "Kategori": "İslam Değerleri ve İbadetler",
            "Başlık": "Kuşların Duası: Zikir",
            "Kaynak": "İsrâ Suresi 44. Ayet",
            "Hikaye": (
                "Sabahları penceremize konan serçelerin 'Çip çip' diye ötüşünü"
                " duydun mu? Aslında onlar kendi dilleriyle Allah'ı anıyor ve"
                " O'na teşekkür ediyorlar. Biz de 'Subhanallah' diyerek evrendeki"
                " tüm canlıların korosuna katılırız."
            ),
            "Pedagoji": "Doğadaki zikir farkındalığı ve dil terbiyesi.",
            "Etkinlik_Turu": "📿 Makarnadan Tespih Yapımı",
            "Etkinlik_Detay": (
                "1. Delikli makarnaları sulu boya ile renklendirin.\n2. İpe"
                " dizerken her makarnada 'Subhanallah', 'Elhamdülillah',"
                " 'Allahu Ekber' deyin.\n3. İpi bağlayıp çocuğa kendi"
                " tespihini hediye edin."
            ),
            "Sorular": [
                "Kuşlar ötüşürken aslında ne yapıyorlar?",
                "Subhanallah deyince ne yapmış oluruz?",
            ],
        },
        {
            "id": 19,
            "Kategori": "İslam Değerleri ve İbadetler",
            "Başlık": "Büyüklere Saygı, Küçüklere Şefkat",
            "Kaynak": "Sünen-i Tirmizî (Birr 15)",
            "Hikaye": (
                "Dedelerimiz ve ninelerimiz bize ne güzel hikayeler anlatır!"
                " Peygamberimiz: 'Küçüklerimize merhamet etmeyen, büyüklere"
                " saygı göstermeyen bizden değildir' demiştir. Onların elini"
                " öpmek ve yardım etmek kalbimizi güzelleştirir."
            ),
            "Pedagoji": "Aile bağları, hürmet ve nesiller arası sevgi.",
            "Etkinlik_Turu": "📞 Dede ve Nineye Sevgi Araması",
            "Etkinlik_Detay": (
                "1. Birlikte aile büyüğünü (dede/nine) arayın.\n2. Çocuğun"
                " 'Seni çok seviyorum, nasılsın?' demesini sağlayın.\n3. Yanlarındaysa"
                " ellerini öpüp başa koyma geleneğini uygulayın."
            ),
            "Sorular": [
                "Büyüklere nasıl davranmalıyız?",
                "Küçük kardeşlerimize veya arkadaşlarımıza ne göstermeliyiz?",
            ],
        },
        {
            "id": 20,
            "Kategori": "İslam Değerleri ve İbadetler",
            "Başlık": "Kabe ve Kıble Yönümüz",
            "Kaynak": "Bakara Suresi 144. Ayet",
            "Hikaye": (
                "Dünyanın neresinde olursak olalım, namaz kılarken hepimiz aynı"
                " yöne döneriz: Mekke'deki mübarek Kâbe'ye! Bu durum, bütün"
                " Müslümanların kardeş olduğunu ve tek bir Allah'a ibadet"
                " ettiğini gösterir."
            ),
            "Pedagoji": "Birlik bilinci, mekan oryantasyonu ve aidiyet.",
            "Etkinlik_Turu": "🧭 Pusula ve Maket Kâbe Yapımı",
            "Etkinlik_Detay": (
                "1. Küçük bir kare kutuyu siyah kartonla kaplayın, üzerine sarı"
                " şerit yapıştırın.\n2. Telefon pusulasıyla Kıble yönünü"
                " bulun.\n3. Maket Kâbe'yi o yöne koyup seccadeyi yöneltin."
            ),
            "Sorular": [
                "Namaz kılarken yönümüzü nereye döneriz?",
                "Kâbe bize neyi hatırlatır?",
            ],
        },
    ]
    return pd.DataFrame(data)


df = get_activity_data()

# ==========================================
# 3. YAN MENÜ & ETKİLEŞİM PANELİ
# ==========================================
st.sidebar.image(
    "https://cdn-icons-png.flaticon.com/512/3068/3068327.png", width=80
)
st.sidebar.title("⭐ Minik Âlim Paneli")

# Yıldız Skoru Gösterimi
st.sidebar.markdown(f"### 🌟 Toplam Yıldızın: *{st.session_state.stars}*")
st.sidebar.progress(min(st.session_state.stars / 200, 1.0))

st.sidebar.markdown("---")
cat_choice = st.sidebar.selectbox(
    "🎯 Kategori Seçin:", ["Tüm Konular"] + list(df["Kategori"].unique())
)
search_word = st.sidebar.text_input(
    "🔍 Kelime Ara (Örn: Deve, Su, Kâbe, Kuş):", ""
)

st.sidebar.markdown("---")
st.sidebar.subheader("🎲 Rastgele Etkinlik Kartı")
if st.sidebar.button("Bana Bir Etkinlik Ver!"):
    rand_card = df.sample(1).iloc[0]
    st.sidebar.info(
        f"*{rand_card['Başlık']}*\n\n_{rand_card['Etkinlik_Turu']}_"
    )

# Yasal / Hukuki Kısaltılmış Bildirim Kutusu (Sidebar)
st.sidebar.markdown(
    """
    <div class="legal-card">
        <b>⚖️ YASAL BİLDİRİM & KULLANIM ŞARTLARI:</b><br>
        Bu platform, erken çocukluk çağındaki (5-6 yaş) çocukların manevi ve ahlaki gelişimini desteklemek amacıyla hazırlanmış ücretsiz bir bilgi paylaşımı aracıdır. Ticari amaçla kopyalanamaz veya satılamaz.
    </div>
    """,
    unsafe_allow_html=True,
)

# ==========================================
# 4. ANA SAYFA VE ETKİNLİK AKIŞI
# ==========================================
st.title("🎨 Etkinlikli & Sahih Kaynaklı İslam Portalı")
st.caption(
    "5-6 Yaş Erken Çocukluk Dönemi İçin İnteraktif, Eğitici ve Uygulamalı Öğretim"
    " Modülü"
)

# Filtreleme
filtered_df = df.copy()
if cat_choice != "Tüm Konular":
    filtered_df = filtered_df[filtered_df["Kategori"] == cat_choice]

if search_word:
    filtered_df = filtered_df[
        filtered_df["Hikaye"].str.contains(search_word, case=False)
        | filtered_df["Başlık"].str.contains(search_word, case=False)
    ]

# Metrikler
m1, m2, m3 = st.columns(3)
m1.metric("Hazır Etkinlik Sayısı", len(df))
m2.metric("Tamamlanan Etkinlik", len(st.session_state.completed_activities))
m3.metric("Kazanılan Yıldız", st.session_state.stars)

st.markdown("---")

# ==========================================
# 5. KARTLARIN VE ETKİNLİKLERİN SUNUMU
# ==========================================
for idx, row in filtered_df.iterrows():
    card_id = row["id"]
    is_completed = card_id in st.session_state.completed_activities

    st.markdown(
        f"""
    <div class="card-container">
        <span class="category-badge">{row['Kategori']}</span>
        <div class="card-title">{row['Başlık']}</div>
        <div class="source-box">📖 <b>Sahih Kaynak:</b> {row['Kaynak']}</div>
        <div class="story-text"><b>🎈 Çocuk Diliyle Narasyon:</b><br>{row['Hikaye']}</div>
        <div class="activity-header">{row['Etkinlik_Turu']}</div>
        <div class="activity-box">{row['Etkinlik_Detay'].replace('\n', '<br>')}</div>
        <div class="pedagogy-info">🧠 <b>Pedagojik Kazanım:</b> {row['Pedagoji']}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # İnteraktif Çocuk Soruları ve Etkinlik Tamamlama Butonu
    col_q, col_btn = st.columns([3, 1])

    with col_q:
        st.write(
            "<b>💬 Çocukla Sohbet Sorusu:</b> " + row["Sorular"][0],
            unsafe_allow_html=True,
        )

    with col_btn:
        if not is_completed:
            if st.button(
                "✅ Etkinliği Yaptık (+10 Yıldız)", key=f"btn_{card_id}"
            ):
                st.session_state.completed_activities.add(card_id)
                st.session_state.stars += 10
                st.balloons()
                st.rerun()
        else:
            st.success("🌟 Etkinlik Tamamlandı!")

    st.markdown("<br>", unsafe_allow_html=True)

# ==========================================
# 6. EBEVEYN KILAVUZU & DETAYLI HUKUKİ BİLDİRİM
# ==========================================
with st.expander("📘 Ebeveyn Kılavuzu, Manevi Gelişim Yöntemi ve Hukuki Metin"):
    st.markdown("""
    ### 🌸 1. Çocukların Manevi ve Ahlaki Gelişim Metodu (5-6 Yaş)
    Erken çocukluk dönemi, çocuğun Yaratıcı kavramı ve ahlak değerleri ile ilk kez tanıştığı altın çağdır.
    * **Soyuttan Somuta Geçiş:** Bu dönemde soyut dini kavramları doğrudan anlatmak yerine somut nesnelerle (su, fener, fasulye, taş, boncuk) somutlaştırarak öğretmek esastır.
    * **Sevgi Odaklı Dil:** Korkutucu veya zorlayıcı anlatımlardan kaçınılarak; merhamet, cömertlik, doğruluk ve sevgi temaları öne çıkarılmıştır.
    * **Oyunlaştırma:** İbadetler ve güzel ahlak ilkelere birer "ödev" değil, eğlenceli ve etkileşimli birer "arkadaşlık/oyun macerası" olarak kurgulanmıştır.

    ---

    ### ⚖️ 2. Hukuki Metin, Bilgi Paylaşımı ve Sorumluluk Sınırları
    * **Amacı ve Niteliği:** Bu platform, **yalnızca bilgilendirme, manevi eğitim ve kâr amacı gütmeyen bilgi paylaşımı** maksadıyla geliştirilmiştir.
    * **Ticari Kullanım Yasağı:** Yazılımın kaynak kodları, veri tabanı ve tasarımı kısmen veya tamamen satılamaz, ücretli bir hizmete dahil edilemez ya da ticari bir ürüne dönüştürülemez.
    * **Kaynak Doğruluğu:** Portaldaki tüm ayet ve hadis aktarımları Diyanet İşleri Başkanlığı ve Kütüb-i Sitte külliyatı esas alınarak sadelikle hazırlanmıştır. 
    * **Sorumluluk Sınırı:** Etkinliklerin uygulanması esnasında (makas, su, küçük objeler kullanımı vb.) ebeveyn veya eğitici gözetimi zorunludur. Uygulamadaki etkinliklerin fiziki uygulanışı esnasında oluşabilecek durumlardan ebeveyn/uygulayıcı sorumludur.
    """)