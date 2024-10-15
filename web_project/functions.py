def get_todo(filePath="todos.txt") -> list:
  """Read a text file and return the list of ToDo items"""
  
  with open(filePath, "r") as file_R:
      todos = file_R.readlines()
  
  return todos

def write_todo(todos_arg, filePath="todos.txt") -> None:
  with open(filePath, "w") as file_W:
      file_W.writelines(todos_arg)