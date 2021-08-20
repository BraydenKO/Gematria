import pandas as pd


pd.set_option('display.max_rows', None)
pd.options.mode.chained_assignment = None

def calcgematria(word,verse):
  gematria = 0
  for letter in word:
    if letter == "א":
      gematria += 1
    elif letter == "ב":
      gematria += 2
    elif letter == "ג":
      gematria += 3
    elif letter == "ד":
      gematria += 4
    elif letter == "ה":
      gematria += 5
    elif letter == "ו":
      gematria += 6
    elif letter == "ז":
      gematria += 7
    elif letter == "ח":
      gematria += 8
    elif letter == "ט":
      gematria += 9
    elif letter == "י":
      gematria += 10
    elif letter == "כ" or letter == "ך":
      gematria += 20
    elif letter == "ל":
      gematria += 30
    elif letter == "מ" or letter == "ם":
      gematria += 40
    elif letter == "נ" or letter == "ן":
      gematria += 50
    elif letter == "ס":
      gematria += 60
    elif letter == "ע":
      gematria += 70
    elif letter == "פ" or letter == "ף":
      gematria += 80
    elif letter == "צ" or letter == "ץ":
      gematria += 90
    elif letter == "ק":
      gematria += 100
    elif letter == "ר":
      gematria += 200
    elif letter == "ש":
      gematria += 300
    elif letter == "ת":
      gematria += 400
    elif letter == '' or letter == ' ':
      gematria += 0
    else:
      raise Exception(f"'{letter}' not known - verse, word: {verse}, {word}")
  return gematria


def create_data():
  path = (r"Docs\Tanach\Torah.csv")
  df = pd.read_csv(path)
  df2 = pd.DataFrame()

  ncol = len(df.columns)
  nrow = len(df)

  data = df[list(df.columns)].values

  for row in range(nrow):
    verse = data[row][0]
    words = data[row][1].split(" ")
    for word in words:
      gematria = 0
      gematria = calcgematria(word, verse)

      new_row = [verse, word,gematria]
      new_rowdf = pd.DataFrame([new_row])
      df2 = pd.concat([new_rowdf, df2], ignore_index=True)

  df2 = df2[::-1]
  df2.to_csv(r"Docs\Gematria_Torah.csv", index = False)

def find_word():
  path = (r"Docs\Gematria_Torah.csv")
  df = pd.read_csv(path)
  search(df)

def search(df):
  input_gmtria = gematria_input()
  results = df.loc[df['2']== input_gmtria]
  results["1"] = results["1"].apply(lambda word: word[::-1])
  print(results)
  
  cont = input("Press Enter to continue or write quit to leave: ")
  if cont.lower() == "quit":
    quit()
  search(df)


def gematria_input():
  try:
    input_gmtria = int(input("Please enter a number: "))
  except ValueError:
    print("Please use a valid number")
    input_gmtria = gematria_input()
  return input_gmtria


find_word()