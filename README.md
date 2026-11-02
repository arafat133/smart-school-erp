# 🏫 نظام المدارس السحابي الآمن الشامل | Smart School Cloud ERP v2.0

نظام إدارة مدرسي سحابي متكامل ومتقدم (ERP) يدعم تعدد المدارس (Multi-Tenant)، مدعوم بإطار عمل **FastAPI** فائق السرعة، ومصمم بأسلوب معماري عصري آمن يشمل جدار حماية سيبراني متعدد الطبقات، وتوثيق الشهادات بالبلوكشين، ولوحات تحكم تفاعلية للمدارس، وأولياء الأمور، وإدارة النظام المركزية (SaaS).

---

## 🚀 روابط ومسارات النظام الرئيسية (System Portals)

| البوابة / الخدمة | المسار المحلي | الوصف |
| :--- | :--- | :--- |
| **بوابة المدارس والمعلمين** | `/school` أو `/school.html` | لوحة إدارة المدرسة الشاملة (الطلاب، الحصص، الجداول، الدرجات، الرسوم) |
| **بوابة الإدارة المركزية (SaaS)** | `/admin` أو `/saas` | لوحة تحكم السوبر آدمن لإدارة المدارس والاشتراكات والمراقبة |
| **بوابة أولياء الأمور والطلاب** | `/parent` أو `/parent.html` | بوابة متابعة الأبناء، الدرجات، الحافلات المدرسية، والإشعارات |
| **العرض الترويجي (Motion Graphics)** | `/motion` | صفحة موشن جرافيك ومؤثرات صوتية تفاعلية للترويج للنظام |
| **التحقق من الشهادات (Blockchain)** | `/verify` | التحقق الفوري المشفر من صحة الوثائق والشهادات المدرسية |
| **فحص جاهزية الخادم (Health Check)** | `/health` | فحص حالة الخادم وتكامله مع منصات الاستضافة السحابية |
| **توثيق الواجهات البرمجية (Swagger API)** | `/docs` | واجهة فحص واختبار جميع مسارات RESTful API التفاعلية |

---

## ☁️ دليل الاستضافة السحابية الشامل (Cloud Deployment Guide)

النظام مهيأ ومعد بالكامل للعمل فورياً عبر المنصات الثلاث: **GitHub**، **Render**، و **Vercel**.

```
                           ┌────────────────────────┐
                           │    GitHub Repository   │
                           │   (الكود المصدري وإدارة الإصدارات)│
                           └───────────┬────────────┘
                                       │
                    ┌──────────────────┴──────────────────┐
                    ▼                                     ▼
        ┌───────────────────────┐             ┌───────────────────────┐
        │        Render         │             │        Vercel         │
        │   (خادم Backend & DB)  │             │ (واجهة Frontend السريعة)│
        │   FastAPI + Uvicorn   │             │ Global Edge CDN + UX  │
        │ https://*.onrender.com│             │ https://*.vercel.app  │
        └───────────────────────┘             └───────────────────────┘
```

---

### 1️⃣ الاستضافة على GitHub (مستودع الكود المركزي)

1. افتح موجه الأوامر في مجلد المشروع وقم بربط المستودع مع حسابك على GitHub:
   ```bash
   git remote add origin https://github.com/USERNAME/REPO_NAME.git
   git branch -M main
   git push -u origin main
   ```
2. بمجرد رفع الكود، يصبح المستودع جاهزاً للربط التلقائي بضغطة زر واحدة مع Render و Vercel.

---

### 2️⃣ الاستضافة على Render (خادم الباك إند والنظام الحي)

منصة **Render** هي الخيار الأمثل لتشغيل تطبيقات Python / FastAPI السحابية:

#### الطريقة الأولى: النشر الآلي بضغطة زر (Render Blueprint):
1. سجّل الدخول إلى [Render Dashboard](https://dashboard.render.com).
2. اضغط على **New +** ثم اختر **Blueprint**.
3. اختر مستودع الـ GitHub الخاص بك.
4. سيقرأ Render ملف `render.yaml` تلقائياً ويقوم ببناء النظام وتشغيله بالكامل مع المتغيرات البيئية وفحص الصحة `/health`.

#### الطريقة الثانية: النشر اليدوي كخدمة ويب (Web Service):
1. اضغط **New +** ثم **Web Service**.
2. اختر مستودع الـ GitHub.
3. اضبط الإعدادات التالية:
   - **Name**: `smartschool-cloud-erp`
   - **Environment**: `Python 3`
   - **Region**: Frankfurt (أو الأقرب لك)
   - **Branch**: `main`
   - **Build Command**: `pip install --upgrade pip && pip install -r requirements.txt`
   - **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - **Health Check Path**: `/health`
4. اضغط **Create Web Service**، وخلال دقيقتين ستحصل على رابط مباشر يعمل بنطاق HTTPS مجاني (مثال: `https://smartschool-cloud-erp.onrender.com`).

---

### 3️⃣ الاستضافة على Vercel (الواجهة الأمامية وشبكة الحافة العالمية)

منصة **Vercel** تمنح الواجهة الأمامية واللوحات سرعة فائقة مع شبكة توصيل محتوى (Edge CDN) عالمية:

1. سجّل الدخول إلى [Vercel Dashboard](https://vercel.com).
2. اضغط على **Add New...** ثم **Project**.
3. اربط حساب GitHub واختر مستودع النظام.
4. سيتعرف Vercel تلقائياً على ملف `vercel.json` الموجود في جذر المشروع.
5. اضغط **Deploy**.
6. ستحصل فوراً على رابط عالمي فائق السرعة ينتهي بـ `.vercel.app`.

---

## ⚙️ المتغيرات البيئية (Environment Variables)

يمكنك ضبط المتغيرات التالية في لوحة تحكم Render أو Vercel:

| المتغير | القيمة الافتراضية | الوصف |
| :--- | :--- | :--- |
| `PORT` | `8000` | المنفذ المخصص للخادم السحابي |
| `SECRET_KEY` | `secure_secret_key` | مفتاح تشفير وفك تشفير رموز JWT |
| `DATABASE_URL` | `sqlite+aiosqlite:///secure_school.db` | رابط قاعدة البيانات (SQLite محلياً أو PostgreSQL سحابياً) |
| `ALLOWED_ORIGINS` | `https://*.vercel.app,https://*.onrender.com` | النطاقات المصرح لها بتبادل البيانات عبر CORS |
| `ENABLE_SECURITY_ALERTS` | `false` | تفعيل الإشعارات السيبرانية الفورية (Telegram / WhatsApp) |

---

## 💻 التشغيل المحلي (Local Development)

```bash
# 1. إنشاء البيئة الافتراضية
python -m venv .venv
source .venv/bin/activate  # في Linux/Mac
.venv\Scripts\activate     # في Windows

# 2. تثبيت الحزم المطلوبة
pip install -r requirements.txt

# 3. تشغيل الخادم
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```
افتح المتصفح على: `http://127.0.0.1:8000`
