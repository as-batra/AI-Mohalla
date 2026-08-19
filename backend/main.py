
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
    def act(self, environment):
      self.change_state("thinking")

      if self.goals:
        goal = self.goals[0]
        print(f"{self.name} is working on: {goal}")
      self.change_state("finished")

    def send_message(self, environment, receiver, content):
      self.change_state("communicating")

      message = Message(
        sender=self,
        receiver=receiver,
        content=content
      )

      environment.send_message(message)  
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
    def __repr__(self):
      return f"Message(from={self.sender.name}, to={self.receiver.name}, content='{self.content}')"       
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
print(coder.short_term_memory)
researcher.set_goal(
    "Find a suitable dataset for sentiment analysis"
)
researcher.act(environment)
researcher.send_message(
    environment,
    coder,
    "I found a suitable sentiment analysis dataset."
)