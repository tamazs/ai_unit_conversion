from langchain.tools import BaseTool

class KgToLbsTool(BaseTool):
    name: str = "KgsToLbs"
    description: str = ("Useful when the user asks to convert kilograms to Lbs. "
                   "Input should be the number you want to convert to lbs.")

    def _run(self, number: float) -> float:
        number = float(number)
        return number * 2.20462

    async def _arun(self, number: float) -> float:
        number = float(number)
        return number * 2.20462
