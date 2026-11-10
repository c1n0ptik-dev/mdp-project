# MDP project: personal finance

The idea comes from personal finance in everyday life: every month you decide whether to work, spend or invest, and that choice affects how much money you have next month.

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

| s     | a      | p(Rich) | p(Some) | p(Broke) |
|-------|--------|---------|---------|----------|
| Rich  | Invest | 0.6     | 0.2     | 0.2      |
| Rich  | Spend  | 0.5     | 0.4     | 0.1      |
| Rich  | Work   | 1       | 0       | 0        |
| Some  | Invest | 0.2     | 0.3     | 0.5      |
| Some  | Spend  | 0       | 0.5     | 0.5      |
| Some  | Work   | 0.4     | 0.6     | 0        |
| Broke | Work   | 0       | 0.7     | 0.3      |

### Rewards r(s, a)

| s \ a | Invest | Spend | Work |
|-------|--------|-------|------|
| Rich  | 5      | 10    | -2   |
| Some  | 3      | 8     | -2   |
| Broke | -      | -     | -1   |

#### State bonus bonus(s')

| s'    | bonus |
|-------|-------|
| Rich  | 5     |
| Some  | 0     |
| Broke | -5    |

### Termination
Each step represents 10 years of a person's life. Assuming a lifetime of 90 years, an episode has 9 steps, so T is 9. After the 9th step the episode ends. 

### Parameters
- START_STATE: The person starts in randomy selected state. (Imitation of real life) 
- y: I chose this because money in the next few decades matters more to a person than money at the very end of life. If y is closer to 1, the agent thinks long-term and is focused to work or invest now to be rich later. If y is closer to 0, the agent only cares about right now and will just spend. I picked 0.6 as something in between, because in real life people want to climp up in society but also want to enjoy their life while they are doing it.