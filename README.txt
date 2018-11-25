# VTT
(1) Verbs_with_concreteness_ratings
English verbs with concreteness ratings and verbnet class information for VTT project
The 6903 verbs are listed as a csv file. 
Each verb includes (lemma, verbnet_verb, verbnet_verb_class, verb_token, concreteness_rating, frequency)
verbnet_verb and verbnet_verb_class are from verbnet.
verb_token, concreteness_rating, and frequency are from Brysbaert et. al. (2014)
We made this list of verbs with concreteness ratings for vision-word mapping task and psycholinguistic study.
We are going to add more English verbs and finally construct a lexicon by adding various lexical semantic information.

(2) verbclass.csv (300 English Verbs with WordNet Synsets and Event Structure-based verb classes)
I annotated aspectual class, semantic class, and Event Structure Type for each WordNet Synset of 300 English verbs.
aspectual class: state, process, transition
semantic class: state, process, motion, COL(change-of-location), COP(change-of-possession), COS(change-of-state)
event structure type: state, process, motion, leave, arrive, pass, transfer, lose, get, give, change-state, scalar-change, begin, continue, end, positive-causation, negative-causation, come-into-existence, go-out-of-existence, cos-leave, cos-arrive, cos-transfer
Example >
#,verb,synset#,example-sentence,aspectual-class,semantic-class,event-structure-type
22,acquire,get.v.01,She got a lot of paintings from her uncle,transition,COP,GET
22,acquire,assume.v.03,His voice took on a sad tone,transition,COS,CHANGE_STATE
22,acquire,grow.v.08,He grew a beard,transition,COS,SCALAR_CHANGE
22,acquire,acquire.v.04,NONE,transition,COS,NONE
22,acquire,acquire.v.05,I acquired a passing knowledge of Chinese,transition,COS,CHANGE_STATE
22,acquire,learn.v.01,She learned dancing from her sister,transition,COS,CHANGE_STATE
22,acquire,develop.v.03,I acquired a strong aversion to television,transition,COS,CHANGE_STATE

(3) EventstructureFrame.py
This file includes the 23 kinds of event structure frames corresponding to the 23 event structure-based verb classes in verbclass.csv.

# How to use verbclass.csv and EventstructureFrame.py
If you have the mapping of video action to text (sentence or word) as an input, you can derive some word meaning-based inferences from the mapping by using verbclass.csv and EventstructureFrame.py via Word Sense Disambiguation.
   *You need NLTK (natural language processing tool with python).

1. Input: a textual sentence and a target verb which describes an action (or an event) in a video  
   Example) the target verb: 'acquire', sentence: 'She acquired a lot of paintings from her uncle.'
2. Word Sense Disambiguation(WSD): Disambiguate the target verb 'acquire' to one of the WordNet Synset by using the WSD code in NLTK.
3. If the WSD result of 'acquire' is 'get.v.01', the event structure-based verb class - Event Structure Type - of 'acquire' is GET in verbclass.csv, as shown above.
2. From EventstructureFrame.py, you get the event structure frame corresponding to the event structure type GET - "get_esf".
    get_ESF
    get['pre-state'] = NOT_HAVE(recipient, theme)
    get['process'] = ving(recipient, theme)
    get['post-state'] = HAVE(recipient, theme)
3. Assign the appropriate value to the variables - ving, recipient, theme - by parsing the sentence.    
   ving = 'acquiring', recipient = 'She', theme = 'a lot of paintings'
4. output = the event structure of the verb 'acquire' in the sentence 'She got a lot of paintings from her uncle.'
   get['pre-state'] = NOT_HAVE(She, a lot of paintings)
   get['process'] = acquiring(She, a lot of paintings)
   get['post-state'] = HAVE(She, a lot of paintings)
5. Usage of Event Structure : inference
   (1) You can derive some event structure-based inferences.
       Before she acquired a lot of paintings, 'She didn't have a lot of paintings'
       After she acquired a lot of paintings, 'She has a lot of paintings.'
6. Extending the event structure-based inferences by adding synonyms and hypernyms
   (1) add the synonyms of the target verb 'acquire' and 'have' in the event structure of 'acquire' by using WordNet
            <python code>
            from NLTK.corpus import wordnet as wn
            synsets = wn.synsets(verb, pos='v')
            for synset in synsets:
               synonym = synset.lemma_names
       When the synset is 'get.v.01', the output synonym is 'get'
       Therefore, we can infer that she "got" a lot of paintings from her uncle from the example sentence.
   (2) add the hypernyms of a target verb
            <python code>
            hypernyms = synset.hypernyms()
            for hyp in hypernyms:
               hyp.lemma_names()
       When you get hypernyms, you also can derive hypernym-based inferences.
       
       
       
