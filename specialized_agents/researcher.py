from framework.agent_base import AgentBase
from integrations.llm_provider import LLMProvider
from protocols.collaboration import get_next_agent

class Researcher(AgentBase):
    def __init__(self, name, memory_pool, message_bus):
        super().__init__(name, memory_pool, message_bus)
        self.llm = LLMProvider()

    def process_message(self, sender, message):
        if message['type'] == 'research_task':
            topic = message['topic']
            workflow = message['workflow']
            self.logger.info(f"Researching topic: {topic}")
            results = self.llm.query(f"Provide research information on {topic}")
            next_agent = get_next_agent(self.name, workflow)
            self.send_message(next_agent, {
                'type': 'research_results',
                'data': results,
                'workflow': workflow
            })
        else:
            self.logger.warning(f"Received unknown message type: {message['type']}")