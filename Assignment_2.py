
import PyDictionary
from PyDictionary import PyDictionary    #Importing the libraries
  
  
  
class DT:
    def Dictionary(self):
        #speak = Speaking()
        dic = PyDictionary()

        print("word?")                  #Enter the word
        query = str(input())
        word = dic.meaning(query)
        #print(len(word))
          
        for state in word:
            print(word[state])          #Meaning is printed
    
if __name__ == '__main__':
    DT()
    DT.Dictionary(self=None)