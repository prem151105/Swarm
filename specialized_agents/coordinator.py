from framework.agent_base import AgentBase
from protocols.collaboration import workflows

class Coordinator(AgentBase):
    def process_message(self, sender, message):
        if message['type'] == 'task':
            task = message['task']
            workflow_key = message.get('workflow', 'complete_task')
            workflow = workflows.get(workflow_key, [])
            if not workflow:
                self.logger.error(f"Unknown workflow: {workflow_key}")
                return
            first_agent = workflow[0]
            self.logger.info(f"Starting workflow {workflow_key} for task: {task}")
            self.send_message(first_agent, {
                'type': 'research_task',
                'topic': task,
                'workflow': workflow_key
            })
        elif message['type'] == 'evaluation':
            evaluation = message['data']
            self.logger.info(f"Received evaluation: {evaluation}")
            self.memory_pool.set('final_result', evaluation)
        else:
            self.logger.warning(f"Received unknown message type: {message['type']}")