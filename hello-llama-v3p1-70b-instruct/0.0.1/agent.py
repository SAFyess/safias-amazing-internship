from nearai.agents.environment import Environment

def run(env: Environment):
    # HERE, we are creating a variable with a instruction
    prompt = {"role": "system", "content": "You are a friendly agent"}
    
    # HERE, env.completions CALLS the MODEL
    # in this particular example we are calling llama-3p2-1b-instruct
    # We are giving it the prompt from line 7, and env.list_messages() is
    # a function that returns all the messages from the chat we had so far
    # with the agent
    result = env.completion([prompt] + env.list_messages())

    # HERE, we send the reply from the model to the user
    env.add_reply(result)

run(env)

