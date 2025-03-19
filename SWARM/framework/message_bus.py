# framework/message_bus.py
from collections import defaultdict, deque
import threading

class MessageBus:
    def __init__(self):
        """Initialize the message bus with queues for each agent."""
        self.queues = defaultdict(deque)
        self.lock = threading.Lock()
        self.agent_list = set()  # Track registered agents

    def register_agent(self, agent_name: str):
        """Register an agent to receive messages."""
        with self.lock:
            self.agent_list.add(agent_name)

    def send(self, sender: str, recipient: str, message: dict):
        """Send a message from sender to recipient, supporting broadcast to 'all'."""
        with self.lock:
            if recipient == 'all':
                for agent in self.agent_list:
                    if agent != sender:  # Exclude sender from broadcast
                        self.queues[agent].append((sender, message))
            else:
                self.queues[recipient].append((sender, message))

    def receive(self, recipient: str):
        """Retrieve the next message for the recipient, if any."""
        with self.lock:
            if recipient in self.queues and self.queues[recipient]:
                return self.queues[recipient].popleft()
        return None