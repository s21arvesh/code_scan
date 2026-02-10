import os
import requests
from flask import Flask

app = Flask(__name__)

# 🔐 CREDENTIAL LEAKS - These will be detected by TruffleHog & Gitleaks
API_KEY = "sk-1234567890abcdef"  # Stripe-like key
DB_PASSWORD = "super_secret_password_123"  # Password
GITHUB_TOKEN = "ghp_1234567890abcdef1234567890abcdef12345678"  # GitHub token
AWS_SECRET = "AKIAIOSFODNN7EXAMPLE"  # AWS access key
JWT_SECRET = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"  # JWT token

# Database connection with credentials
DATABASE_URL = "postgresql://user:password_123@localhost:5432/dbname"  # DB URL

@app.route('/')
def home():
    # API call with sensitive data
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'X-API-Key': GITHUB_TOKEN
    }
    response = requests.get('https://api.example.com/data', headers=headers)
    return response.json()

if __name__ == '__main__':
    app.run(debug=True)
