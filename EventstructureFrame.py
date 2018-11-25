########################################################################################################################
# EventStructureFrame.py v.1                                                                                           #
# Date: 2018. 11. 24                                                                                                   #
# Developed by Seohyun Im                                                                                              #
# input: Event Structure Type (event structure-based verb class)                                                       #
# output: Event Structure Frame (structured subevents with predicate + arguments which is annotated as semantic roles) #
######################################################################################################################## 

"""
In this version, Event Structure Frame does not consider intransitive-transiive alternation.
For example, it gives the same event Structure Frame for the verbs in the two sentences below:
   (1) I broke the window.
   (2) The window broke.  
Basically, the Event Structure Frame is for intransitive forms. You need to add agent argument for transitive forms if you need one.
"""
"""
variables: ving, ved, prep, semantic roles 
           ving: the progressive form of the target verb lemma 
           ved: the pastpart form of the target verb lemma
           prep: preposition
           semantic roles = [agent, theme, source, goal, location, possessor, beneficiary, event, state]
"""

def state_ESF(est):
   state = {}
   ving = None
   theme = None
   state['state'] = ving+'('+theme+')'
   return state

def process_ESF(est):
   process = {}
   ving = None
   agent = None
   theme = None
   process['process'] = ving+'('+agent+')'
   return process

def motion_ESF(est):
   motion = {}
   ving = None
   agent = None
   theme = None
   source = 'SOURCE_LOCATION'
   goal = 'GOAL_LOCATION'
   prep = 'AT'
   motion['assumed_pre-state'] = 'BE_'+prep+'('+agent+', '+source+')'
   motion['process'] = ving+'('+agent+')'
   motion['assumed_post-state'] = 'BE_'+prep+'('+agent+', '+goal+')'
   return motion

def leave_ESF(est):
   leave = {}
   ving = None
   agent = None
   source = 'SOURCE'
   prep = 'AT'
   leave['pre-state'] = 'BE_'+prep+'('+agent+', '+source+')'
   leave['process'] = ving+'('+agent+')'
   leave['post-state'] = 'NOT_BE_'+prep+'('+agent+', '+source+')'
   return leave

def arrive_ESF(est):
   arrive = {}
   ving = None
   agent = None
   theme = None
   goal = 'GOAL'
   prep = 'AT'
   leave['pre-state'] = 'NOT_BE_'+prep+'('+agent+', '+goal+')'
   leave['process'] = ving+'('+agent+')'
   leave['post-state'] = 'BE_'+prep+'('+agent+', '+goal+')'
   return arrive

def transfer_ESF(est):
   transfer = {}
   ving = None
   agent = None
   source = 'SOURCE'
   goal = 'GOAL'
   prep = 'AT'
   transfer['pre-state1'] = 'BE_'+prep+'('+agent+', '+source+')'
   transfer['pre-state2'] = 'NOT_BE_'+prep+'('+agent+', '+goal+')'
   transfer['process'] = ving+'('+agent+')'
   transfer['post-state1'] = 'BE_'+prep+'('+agent+', '+goal+')'
   transfer['post-state2'] = 'NOT_BE_'+prep+'('+agent+', '+source+')'
   return transfer

def pass_ESF(est):
   pas = {}
   ving = None
   agent = None
   source = 'SOURCE'
   goal = 'GOAL'
   location = 'PASSING_LOCATION'
   prep = 'AT'
   pas['pre-state'] = 'BE_'+prep+'('+agent+', '+source+')'
   pas['process'] = ving+'('+agent+')'
   pas['state'] = 'BE_'+prep+'('+agent+', '+location+')'
   pas['post-state'] = 'BE_'+prep+'('+agent+', '+goal+')'
   return pas

def lose_ESF(est):
   lose = {}
   ving = None
   possessor = None
   theme = None
   lose['pre-state'] = 'HAVE'+'('+possessor+', '+theme+')'
   lose['process'] = ving+'('+possessor+', '+theme+')'
   lose['post-state'] = 'NOT_HAVE'+'('+possessor+', '+theme+')'
   return lose

