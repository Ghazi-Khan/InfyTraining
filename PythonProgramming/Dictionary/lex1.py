#lex_auth_012693774187716608134

'''
Author  : Ghazi Khan
problem : https://lex.infosysapps.com/en/viewer/hands-on/lex_auth_012693774187716608134?collectionId=lex_auth_0125409616243425281061&collectionType=Course
'''
def translate(bilingual_dict,english_words_list):
    #Write your logic here
    swedish_words_list = []
    for item in english_words_list:
        swedish_words_list.append(bilingual_dict[item])
        
    return swedish_words_list


bilingual_dict= {"merry":"god", "christmas":"jul", "and":"och", "happy":"gott", "new":"nytt", "year":"ar"}
english_words_list=["merry","christmas"]
print("The bilingual dict is:",bilingual_dict)
print("The english words are:",english_words_list)

swedish_words_list=translate(bilingual_dict, english_words_list)
print("The equivalent swedish words are:",swedish_words_list)
