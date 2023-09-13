# 1달 28일
def month_to_day(termdue): # termdue -> month
    day = int(termdue)*28
    return day

def ymd_to_day(ymd):
    y = ymd.split('.')[0]
    m = ymd.split('.')[1]
    d = ymd.split('.')[2]
    
    y_day = int(y)*12*28
    m_day = int(m)*28
    print(m, m_day)
    day = int(d)
    
    totalday = y_day + m_day + day
    
    return totalday

def due_or_not(totalday_today, totalday_due):
    save = False
    
    if totalday_today >= totalday_due:
        save = True
        return save
    
    else:
        return save

def solution(today, terms, privacies):
    answer = []
    
    # about today 
    totalday_today = ymd_to_day(today)
        
    # about term
    dict_term = {}
    for term in terms:
        termkind = term.split(' ')[0]
        termdue = term.split(' ')[1]
        
        dict_term[termkind] = month_to_day(termdue) # ex) {A : 28, B : 56}
        
    # about privacies
    for idx, privacy in enumerate(privacies):
        date_privacy = privacy.split(' ')[0] # type : ymd
        termkind_prv = privacy.split(' ')[1] # ex) A, B
        
        totalday_privacy = ymd_to_day(date_privacy)
        totalday_term = dict_term[termkind_prv]
        
        # cal due date
        totalday_due = totalday_privacy + totalday_term 
        if due_or_not(totalday_today, totalday_due):
            answer.append(idx+1)       
    
    return answer


# print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))