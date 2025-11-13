from flask import Flask
import ssl

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>🌐 اتصال امن Flask (TLS فعال)</h1><p>این صفحه از طریق HTTPS در GitHub Codespaces اجرا شده است.</p>'

if __name__ == '__main__':
    context = ('cert.pem', 'key.pem')
    app.run(host='0.0.0.0', port=5000, ssl_context=context)
