from langchain.tools import BaseTool

class KmhToMihTool(BaseTool):
    name: str = "KmhToMih"
    description: str = ("Useful when the user asks to convert Kilometers per hour to Miles per hour. "
                   "Input should be the number you want to convert to Miles per hour.")

    def _run(self, number: float) -> float:
        number = float(number)
        return number / 1.609344

    async def _arun(self, number: float) -> float:
        number = float(number)
        return number / 1.609344
