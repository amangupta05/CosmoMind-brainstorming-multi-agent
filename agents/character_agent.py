from swarm import Agent

# Define and export the CharacterAgent as an Agent instance.
CharacterAgent = Agent(
    name="CharacterAgent",
    instructions=(
        "You are the CharacterAgent. Your role is to develop characters for a "
        "22nd-century sci-fi story. When handed off control, please continue the narrative."
    ),
    model="gpt-4",
)
