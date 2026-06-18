from pymongo import MongoClient
from werkzeug.security import generate_password_hash
from datetime import datetime

# Your MongoDB connection
MONGODB_URI = "mongodb+srv://euawari_db_user:6SnKvQvXXzrGeypA@cluster0.fkkzcvz.mongodb.net/microfinance_db?retryWrites=true&w=majority"

print("🔄 Connecting to MongoDB...")

try:
    client = MongoClient(MONGODB_URI)
    db = client["microfinance_db"]
    
    print("✅ Connected to MongoDB!")
    
    # Delete ALL old users
    print("🗑️  Clearing old users...")
    users_col = db['users']
    result = users_col.delete_many({})
    print(f"✅ Deleted {result.deleted_count} old users")
    
    # Create new admin account
    print("➕ Creating admin account...")
    admin_password = generate_password_hash("admin123")
    
    users_col.insert_one({
        "username": "admin",
        "password": admin_password,
        "role": "admin",
        "status": "approved",
        "created_at": datetime.now()
    })
    
    print("\n" + "="*50)
    print("✅ ADMIN ACCOUNT CREATED!")
    print("="*50)
    print("Username: admin")
    print("Password: admin123")
    print("="*50 + "\n")
    
    client.close()
    print("✅ Done! You can now login to your app.")
    
except Exception as e:
    print(f"❌ Error: {e}")