


###########################################################################################################
#
#    student name : HAOTIAN ZHU 
#    id :1467741 
#    CCID: haotian1
#    
#    if you have any question, please contact haotian1@ualberta.ca
###########################################################################################################
# 
#
#  Plots: There are two plots submitted
#         the file "Epsilon-Greedy.pdf" shows case with alpha = 0.1, Q(a)=0, Epsilon = 0.1 
#         the file "Greedy.pdf" shows case with alpha = 0.1, Q(a) = 5, Epsilon = 0 
###########################################################################################################
#
# To Run The Code:    python2.7 bandit_exp.py
# To Get The Plot:    r -f plot.r 
#
# IMPORTANT: you may need change value of variable to set Q(a) and Epsilon in bandit_agent
#            the lines you may change already commended with "# you may need change it ...."
#
#            when you need try Epsilon-Greedy:
#                 1. OPEN bandit_agent.py 
#                 2. IN FUNCTION createTable() MAKE SURE THAT Q_a = 0
#                 3. IN FUNCTION agent_start(this_observation) MAKE SURE ran_un()<0.1
#
#            when you need try Greedy:
#                 1. OPEN bandit_agent.py
#                 2. IN FUNCTION createTable() MAKE SURE THAT Q_a = 5
#                 3. IN FUNCTION agent_start(this_observation) MAKE SURE ran_un()<0
#
##########################################################################################################

