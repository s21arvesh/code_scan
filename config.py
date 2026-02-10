# Configuration file with various credential types

class Config:
    # 🔐 API Keys and Tokens
    STRIPE_SECRET_KEY = "sk_live_1234567890abcdef"
    GOOGLE_API_KEY = "AIzaSyC123abcDEF456ghiJKL789mno"
    SLACK_BOT_TOKEN = "xoxb-1234567890-1234567890-abcdef123456"
    
    # 🔐 Database Credentials
    DATABASE_CONFIG = {
        'host': 'localhost',
        'user': 'admin',
        'password': 'P@ssw0rd!123',
        'database': 'production_db'
    }
    
    # 🔐 Service Credentials
    REDIS_URL = "redis://:redis_password_123@localhost:6379/0"
    SMTP_PASSWORD = "email_smtp_pass_456"
    
    # 🔐 Encryption Keys
    ENCRYPTION_KEY = "AES256SecretKey12345678901234567890"
    PRIVATE_KEY = """-----BEGIN PRIVATE KEY-----
MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC...
-----END PRIVATE KEY-----"""
