from rasa_nlu.training_data import load_data
from rasa_nlu.model import Trainer
from rasa_nlu import config
import en_core_web_sm

nlp = en_core_web_sm.load()
from rasa_nlu.model import Metadata, Interpreter

train_data = load_data('rasa_dataset.json')
trainer = Trainer(config.load("config_spacy.yaml"))

trainer.train(train_data)
model_directory = trainer.persist('/projects/')
#singhsiddharth.1998@gmail.com
# import spacy
# import en_core_web_sm

# nlp = en_core_web_sm.load()
# docx = nlp(u"Northern Indian restaurants")
# for word in docx.ents:
#     print("value", word.text, "entity", word.label_, "start", word.start_char, "end", word.end_char)
# for word1 in docx.ents:
#     print(word1.label_)
for i in range(5):
    eg = input("")
    interpreter = Interpreter.load(model_directory)
    intent = interpreter.parse(eg)
    print(intent)
    string = (intent['intent']['name'])
    print(string)
    ex = nlp(eg)
    for x in ex.ents:
        y=str(x)
        print(x, x.label_)
    if string == "restaurant_search" and x.label_ == "GPE":
            print("The restaurants in "+y+" are:")
        
    if string == "restaurant_search" and x.label_ == "TIME":
        print("The restaurants available at "+y+" are:")
        res=input("")
        intent = interpreter.parse(res)
        string2 = (intent['intent']['name'])
        if string2 == "affirm":
            print("Would you like to book one of the above")
    if string == "greet":
        print("Hi, How are you?")
    if string == "affirm":
        print("Okay")
    if string == "goodbye":
        print("Thank you")