# MDP project: personal finance

The idea comes from personal finance in everyday life: every year you decide whether to work, spend or invest, and that choice affects how much money you have next year.

Before this, I tried a few other ideas: a Counter-Strike 2 economy model and a crypto trading model. The CS2 model became too complicated, because winning a round depends on much more than money, so I switched to something simpler where the states and actions are easier to define.

The probabilities are my own estimates, based on how money usually work in real life. Rich people have more stability: even when they spend or invest, they are still likely to stay rich. People with some money are more unstable, so spending can easily push them down to broke. For broke people, working is the only option, and it slowly helps them climb back up. These numbers are not based on real data and they are a simple way to model the idea that money makes it easier to keep money.

### States
S = { Rich, Some, Broke }

### Actions
A = { Invest, Spend, Work }

- a(Rich) = { Invest, Spend, Work }
- a(Some) = { Invest, Spend, Work }
- a(Broke) = { Work } 

### Transition probabilities p(s'|s, a) 

It was changed the values of spend probabilites for rich people, so now investment will also be a valuable point-wise option. Also for Some it is higher chance to get rich through investment, but also higher probability of getting broken than work. 

| s     | a      | p(Rich) | p(Some) | p(Broke) |
|-------|--------|---------|---------|----------|
| Rich  | Invest | 0.7     | 0.2     | 0.1      |
| Rich  | Spend  | 0.3     | 0.6     | 0.1      |
| Rich  | Work   | 1       | 0       | 0        |
| Some  | Invest | 0.3     | 0.3     | 0.4      |
| Some  | Spend  | 0       | 0.5     | 0.5      |
| Some  | Work   | 0.1     | 0.9     | 0        |
| Broke | Work   | 0       | 0.5     | 0.5      |

### Rewards r(s, a)

| s \ a | Invest | Spend | Work |
|-------|--------|-------|------|
| Rich  | 5      | 9     | -2   |
| Some  | 3      | 8     | -2   |
| Broke | -      | -     | -1   |

#### State bonus bonus(s')

| s'    | bonus |
|-------|-------|
| Rich  | 5     |
| Some  | 0     |
| Broke | -8    |

### Termination 
After the feedback and additional analysis it was decide to move from decades to years, to make the episodes jumps smaller. Therefore the model terminates after 90 steps (90 years).

### Parameters
- START_STATE: The person starts in randomly selected state. (Imitation of real life). Since the probability to get born in wealthy family is low, the chance distributions are: Rich - 0.1, Some - 0.6, Broke - 0.3. 
- y = 0.9: If y is closer to 1, the agent thinks long-term and is focused to work or invest now to be rich later. If y is closer to 0, the agent only cares about right now and will just spend. I picked 0.9 as something in between, because in real life people want to climb up in society but also want to enjoy their life while they are doing it.