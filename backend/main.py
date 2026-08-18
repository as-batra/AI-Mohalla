
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
    def receive_message(self, message):
        self.short_term_memory.append(message)
        print(
        f"{self.name} received a message from "
        f"{message.sender.name}: {message.content}"
        )      

researcher = Agent(name="AI Researcher",
    role="Research information and provide findings",
    personality="Curious and skeptical",
    llm=None
)

coder = Agent(name="AI Coder",
    role="Write code based on research findings",
    personality="Analytical and detail-oriented",
    llm=None
)

critic = Agent(name="AI Critic",
    role="Evaluate the code and provide feedback",
    personality="Critical and constructive",
    llm=None
)

class Message:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
message = Message(
    sender=researcher,
    receiver=coder,
    content="I found a suitable sentiment analysis dataset."
)    
class Environment:
    def __init__(self):
        self.messages = []
        self.agents = []
    def add_agent(self, agent):
        self.agents.append(agent)   
    def send_message(self, message):
        self.messages.append(message)
        message.receiver.receive_message(message)         
environment = Environment()

environment.add_agent(researcher)
environment.add_agent(coder)
environment.add_agent(critic)
