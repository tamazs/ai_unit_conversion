from langchain.tools import BaseTool

class CelsiusToFahrenheitTool(BaseTool):
    name: str = "CelsiusToFahrenheit"
    description: str = ("Useful when the user asks to convert Celsius to Fahrenheit. "
                   "Input should be the number you want to convert to Fahrenheit.")

    def _run(self, number: float) -> float:
        number = float(number)
        return (number * 9/5) + 32

    async def _arun(self, number: float) -> float:
        number = float(number)
        return (number * 9/5) + 32
