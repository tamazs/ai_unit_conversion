from langchain.tools import BaseTool

class FahrenheitToCelsiusTool(BaseTool):
    name: str = "FahrenheitToCelsius"
    description: str = ("Useful when the user asks to convert Fahrenheit to Celsius. "
                   "Input should be the number you want to convert to Celsius.")

    def _run(self, number: float) -> float:
        number = float(number)
        return (number - 32) / (9/5)

    async def _arun(self, number: float) -> float:
        number = float(number)
        return (number - 32) / (9/5)
