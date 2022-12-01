
class Computerender:

  api_key: str

  def __init__(self, api_key=None):
    if (api_key == None):
        self.api_key = "bad"
    else:
        self.api_key = api_key

  def do_it(self):
    print("oh baby a triple")
