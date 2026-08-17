
class Agent:
    def __init__(self, name, role, personality, llm):
        self.name = name
        self.role = role
        self.personality = personality
        self.llm = llm
        self.short_term_memory = []
        self.long_term_memory = []
        self.goals = []
        self.state="idle"
    def set_goal(self, goal):
        self.goals.append(goal)
        print(f"{self.name} received a new goal: {goal}")
    def change_state(self, new_state):
         self.state = new_state
         print(f"{self.name} is now {self.state}")    

researcher = Agent(name="Researcher",
    role="Research information and provide findings",
    personality="Curious and skeptical",
    llm=None
)
researcher.set_goal("Find a suitable dataset for sentiment analysis")        
researcher.change_state("thinking")

coder = Agent(name="Researcher",
    role="Research information and provide findings",
    personality="Curious and skeptical",
    llm=None
)

researcher = Agent(name="Researcher",
    role="Research information and provide findings",
    personality="Curious and skeptical",
    llm=None
)