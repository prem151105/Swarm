# protocols/collaboration.py
from framework.message_bus import MessageBus

class CollaborationProtocol:
    def __init__(self, message_bus: MessageBus):
        """Initialize the collaboration protocol with a message bus for communication."""
        self.message_bus = message_bus

    def request_assistance(self, agent_name: str, task: dict):
        """Broadcast a request for assistance with a task to all agents."""
        message = {
            'type': 'assistance_request',
            'task': task,
            'from': agent_name
        }
        self.message_bus.send(agent_name, 'all', message)

    def share_knowledge(self, agent_name: str, knowledge: dict):
        """Broadcast knowledge to all agents."""
        message = {
            'type': 'knowledge_share',
            'knowledge': knowledge,
            'from': agent_name
        }
        self.message_bus.send(agent_name, 'all', message)

    def respond_to_assistance(self, agent_name: str, requester: str, response: dict):
        """Send a direct response to an assistance request."""
        message = {
            'type': 'assistance_response',
            'response': response,
            'from': agent_name
        }
        self.message_bus.send(agent_name, requester, message)