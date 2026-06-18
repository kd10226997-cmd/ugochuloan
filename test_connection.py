from pymongo import MongoClient

MONGODB_URI = "mongodb+srv://euawari_db_user:6SnKvQvXXzrGeypA@cluster0.fkkzcvz.mongodb.net/microfinance_db?retryWrites=true&w=majority"

print("🔄 Testing connection...")
print(f"Connection string: {MONGODB_URI}\n")

try:
    client = MongoClient(MONGODB_URI, serverSelectionTimeoutMS=5000)
    client.admin.command('ping')
    print("✅ SUCCESS! Connected to MongoDB Atlas!")
    
    # List databases
    databases = client.list_database_names()
    print(f"\n📊 Databases found: {databases}")
    
    client.close()
    
except Exception as e:
    print(f"❌ Connection Failed: {e}")