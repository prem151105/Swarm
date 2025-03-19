# framework/memory_pool.py
import threading

class MemoryPool:
    def __init__(self):
        """Initialize the shared memory pool."""
        self.memory = {}
        self.lock = threading.Lock()

    def get(self, key):
        """Retrieve a value from the memory pool."""
        with self.lock:
            return self.memory.get(key)

    def set(self, key, value):
        """Store a value in the memory pool."""
        with self.lock:
            self.memory[key] = value