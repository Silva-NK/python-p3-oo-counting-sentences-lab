#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self._value = ""
    self.value = value


  @property
  def value(self):
    return self._value 


  @value.setter
  def value(self, value):
    if not isinstance (value, str):
      print("The value must be a string.")
    else:
      self._value = value


  def is_sentence(self):
    if self.value.endswith("."):
      return True
    else:
      return False
    
  
  def is_question(self):
    if self.value.endswith("?"):
      return True
    else:
      return False
  

  def is_exclamation(self):
    if self.value.endswith("!"):
      return True
    else:
      return False
  

  def count_sentences(self):
    replaced = self.value.replace("!", ".").replace("?", ".")
    sentences = [s for s in replaced.split(".") if s.strip()]
    return len(sentences)
  


strings = MyString("This is a string! It has three sentences. Right?")
print(strings.is_sentence())
print(strings.is_question())
print(strings.is_exclamation())
print(strings.count_sentences())