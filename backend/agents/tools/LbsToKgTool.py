from langchain.tools import BaseTool

class LbsToKgTool(BaseTool):
    name: str = "LbsToKg"
    description: str = ("Useful when the user asks to convert Lbs to Kilograms. "
                   "Input should be the number you want to convert to kilograms.")

    def _run(self, number: float) -> float:
        number = float(number)
        return number / 2.20462

    async def _arun(self, number: float) -> float:
        number = float(number)
        return number / 2.20462
