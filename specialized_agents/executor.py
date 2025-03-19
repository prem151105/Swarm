from framework.agent_base import AgentBase
from integrations.llm_provider import LLMProvider
from protocols.collaboration import get_next_agent

class Executor(AgentBase):
    def __init__(self, name, memory_pool, message_bus):
        super().__init__(name, memory_pool, message_bus)
        self.llm = LLMProvider()

    def process_message(self, sender, message):
        if message['type'] == 'plan':
            plan = message['data']
            workflow = message['workflow']
            self.logger.info("Executing plan")
            execution_result = self.llm.query(f"Simulate the execution of the following plan: {plan}")
            next_agent = get_next_agent(self.name, workflow)
            self.send_message(next_agent, {
                'type': 'execution_result',
                'data': execution_result,
                'workflow': workflow
            })
        else:
            self.logger.warning(f"Received unknown message type: {message['type']}")