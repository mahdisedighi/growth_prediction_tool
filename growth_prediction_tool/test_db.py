import pymongo

def test_mongo_connection():
    """
    Connect to your MongoDB Atlas cluster using PyMongo,
    list all databases, and list collections in the 'vatche' database.
    """

    # Replace this URI ONLY if you need to change the database name or credentials.
    # Otherwise, keep it exactly as provided by Atlas if you just want to confirm
    # that your connection works.
    MONGO_URI = (
        "mongodb+srv://vatche:tmboozik@cluster0.vs028.mongodb.net/"
        "?retryWrites=true&w=majority&appName=Cluster0"
    )

    # Initialize the client with your Atlas connection string
    print("Connecting to MongoDB Atlas...")
    client = pymongo.MongoClient(MONGO_URI)

    # Force a connection by listing database names (this pings the cluster)
    db_list = client.list_database_names()
    print("Databases found:", db_list)

    # If you want to check a specific database (e.g. 'growth' or 'vatche'):
    db_name = "growth"  # or "growth", depending on which you actually want to use
    db = client[db_name]

    # List collections in that database
    collections = db.list_collection_names()
    print(f"Collections in '{db_name}': {collections}")

    print("✓ Successfully connected to MongoDB Atlas!")

if __name__ == "__main__":
    test_mongo_connection()
