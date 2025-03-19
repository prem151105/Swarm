import math
import datetime

class Tool:
    """Base class for all tools."""
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def execute(self, input_data):
        """Execute the tool's functionality. Must be implemented by subclasses."""
        raise NotImplementedError("Subclasses must implement execute method")

class MathTool(Tool):
    """Tool to evaluate mathematical expressions."""
    def __init__(self):
        super().__init__("MathTool", "Evaluates mathematical expressions")

    def execute(self, expression):
        """Evaluate a mathematical expression and return the result as a string."""
        try:
            # Restrict eval to math module functions for safety
            allowed_names = {k: v for k, v in math.__dict__.items() if not k.startswith("__")}
            result = eval(expression, {"__builtins__": None}, allowed_names)
            return str(result)
        except Exception as e:
            return f"Error evaluating expression: {e}"

class DateTimeTool(Tool):
    """Tool to provide the current date and time."""
    def __init__(self):
        super().__init__("DateTimeTool", "Provides current date and time")

    def execute(self, input_data=None):
        """Return the current date and time as a formatted string."""
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return current_time

class ToolRegistry:
    """Registry to manage available tools."""
    def __init__(self):
        self.tools = {}

    def register_tool(self, tool):
        """Register a tool in the registry."""
        self.tools[tool.name] = tool

    def get_tool(self, name):
        """Retrieve a tool by its name."""
        return self.tools.get(name)

# Global registry instance
registry = ToolRegistry()

# Register initial tools
registry.register_tool(MathTool())
registry.register_tool(DateTimeTool())

# Helper functions for external use
def register_tool(tool):
    """Add a tool to the global registry."""
    registry.register_tool(tool)

def get_tool(name):
    """Get a tool from the global registry by name."""
    return registry.get_tool(name)