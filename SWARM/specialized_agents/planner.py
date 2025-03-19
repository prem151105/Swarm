from framework.agent_base import AgentBase
from integrations.llm_provider import LLMProvider
from protocols.collaboration import get_next_agent

class Planner(AgentBase):
    def __init__(self, name, memory_pool, message_bus):
        super().__init__(name, memory_pool, message_bus)
        self.llm = LLMProvider()

    def process_message(self, sender, message):
        if message['type'] == 'research_results':
            data = message['data']
            workflow = message['workflow']
            self.logger.info("Creating plan based on research data")
            plan = self.llm.query(f"Based on the following research data, create a strategic plan: {data}")
            next_agent = get_next_agent(self.name, workflow)
            self.send_message(next_agent, {
                'type': 'plan',
                'data': plan,
                'workflow': workflow
            })
        else:
            self.logger.warning(f"Received unknown message type: {message['type']}")