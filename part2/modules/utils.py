def print_section_separator(msg: str):
  seperator = "=" * int((80 - len(msg))/ 2 - 1)
  print(f"{seperator} {msg} {seperator}")