def get_ESF(est):
   get = {}
   ving = None
   recipient = None
   theme = None
   get['pre-state'] = 'NOT_HAVE'+'('+recipient+', '+theme+')'
   get['process'] = ving+'('+recipient+', '+theme+')'
   get['post-state'] = 'HAVE'+'('+recipient+', '+theme+')'
   return get

def give_ESF(est):
   give = {}
   ving = None
   possessor = None
   recipient = None
   theme = None
   give['pre-state1'] = 'HAVE'+'('+possessor+', '+theme+')'
   give['pre-state2'] = 'NOT_HAVE'+'('+recipient+', '+theme+')'
   give['process'] = ving+'('+possessor+', '+recipient+', '+theme+')'
   give['post-state1'] = 'HAVE'+'('+recipient+', '+theme+')'
   give['post-state2'] = 'NOT_HAVE'+'('+possessor+', '+theme+')'
   return give

def come_into_existence_ESF(est):
   comeex = {}
   ving = None
   theme = None
   comeex['pre-state1'] = 'NOT_BE'+ved+'('+theme+')'
   comeex['pre-state2'] = 'THERE_BE_NOT'+'('+theme+')'
   comeex['process'] = ving+'('+theme+')'
   comeex['post-state1'] = 'BE'+ved+'('+theme+')'
   comeex['post-state2'] = 'THERE_BE'+'('+theme+')'
   return comeex

def go_out_of_existence_ESF(est):
   goex = {}
   ving = None
   theme = None
   goex['pre-state1'] = 'NOT_BE'+ved+'('+theme+')'
   goex['pre-state2'] = 'THERE_BE'+'('+theme+')'
   goex['process'] = ving+'('+theme+')'
   goex['post-state1'] = 'BE'+ved+'('+theme+')'
   goex['post-state2'] = 'THERE_BE_NOT'+'('+theme+')'
   return goex

def become_ESF(est):
   become = {}
   ving = None
   theme = None
   state = None
   become['pre-state1'] = 'NOT_BE'+ved+'('+theme+', '+state+')'
   become['pre-state2'] = 'NOT_BE'+'('+theme+', '+state+')'
   become['process'] = ving+'('+theme+', '+state+')'
   become['post-state1'] = 'BE'+ved+'('+theme+', '+state+')'
   become['post-state2'] = 'BE'+'('+theme+', '+state+')'
   return become

def positive_causation(est):
   poscau = {}
   ving = None
   causer = None
   event = None
   poscau['process1'] = ving+'('+causer+', '+event+')'
   poscau['process2'] = 'HAPPEN('+event+')'
   return poscau

def negative_causation(est):
   negcau = {}
   ving = None
   causer = None
   event = None
   negcau['process1'] = ving+'('+causer+', '+event+')'
   negcau['process2'] = 'NOT_HAPPEN('+event+')'
   return negcau

def begin_ESF(est):
   begin = {}
   ving = None
   event = None
   begin['pre-state'] = 'NOT_IN_PROGRESS('+event+')'
   begin['process'] = ving+'('+event+')'
   begin['post-state'] = 'IN_PROGRESS('+event+')'
   return begin

def continue_ESF(est):
   continu = {}
   ving = None
   event = None
   continu['pre-state'] = 'IN_PROGRESS('+event+')'
   continu['process'] = ving+'('+event+')'
   continu['post-state'] = 'IN_PROGRESS('+event+')'
   return continu

def end_ESF(est):
   end = {}
   ving = None
   event = None
   end['pre-state'] = 'IN_PROGRESS('+event+')'
   end['process'] = ving+'('+event+')'
   end['post-state'] = 'NOT_IN_PROGRESS('+event+')'
   return end

def cos_leave_ESF(est):
   cosleave = {}
   ving = None
   theme = None
   source = 'SOURCE'
   prep = 'AT'
   cosleave['pre-state'] = 'BE_'+prep+'_('+theme+', '+source+')'
   cosleave['process'] = ving+'('+theme+')'
   cosleave['post-state'] = 'NOT_BE_'+prep+'_('+theme+', '+source+')'
   return cosleave

