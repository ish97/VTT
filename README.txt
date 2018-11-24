# VTT
(1) Verbs_with_concreteness_ratings
English verbs with concreteness ratings and verbnet class information for VTT project
The 6903 verbs are listed as a csv file. 
Each verb includes (lemma, verbnet_verb, verbnet_verb_class, verb_token, concreteness_rating, frequency)
verbnet_verb and verbnet_verb_class are from verbnet.
verb_token, concreteness_rating, and frequency are from Brysbaert et. al. (2014)
We made this list of verbs with concreteness ratings for vision-word mapping task and psycholinguistic study.
We are going to add more English verbs and finally construct a lexicon by adding various lexical semantic information.

(2) 300 English Verbs with WordNet Synsets and Event Structure-based verb classes
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
