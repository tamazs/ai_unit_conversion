from langchain.tools import BaseTool

class MihToKmhTool(BaseTool):
    name: str = "MihToKmh"
    description: str = ("Useful when the user asks to convert Miles per hour to Kilometers per hour. "
                   "Input should be the number you want to convert to Kilometers per hour.")

    def _run(self, number: float) -> float:
        number = float(number)
        return number * 1.609344

    async def _arun(self, number: float) -> float:
        number = float(number)
        return number * 1.609344