def cos_arrive_ESF(est):
   cosarrive = {}
   ving = None
   theme = None
   goal = 'GOAL'
   prep = 'AT'
   cosarrive['pre-state'] = 'NOT_BE_'+prep+'_('+theme+', '+goal+')'
   cosarrive['process'] = ving+'('+theme+')'
   cosarrive['post-state'] = 'BE_'+prep+'_('+theme+', '+goal+')'
   return cosarrive

def cos_transfer_EFS(est):
   costrans = {}
   ving = None
   theme = None
   source = 'SOURCE'
   goal = 'GOAL'
   prep = 'AT'
   costrans['pre-state1'] = 'BE_'+prep+'('+theme+', '+source+')'
   costrans['pre-state2'] = 'NOT_BE_'+prep+'('+theme+', '+goal+')'
   costrans['process'] = ving+'('+theme+')'
   costrans['post-state1'] = 'BE_'+prep+'('+theme+', '+goal+')'
   costrans['post-state2'] = 'NOT_BE_'+prep+'('+theme+', '+source+')'
   return costrans

def scalar_change_ESF(est):
   scalar = {}
   ved = None
   ving = None
   theme = None
   source_state = 'SOURCE_STATE'
   goal_state = 'GOAL_STATE'
   scalar['pre-state1'] = 'NOT_BE'+ved+'('+theme+')'
   scalar['pre-state2'] = 'BE'+'('+theme+', '+source_state+')'
   scalar['process'] = ving+'('+theme+')'
   scalar['post-state1'] = 'BE'+ved+'('+theme+')'
   scalar['post-state2'] = 'BE'+'('+theme+', '+goal_state+')'
   return scalar

def change_state_ESF(est):
   changestate = {}
   ved = None
   ving = None
   theme = None
   changestate['pre-state'] = 'NOT_BE '+ved+'('+theme+')'
   changestate['process'] = ving+'('+theme+')'
   changestate['post-state'] = 'BE '+ved+'('+theme+')'
   return changestate


def esfAssign(est):
   esframe = None
   if est =='STATE':
      esframe = state_ESF(est)
   elif est =='PROCESS':
      esframe = process_ESF(est)
   elif est =='MOTION':
      esframe = motion_ESF(est)
   elif est =='LEAVE':
      esframe = leave_ESF(est)
   elif est =='ARRIVE':
      esframe = arrive_ESF(est)  
   elif est =='TRANSFER':
      esframe = transfer_ESF(est)
   elif est =='PASS':
      esframe = pass_ESF(est)
   elif est =='LOSE':
      esframe = lose_ESF(est)
   elif est =='GET':
      esframe = get_ESF(est)
   elif est =='GIVE':
      esframe = give_ESF(est)
   elif est =='COME_INTO_EXISTENCE':
      esframe = come_into_existence_ESF(est)
   elif est =='GO_OUT_OF_EXISTENCE':
      esframe = go_out_of_existence_ESF(est)
   elif est =='BECOME':
      esframe = become_ESF(est)
   elif est =='POSITIVE_CAUSATION':
      esframe = positive_causation(est)
   elif est =='NEGATIVE_CAUSATION':
      esframe = negative_causation(est)
   elif est =='BEGIN':
      esframe = begin_ESF(est)
   elif est =='CONTINUE':
      esframe = continue_ESF(est)
   elif est =='END':
      esframe = end_ESF(est)
   elif est =='COS_LEAVE':
      esframe = cos_leave_ESF(est)
   elif est =='COS_ARRIVE':
      esframe = cos_arrive_ESF(est)
   elif est =='COS_TRANSFER':
      esframe = cos_transfer_EFS(est)
   elif est =='SCALAR_CHANGE':
      esframe = scalar_change_ESF(est)
   else:
      esframe = change_state_ESF(est)
   return esframe

