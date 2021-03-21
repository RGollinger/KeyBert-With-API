#%%
from keybert import KeyBERT
doc = """
         Supervised learning is the machine learning task of learning a function that
         maps an input to an output based on example input-output pairs.[1] It infers a
         function from labeled training data consisting of a set of training examples.[2]
         In supervised learning, each example is a pair consisting of an input object
         (typically a vector) and a desired output value (also called the supervisory signal). 
         A supervised learning algorithm analyzes the training data and produces an inferred function, 
         which can be used for mapping new examples. An optimal scenario will allow for the 
         algorithm to correctly determine the class labels for unseen instances. This requires 
         the learning algorithm to generalize from the training data to unseen situations in a 
         'reasonable' way (see inductive bias).
      """

doc2 = "RT @econnaturalist: Holiday gatherings, the COVID-19 surge, and the sunk cost fallacy: Why you should cancel your Thanksgiving travel plans\u2026"

doc3 = "Mandryk: Moe's resistance to a lockdown defines COVID-19 response What's driven this is a call to action by doctors. Why it didn't go further is Moe drew a line ... and then business interests stood him."

model = KeyBERT('distilbert-base-nli-mean-tokens')
keywords = model.extract_keywords(doc3)
print(keywords) 

#%%