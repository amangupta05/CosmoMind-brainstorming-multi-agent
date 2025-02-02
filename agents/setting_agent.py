from swarm import Agent
from swarm.types import Result  # Import Result from swarm.types
from agents.character_agent import CharacterAgent  # Import the CharacterAgent instance

def setting_to_character(context_variables):
    """
    Increments iteration, checks the stopping condition,
    and hands off to CharacterAgent if max iterations are not reached.
    """
    iteration = context_variables.get("iteration", 0)
    max_iterations = context_variables.get("max_iterations", 3)

    iteration += 1
    context_variables["iteration"] = iteration

    # If we've reached or exceeded max_iterations, return a "Done" message.
    if iteration >= max_iterations:
        return "Done! (SettingAgent reached max iterations.)"
    else:
        # Return a Result that hands off control to CharacterAgent.
        return Result(
            value="SettingAgent passing to CharacterAgent",
            agent=CharacterAgent,  # Pass the actual Agent instance
            context_variables=context_variables,
        )

SettingAgent = Agent(
    name="SettingAgent",
    instructions=(
        "You are the SettingAgent. Your role is to propose or refine a futuristic environment "
        "for a 22nd-century sci-fi story. When you are ready to hand off control to the CharacterAgent, "
        "output ONLY the following JSON object EXACTLY as shown and nothing else:\n\n"
        "{\"tool_call\": {\"name\": \"setting_to_character\", \"arguments\": {}}}\n\n"
        "Do not include any additional text, narrative, or formatting."
    ),
    functions=[setting_to_character],
    model="gpt-4",
)
