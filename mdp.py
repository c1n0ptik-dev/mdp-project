import random

class FinancesMDP:
    def __init__(self, seed=None, max_steps=90, gamma=0.9):
        self.rng = random.Random(seed)
        self.max_steps = max_steps
        self.gamma = gamma
        self.state = None
        self.time = 0

        self.states = ["Rich", "Some", "Broke"]

        # a(s)
        self.actions = {
            "Rich":  ["Invest", "Spend", "Work"],
            "Some":  ["Invest", "Spend", "Work"],
            "Broke": ["Work"],
        }

        # p(s' | s, a)
        self.transitions = {
            ("Rich", "Invest"):  {"Rich": 0.7, "Some": 0.2, "Broke": 0.1},
            ("Rich", "Spend"):   {"Rich": 0.3, "Some": 0.6, "Broke": 0.1},
            ("Rich", "Work"):    {"Rich": 1.0, "Some": 0.0, "Broke": 0.0},
            ("Some", "Invest"):  {"Rich": 0.3, "Some": 0.3, "Broke": 0.4},
            ("Some", "Spend"):   {"Rich": 0.0, "Some": 0.5, "Broke": 0.5},
            ("Some", "Work"):    {"Rich": 0.1, "Some": 0.9, "Broke": 0.0},
            ("Broke", "Work"):   {"Rich": 0.0, "Some": 0.5, "Broke": 0.5},
        }

        # r(s, a)
        self.rewards = {
            ("Rich", "Invest"): 5,
            ("Rich", "Spend"):  9,
            ("Rich", "Work"):  -2,
            ("Some", "Invest"): 3,
            ("Some", "Spend"):  8,
            ("Some", "Work"):  -2,
            ("Broke", "Work"): -1,
        }

        # bonus(s')
        self.bonus = {"Rich": 5, "Some": 0, "Broke": -8}

        # start distribution 
        self.start_distribution = {"Rich": 0.1, "Some": 0.6, "Broke": 0.3}

    def reset(self):
        self.state = None
        self.time = 0
        return self.state

    def q_value(self, s, a, V):
        return sum(p * (self.rewards[(s, a)] + self.bonus[s2] + self.gamma * V[s2]) 
                    for s2, p in self.transitions[(s, a)].items())

    def compute_best_policy(self):
        V = {s: 0 for s in self.states}
        policy = {s: "" for s in self.states}

        for _ in range(self.max_steps):
            V_new = V.copy()

            for state in V:
                q = []
                for action in self.actions[state]:
                    q.append((self.q_value(state, action, V), action))

                V_new[state] = max(q)[0]
                policy[state] = max(q)[1]

            V = V_new
        return policy

env = FinancesMDP()
print(env.compute_best_policy())

    

    