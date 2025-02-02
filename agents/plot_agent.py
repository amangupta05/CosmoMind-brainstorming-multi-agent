from swarm import Agent
from swarm.types import Result

def plot_to_setting(context_variables):
    """
    Increments iteration, checks the stopping condition,
    and hands control back to SettingAgent if not done.
    """
    iteration = context_variables.get("iteration", 0)
    max_iterations = context_variables.get("max_iterations", 3)

    iteration += 1
    context_variables["iteration"] = iteration

    if iteration >= max_iterations:
        return "Done! (PlotAgent reached max iterations.)"
    else:
        # To avoid circular imports, do a local import of SettingAgent.
        from agents.setting_agent import SettingAgent
        return Result(
            value="PlotAgent passing to SettingAgent",
            agent=SettingAgent,  # Pass the actual Agent instance
            context_variables=context_variables,
        )

PlotAgent = Agent(
    name="PlotAgent",
    instructions=(
        "You are the PlotAgent. Your role is to refine the storyline, integrating the setting "
        "and characters into a coherent plot. When ready to hand off control back to the SettingAgent, "
        "output ONLY the following JSON object EXACTLY as shown and nothing else:\n\n"
        "{\"tool_call\": {\"name\": \"plot_to_setting\", \"arguments\": {}}}\n\n"
        "Do not include any additional text, narrative, or formatting."
    ),
    functions=[plot_to_setting],
    model="gpt-4",
)
