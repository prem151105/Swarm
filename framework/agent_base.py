# framework/agent_base.py
from abc import ABC, abstractmethod
import threading
import time
import logging

class AgentBase(ABC):
    def __init__(self, name, memory_pool, message_bus):
        """Initialize the agent with a name, shared memory, and message bus."""
        self.name = name
        self.memory_pool = memory_pool
        self.message_bus = message_bus
        self.logger = logging.getLogger(self.name)
        self.running = False

    def start(self):
        """Start the agent in its own thread."""
        self.running = True
        self.thread = threading.Thread(target=self.run)
        self.thread.start()

    def stop(self):
        """Stop the agent and wait for its thread to finish."""
        self.running = False
        self.thread.join()

    @abstractmethod
    def process_message(self, sender, message):
        """Abstract method that each agent must implement to handle messages."""
        pass

    def run(self):
        """Main loop where the agent checks for and processes messages."""
        while self.running:
            message = self.message_bus.receive(self.name)
            if message:
                sender, msg = message
                self.process_message(sender, msg)
            time.sleep(0.1)  # Prevent busy waiting

    def send_message(self, recipient, message):
        """Send a message to another agent via the message bus."""
        self.message_bus.send(self.name, recipient, message)