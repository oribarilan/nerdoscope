from dataclasses import dataclass

import typer
from fliq import q
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from utils import stream_print

app = typer.Typer()

system_prompt = """
You are a horoscope bot for personnas in the software development industry.
Given a user's role, generate a personalized "nerdoscope" (horoscope for nerds) message for the week.
Guidelines for the message:
* The message should consists of a single paragraph, 5 sentences max.
* The message should be in the spirit of a horoscope (refer to it as nerdoscope), offering a blend of foresight and advice relevant to the user role, but in a humorous way.
* If possible, the foresight and/or advice should reference a popular tool or technology in the software development industry, relevant to the role.
* The tone should be fun and lighthearted.
* The message should be funny and sarcastic, and personalized to the role.
* The message should include technical jargon.
"""


@dataclass
class Role:
    key: str
    verbose: str


roles = [
    Role("dev", "👩‍💻 Software Developer"),
    Role("qa", "🔍 Quality Assurance Engineer"),
    Role("pm", "📈 Project Manager"),
    Role("design", "🎨 UI/UX Designer"),
    Role("devops", "🔧 DevOps Engineer"),
    Role("ds", "📊 Data Scientist"),
    Role("mngr", "👨‍💼 Manager"),
]


@app.command()
def nerdoscope(role: str):
    """Get your personalized nerdoscope!

    Args:
        role (str): role in the tech industry (use list_roles to see available roles)
    """
    selected_role = q(roles).single(lambda r: r.key == role, default=None)
    if selected_role is None:
        typer.echo(f"Invalid role. Please select from {role}")
        raise typer.Exit()

    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("user", "{role}")
    ])
    llm = Ollama(model="orca-mini:3b")
    chain = prompt | llm
    role = "🧑‍💻 Software Develpoer"
    stream_print(chain, {"role": selected_role.verbose})


@app.command()
def list_roles():
    for role in roles:
        max_key_length = q(roles).select(lambda r: len(r.key)).max()
        print(f"* {role.key.ljust(max_key_length)}\tfor\t{role.verbose}")


if __name__ == "__main__":
    app()
