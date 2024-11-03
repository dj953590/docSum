from rag.agents.doc_agents import doc_agents
from rag.tools.tools import create_tools
from rag.db.ingest import create_DB
from edgar.downloader import download
from constants import ROOT_DIRECTORY
from ingest.queries import Queries

import sys

# Initialize environment and tools
from dotenv import load_dotenv

load_dotenv()

agents = {}


class SessionState:
    def __init__(self):
        self.data = {}

    def __getattr__(self, item):
        return self.data.get(item)

    def __setattr__(self, key, value):
        if key == "data":
            super().__setattr__(key, value)
        else:
            self.data[key] = value


class FileOutput:
    def __init__(self, symbol):
        self.symbol = symbol

    def write(self, content):
        with open(f"{self.symbol}_output.txt", "a") as file:
            file.write(content + "\n")


def load_tools(symbol):
    if symbol not in agents:  # Load agent if not already loaded
        tools = create_tools(symbol)
        agents[symbol] = doc_agents(tools)
    return agents[symbol]


def run_agent_query(agent, query):
    return agent.invoke(query)


def main():
    source_directory = f"{ROOT_DIRECTORY}//ingest//"
    with open(source_directory + "symbols.txt", "r") as file:
        symbols = file.read().splitlines()

    for symbol in symbols:
        queries = Queries(symbol)
        # Load data
        if symbol not in agents:
            download(symbol)
            create_DB(symbol)
            agent = load_tools(symbol)
            responses = {}
            output = FileOutput(symbol)  # Create an instance of FileOutput
            # Run queries and store responses
            for key, query in queries.queries.items():
                response = run_agent_query(agent, query)
                responses[key] = response

            # Display insights from the agent
            for key, response in responses.items():
                output.write(f"Analysis for **{key}** from recent 10-K filing of **{symbol}**:")
                output.write(response['output'])


if __name__ == "__main__":
    main()
