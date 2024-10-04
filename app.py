from flask import Flask
import redis
import os

app = Flask(__name__)

# الاتصال بـ Redis باستخدام متغير بيئي لتحديد المضيف
cache = redis.Redis(host=os.environ.get('REDIS_HOST', 'localhost'), port=6379)

@app.route('/')
def home():
    try:
        # زيادة عدد الزيارات المخزنة في Redis
        count = cache.incr('hits')
    except redis.exceptions.ConnectionError as e:
        count = f"Error: {e}"

    return f"""
    <html>
        <head>
            <title>Flask-Redis App</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    background-color: #f4f4f9;
                }}
                h1 {{
                    color: #333;
                }}
                p {{
                    font-size: 18px;
                    line-height: 1.6;
                }}
                .highlight {{
                    color: #007bff;
                    font-weight: bold;
                }}
            </style>
        </head>
        <body>
            <h1>Welcome to the Flask-Redis App!</h1>
            <p>This project demonstrates how to use <span class="highlight">Flask</span> with <span class="highlight">Redis</span> to track the number of visits to this page.</p>
            <p>It has been visited <span class="highlight">{count}</span> times.</p>
            <p>The project is fully containerized using <span class="highlight">Docker Compose</span>, and includes persistent storage through <span class="highlight">Docker Volumes</span> and isolated networking with <span class="highlight">Docker Networks</span>.</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=6001)  # تم تغيير المنفذ إلى 6001
