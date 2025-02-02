import json
from swarm import Swarm
from agents.setting_agent import SettingAgent
from agents.character_agent import CharacterAgent
from agents.plot_agent import PlotAgent
from dotenv import load_dotenv
import os

# Load environment variables (e.g. OPENAI_API_KEY)
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


def extract_balanced_json(text: str, start_index: int) -> str:
    """
    Extracts a balanced JSON substring from 'text' starting at 'start_index'.
    Returns the substring that contains a balanced set of curly braces.
    """
    stack = []
    i = start_index
    in_string = False
    escape = False

    while i < len(text):
        char = text[i]
        if char == '"' and not escape:
            in_string = not in_string
        if not in_string:
            if char == '{':
                stack.append('{')
            elif char == '}':
                if not stack:
                    # Should not happen; break out.
                    break
                stack.pop()
                if not stack:
                    # When the stack is empty, we found a balanced JSON object.
                    return text[start_index:i+1]
        # Update escape flag: if we see a backslash and we're not already escaping, set escape True.
        if char == '\\' and not escape:
            escape = True
        else:
            escape = False
        i += 1
    return None  # No balanced JSON object found


def extract_tool_call(response_text: str):
    """
    Extracts and parses a JSON object containing a "tool_call" key from the response text.
    """
    start_index = response_text.find('{"tool_call"')
    if start_index == -1:
        return None

    json_str = extract_balanced_json(response_text, start_index)
    if json_str:
        try:
            return json.loads(json_str)
        except json.JSONDecodeError as e:
            print("JSON decode error:", e)
    return None


def run_brainstorm():
    """
    Orchestrates the cyclical brainstorming:
      1) Starts with SettingAgent.
      2) Uses shared context to track iterations.
      3) Attempts to detect a structured tool call in the agent's output.
    """
    client = Swarm()

    user_prompt = {
        "role": "user",
        "content": "I need creative ideas for a sci-fi short story set in the 22nd century."
    }

    # Start with SettingAgent.
    initial_agent = SettingAgent

    # Shared context for iteration tracking.
    initial_context = {
        "iteration": 0,
        "max_iterations": 3,
    }

    # Run the conversation.
    response = client.run(
        agent=initial_agent,
        messages=[user_prompt],
        context_variables=initial_context,
        debug=True  # Set to True for detailed debug logs.
    )

    # Retrieve the last message from the agent's output.
    last_message = response.messages[-1]["content"]
    print("Raw agent output:")
    print(last_message)
    
    # Attempt to extract the tool call from the output.
    tool_call_data = extract_tool_call(last_message)
    if tool_call_data:
        print("Extracted tool call:", tool_call_data)
        # Example: if the tool call's name is "setting_to_character", execute it.
        if tool_call_data.get("tool_call", {}).get("name") == "setting_to_character":
            from agents.setting_agent import setting_to_character  # Import the function
            result = setting_to_character(response.context_variables)
            print("Executed tool call result:", result)
    else:
        print("No valid tool call found in the output.")

    return response


# if __name__ == "__main__":
#     final_response = run_brainstorm()
#     print("Final Response:")
#     print(final_response)
