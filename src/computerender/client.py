from typing import Optional

class Computerender:

  api_key: str

  def __init__(self, api_key: str="bad") -> None:
    self.api_key = api_key

  def do_it(self) -> None:
    print("oh baby a triple")
