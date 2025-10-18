🔗 TinyURL – کوتاه‌کننده لینک با FastAPI

یه پروژه‌ی کوچیک ولی خیلی باحال 😎
یه کوتاه‌کننده لینک نوشتم با FastAPI، SQLModel و Jinja2 که هم تمرینیه، هم واقعاً می‌تونه کار کنه.

💡 چی کار می‌کنه؟

کارش ساده‌ست ولی خیلی کاربردی:

لینک‌های طولانی رو کوتاه می‌کنه

برای هر لینک یه کد یکتا می‌سازه (یا اگه بخوای، خودت یه کد خاص بده 😁)

هر کلیک روی لینک، یه کلیک‌کانت یا تعداد کلیک رو ثبت می‌کنه

همه‌ی دیتاها توی دیتابیس ذخیره می‌شن

یه داشبورد ساده و خوشگل و مینیمال هم داره برای دیدن لینک‌ها


⚙️ چطوری اجراش کنم؟
۱. ریپو رو بگیر 😎
git clone https://github.com/<mahkzmi>/tiny-url-shortener.git
cd url-shortener

۲. محیط مجازی بساز و پکیج‌ها رو نصب کن
python -m venv env
source env/bin/activate    # روی macOS/Linux
env\Scripts\activate       # روی ویندوز

pip install -r requirements.txt

۳. پروژه رو اجرا کن
uvicorn app.main:app --reload


حالا برو به:
👉 http://localhost:8000/dashboard

و یه لینک جدید بساز 😍

🧱 APIها
متد	مسیر	توضیح
POST	/shorten	ساخت لینک کوتاه جدید
GET	/{code}	ریدایرکت به لینک اصلی
GET	/stats/{code}	نمایش آمار کلیک لینک خاص
GET	/dashboard	داشبورد مدیریت لینک‌ها
🧰 تکنولوژی‌هایی که استفاده کردم

🐍 Python 3.11

⚡ FastAPI

🗃️ SQLModel (با SQLite)

🧩 Jinja2 Templates

💡 Uvicorn

💥 ویژگی‌ها

✅ لینک کوتاه می‌سازه (با کد تصادفی یا دلخواه)
✅ دیتاها رو ذخیره می‌کنه
✅ آمار بازدید هر لینک رو نگه می‌داره
✅ یه داشبورد ساده داره که خودت ببینی چی ساختی

🧪 یه نمونه درخواست API
درخواست:
POST /shorten
Content-Type: application/json

{
  "url": "https://example.com/very-long-link",
  "title": "مثال تستی"
}

پاسخ:
{
  "code": "aB3kD9",
  "short_url": "http://localhost:8000/aB3kD9",
  "target_url": "https://example.com/very-long-link"
}

🎯 هدفم از ساختش

این پروژه بخشی از مسیر یادگیری منه توی دنیای بک‌اند پایتون 💻
توش یاد گرفتم:

چطور یه REST API واقعی بسازم

چطور دیتابیس رو با SQLModel هندل کنم

Dependency Injection چیه

و اینکه چطوری یه پروژه‌ی کوچیک ولی تمیز و استاندارد بسازم

🚧 برنامه‌های بعدی

🔹 اضافه کردن لاگین و اکانت کاربر
🔹 تولید QR Code برای لینک‌ها
🔹 نمایش گراف آمار کلیک‌ها
🔹 دیپلوی روی Render یا Railway



❤️ مشارکت و توسعه

اگر ایده‌ای برای بهبود پروژه داری یا خواستی فیچر جدیدی اضافه کنی،
خیلی خوشحال می‌شم Pull Request بدی یا توی Issues بنویسی 💬

Developed with ☕ and ❤️!
