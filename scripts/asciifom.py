def create_ascii_art(text):
  """
  Create a simple ASCII art representation of the given text.
  This is a basic implementation and will create a minimalistic design.
  """
  # Splitting the text into words for individual processing
  words = text.split()

  # ASCII art representation
  ascii_art = ""
  for word in words:
    # Adding each word in ASCII style
    ascii_art += "".join(["#FF+" if char != " " else " " for char in word])
    ascii_art += "\n"

  return ascii_art

# Creating ASCII art for "Forensic Obfuscation Model"
ascii_art = create_ascii_art("Forensic Obfuscation Model")
print(ascii_art)
