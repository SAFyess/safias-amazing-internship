from nearai.agents.environment import Environment

tanjer = """
Info on tanjer
"""

marrakesh = """
Info on marrakesh
"""

rabat = """
info on rabat
"""


def run(env: Environment):
    prompt = {"role": "system", "content": "You are a traveling agent helping people planning trips"}

    turistic_information = [
        {"role": "information", "content": tanjer},
        {"role": "information", "content": marrakesh},
        {"role": "information", "content": rabat},
    ]

    result = env.completion(
        [prompt] +
        turistic_information +
        env.list_messages()
    )
    env.add_reply(result)

run(env)
