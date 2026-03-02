from langchain_ollama import ChatOllama
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from agents.tools.CelsiusToFahrenheitTool import CelsiusToFahrenheitTool
from agents.tools.FahrenheitToCelsiusTool import FahrenheitToCelsiusTool
from agents.tools.KgToLbsTool import KgToLbsTool
from agents.tools.KmhToMihTool import KmhToMihTool
from agents.tools.LbsToKgTool import LbsToKgTool
from agents.tools.MihToKmhTool import MihToKmhTool


class ConversionAgent:
    def __init__(self, model: str = "mistral", temperature: float = 0.0):
        llm = ChatOllama(model=model, temperature=temperature)

        tools = [CelsiusToFahrenheitTool(), FahrenheitToCelsiusTool(), KgToLbsTool(), LbsToKgTool(), KmhToMihTool(), MihToKmhTool()]

        prompt = ChatPromptTemplate.from_messages([
            ("system", (
                "You are a unit conversion calculator. "
                "Always use a tool to perform the conversion. "
                "After receiving the tool result, respond with ONLY the numeric result. "
                "Do NOT generate additional questions or examples. "
                "Do NOT include any text before or after the number. "
                "Your entire response must be a single number. "
                "STOP after outputting the number."
            )),
            ("human", "{input}"),
            MessagesPlaceholder("agent_scratchpad"),
        ])

        agent = create_tool_calling_agent(
            llm=llm,
            tools=tools,
            prompt=prompt
            )

        self._executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

    def run(self, user_input: str) -> str:
        result = self._executor.invoke({"input": user_input})
        return result["output"]