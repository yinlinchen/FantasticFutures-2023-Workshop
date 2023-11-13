from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from SPARQLWrapper import SPARQLWrapper, JSON
import openai
import gradio as gr


llm = ChatOpenAI(temperature=0.1, model='gpt-4')


def generate_sparql_query(message):
    template = """generate a sparql query to dbpedia without explaination for {user_question}"""

    prompt = PromptTemplate(template=template, input_variables=["message"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    response = llm_chain.run(message)

    return response


def perform_sparql_query(sparql_query):
    sparql = SPARQLWrapper("http://dbpedia.org/sparql")
    sparql.setQuery(sparql_query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()


def create_natural_language_query(results, user_question):
    key_value_pairs = [f"{key}: {value['value']}" for item in results['results']
                       ['bindings'] for key, value in item.items()]
    return f"The information for your query '{user_question}' is as follows: {'; '.join(key_value_pairs)}."


def generate_natural_language_response(natural_language_query):

    template = """{user_question} and the responses should be in the same language as the question."""

    prompt = PromptTemplate(template=template, input_variables=["message"])
    llm_chain = LLMChain(prompt=prompt, llm=llm)
    response = llm_chain.run(natural_language_query)

    return response


def predict(message, history):
    history_langchain_format = []
    for human, ai in history:
        history_langchain_format.append(HumanMessage(content=human))
        history_langchain_format.append(AIMessage(content=ai))
    history_langchain_format.append(HumanMessage(content=message))

    print(history_langchain_format)

    sparql_query = generate_sparql_query(message)
    print(sparql_query)

    results = perform_sparql_query(sparql_query)
    print(results)

    natural_language_query = create_natural_language_query(results, message)
    print(natural_language_query)

    natural_language_response = generate_natural_language_response(
        natural_language_query)
    print(natural_language_response)

    return natural_language_response


gr.ChatInterface(predict).launch()
