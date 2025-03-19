import json

def serialize_message(message):
    """Serialize a message dictionary to a JSON string."""
    return json.dumps(message)

def deserialize_message(message_str):
    """Deserialize a JSON string to a message dictionary."""
    return json.loads(message_str)