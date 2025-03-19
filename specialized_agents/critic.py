from framework.agent_base import AgentBase
from integrations.llm_provider import LLMProvider
from protocols.collaboration import get_next_agent

class Critic(AgentBase):
    def __init__(self, name, memory_pool, message_bus):
        super().__init__(name, memory_pool, message_bus)
        self.llm = LLMProvider()

    def process_message(self, sender, message):
        if message['type'] == 'execution_result':
            result = message['data']
            workflow = message['workflow']
            self.logger.info("Evaluating execution result")
            evaluation = self.llm.query(f"Evaluate the following execution result: {result}")
            next_agent = get_next_agent(self.name, workflow)
            self.send_message(next_agent, {
                'type': 'evaluation',
                'data': evaluation,
                'workflow': workflow
            })
        else:
            self.logger.warning(f"Received unknown message type: {message['type']}")