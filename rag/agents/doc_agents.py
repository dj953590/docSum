import langchain
from langchain.agents import AgentType, initialize_agent
from langchain_community.llms.ollama import Ollama
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

'''
Using the langchain agents
'''


def doc_agents(tools):
    # Defining the llm to be used
    llm = ChatOpenAI(
        temperature=0,
        model="gpt-3.5-turbo-0125",
    )
    #llm = Ollama(base_url='http://localhost:11434', model="llama3:instruct")

    '''
    True: Run the program in debug mode
    False: Run the program in normal mode
    '''
    langchain.debug = True

    agent = initialize_agent(
        agent=AgentType.OPENAI_FUNCTIONS,
        tools=tools,
        llm=llm,
        verbose=False,
    )

    return agent
