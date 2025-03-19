import time
from utils.logging import setup_logging
from utils.config import load_config
from framework.swarm_manager import SwarmManager
from framework.memory_pool import MemoryPool
from framework.message_bus import MessageBus
from specialized_agents.researcher import Researcher
from specialized_agents.planner import Planner
from specialized_agents.executor import Executor
from specialized_agents.critic import Critic
from specialized_agents.coordinator import Coordinator
import logging

def main():
    # Set up logging
    logger = setup_logging(log_level=logging.INFO)
    logger.info("Starting AI-Agent-Swarm")

    # Load configuration
    config = load_config('config.yaml')
    logger.info("Configuration loaded successfully")

    # Initialize core components
    memory_pool = MemoryPool()
    message_bus = MessageBus()

    # Define agent roles for task routing (this could also come from config.yaml)
    agent_roles = {
        "Coordinator": "coordination",
        "Researcher": "research",
        "Planner": "planning",
        "Executor": "execution",
        "Critic": "evaluation"
    }

    # Update config with agent roles
    config['agent_roles'] = agent_roles

    # Initialize the swarm manager with the config
    swarm = SwarmManager(config)
    
    # Override the default agent initialization with actual agent instances
    swarm.agents = [
        Coordinator("Coordinator", memory_pool, message_bus),
        Researcher("Researcher", memory_pool, message_bus),
        Planner("Planner", memory_pool, message_bus),
        Executor("Executor", memory_pool, message_bus),
        Critic("Critic", memory_pool, message_bus)
    ]

    # Register agents with the message bus for broadcasting
    for agent in swarm.agents:
        message_bus.register_agent(agent.name)

    # Start the swarm
    logger.info("Starting the swarm")
    swarm.start_swarm()

    # Submit an example task
    example_task = {
        "type": "task",
        "task": "Investigate the impact of AI on healthcare",
        "workflow": "complete_task"
    }
    swarm.submit_task(example_task)
    logger.info(f"Submitted task: {example_task['task']}")

    # Wait for the task to complete (simulated with a sleep; in a real system, use a completion signal)
    logger.info("Waiting for swarm to process task...")
    time.sleep(15)  # Adjust this based on task complexity and LLM response time

    # Retrieve and log the final result from the memory pool
    final_result = memory_pool.get('final_result')
    if final_result:
        logger.info(f"Final result: {final_result}")
    else:
        logger.warning("No final result found in memory pool")

    # Stop the swarm
    logger.info("Stopping the swarm")
    swarm.stop_swarm()

if __name__ == "__main__":
    main()