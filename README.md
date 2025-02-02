# 🌌 CosmoMind – Brainstorming with OpenAI Swarm 🚀

**CosmoMind** is a futuristic, multi-agent brainstorming system powered by **OpenAI Swarm**. It enables AI-driven agents to collaborate, refine ideas, and generate creative concepts in an interstellar-inspired environment.

---

## 🚀 Features

✅ Multi-agent framework using **OpenAI Swarm**  
✅ AI-driven iterative brainstorming & idea refinement  
✅ Modular design with distinct **SettingAgent**, **CharacterAgent**, and **PlotAgent**  
✅ Dynamic negotiation and handoff between agents  
✅ Extensible architecture for further enhancements  

---

## 📂 Project Structure

```
CosmoMind-brainstorming-multi-agent/
│── agents/
│   ├── setting_agent.py       # Handles setting brainstorming
│   ├── character_agent.py     # Develops characters
│   ├── plot_agent.py          # Crafts storylines
│── .env                       # Stores OpenAI API key (DO NOT COMMIT)
│── .gitignore                 # Ignores .env and unnecessary files
│── orchestrator.py            # Controls agent interactions
│── main.py                    # Entry point for running the project
│── README.md                  # Project documentation
```

---

## 🛠 Installation & Setup

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/amangupta05/CosmoMind-brainstorming-multi-agent.git
cd CosmoMind-brainstorming-multi-agent
```

### **2️⃣ Set Up a Virtual Environment**
```bash
python3 -m venv env
source env/bin/activate   # On macOS/Linux
env\Scripts\activate      # On Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Configure API Keys**
Create a `.env` file in the root directory and add your **OpenAI API key**:
```bash
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

---

## ▶️ Usage

Run the main entry point:
```bash
python main.py
```
This will start the brainstorming session, where agents will interact to generate ideas.

---

## 🤖 How It Works

1️⃣ **SettingAgent** generates a sci-fi setting.  
2️⃣ **CharacterAgent** creates compelling characters.  
3️⃣ **PlotAgent** refines the storyline.  
4️⃣ The **Orchestrator** manages the interactions and ensures smooth handoffs.  

Each agent iteratively contributes to refining the ideas using **OpenAI Swarm**.

---

## 🏗️ Extending the Project

Want to add a new agent?  
1. Create a new file inside the `agents/` folder, e.g., `theme_agent.py`.  
2. Define a new `Agent` in the file:
   ```python
   from swarm import Agent

   ThemeAgent = Agent(
       name="ThemeAgent",
       instructions="You are responsible for defining the overarching themes.",
       model="gpt-4",
   )
   ```
3. Update `orchestrator.py` to include the new agent.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Submit pull requests
- Report issues
- Suggest enhancements

---

## 📜 License

This project is licensed under the **MIT License**.  
Feel free to use, modify, and distribute it.

---

## 📬 Contact

For any questions or collaboration, reach out via:  
📧 **Email:** amangupta52001@gmail.com  
🐙 **GitHub:** [amangupta05](https://github.com/amangupta05)  

Happy brainstorming! 🚀🌌

