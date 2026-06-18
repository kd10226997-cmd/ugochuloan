from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from datetime import datetime

MONGODB_URI = "mongodb+srv://euawari_db_user:6SnKvQvXXzrGeypA@cluster0.fkkzcvz.mongodb.net/microfinance_db?retryWrites=true&w=majority"

print("🔄 Connecting to MongoDB...")

try:
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=30000)
    db = client["microfinance_db"]
    
    print("✅ Connected!")
    
    # Delete all users
    print("🗑️ Deleting old users...")
    result = db['users'].delete_many({})
    print(f"✅ Deleted {result.deleted_count} users")
    
    # Create admin account
    print("➕ Creating admin account...")
    hashed_pwd = generate_password_hash("admin123", method='pbkdf2:sha256')
    
    db['users'].insert_one({
        "username": "admin",
        "password": hashed_pwd,
        "role": "admin",
        "status": "approved",
        "created_at": datetime.now()
    })
    
    print("\n" + "="*50)
    print("✅ ADMIN ACCOUNT CREATED!")
    print("="*50)
    print("Username: admin")
    print("Password: admin123")
    print("="*50)
    
    client.close()
    print("✅ Done!")
    
except Exception as e:
    print(f"❌ Error: {e}")