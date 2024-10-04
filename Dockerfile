# استخدام Python 3.10 على بيئة Alpine خفيفة الوزن
FROM python:3.10-alpine

# تحديد مجلد العمل
WORKDIR /code

# تعيين متغيرات البيئة لتشغيل Flask
ENV FLASK_APP=app.py
ENV FLASK_ENV=development  
ENV FLASK_RUN_HOST=0.0.0.0

# تثبيت الحزم الضرورية للبناء
RUN apk add --no-cache gcc musl-dev linux-headers

# نسخ ملف المتطلبات وتثبيتها
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# نسخ جميع الملفات في المجلد الحالي إلى مجلد العمل داخل الحاوية
COPY . .

# أمر التشغيل لتشغيل Flask
CMD ["flask", "run", "--host=0.0.0.0", "--port=6001"]  # تعيين المنفذ إلى 6001
