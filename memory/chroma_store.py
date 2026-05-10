import chromadb
import uuid

# Persistent local database
client = chromadb.PersistentClient(
    path="./chroma_db"
)

# Create collection
collection = client.get_or_create_collection(
    name="travel_memory"
)

# -----------------------------
# SAVE MEMORY
# -----------------------------
def save_memory(user_id: str, text: str):

    # Ignore empty users
    if not user_id:
        return

    collection.add(

        documents=[text],

        metadatas=[
            {
                "user_id": user_id
            }
        ],

        ids=[str(uuid.uuid4())]
    )

# -----------------------------
# RETRIEVE MEMORY
# -----------------------------
def retrieve_memory(user_id: str):

    # Fresh search mode
    if not user_id:
        return []

    try:

        results = collection.get(

            where={
                "user_id": user_id
            }
        )

        documents = results.get(
            "documents",
            []
        )

        # Return last 3 memories only
        return documents[-3:]

    except Exception as e:

        print(
            f"Memory retrieval error: {e}"
        )

        return []

# -----------------------------
# CLEAR MEMORY
# -----------------------------
def clear_memory(user_id: str):

    try:

        results = collection.get(
            where={
                "user_id": user_id
            }
        )

        ids = results.get("ids", [])

        if ids:

            collection.delete(ids=ids)

    except Exception as e:

        print(
            f"Memory clear error: {e}"
        )