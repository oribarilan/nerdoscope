# nerdoscope

A horoscope app for nerds in the tech industry.

## Background

This is a simple demo project aimed at helping with basic first steps in settings up a generative AI based app.

## Recommended Setup

1. Install [Docker](https://www.docker.com/products/docker-desktop)
2. Install [Visual Studio Code](https://code.visualstudio.com/)
3. Install the [Remote Development extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
4. Reopen the project in a dev container (CMD + Shift + P -> Reopen in Container)
5. Inside the dev container, run `ollama serve`
6. Open another terminal and download the model `ollama pull orca-mini:3b`

## Instructions

### Play Around

First, play around with a model that is available to you (some playground are listed below). 
For example, you can use [Hugging Face Model Repository](https://huggingface.co/models) to interact with many models, and pick one that seems promising for your use case.

For ease of use working with these demos, we suggest that you pick a model that is available in the [Ollama model repository](https://ollama.com/library).

Don't worry, you can always change this later :)

### Jupyter Notebook

Now, enter the dev container and open the Jupyter Notebook at `src/demo.ipynb`.
Follow along with the notebook to see how to use the model in your app.

### Code your CLI

TBD

## Useful Links

### Models and Playgrounds
1. [Azure OpenAI Studio](https://oai.azure.com/)
2. [Hugging Face](https://huggingface.co/)
3. [Ollama](https://ollama.com/)

### Libraries (and coding tutorials)
1. [Azure OpenAI Quickstarts](https://learn.microsoft.com/en-us/azure/ai-services/openai/)
2. [Semantic Kernel](https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide?tabs=python)
3. [LangChain](https://python.langchain.com/docs/get_started/quickstart)

### Prompt Engineering
1. [Prompt Engineering Guide](https://www.promptingguide.ai/)
