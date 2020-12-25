#lex_auth_012693816757551104165

def max_visited_speciality(patient_medical_speciality_list,medical_speciality):

    speciality = ''
    res = {}
    i =0
    for i in range(0, len(patient_medical_speciality_list)):
        if i % 2 != 0 :
            res[patient_medical_speciality_list[i]] = res.get(patient_medical_speciality_list[i],0) + 1
        i +=1
        
    mx_count = 0
    mx_name =''
    
    for i, j in res.items():
        if j > mx_count :
            mx_count = j
            mx_name = i
    
    speciality = medical_speciality[mx_name] 

    return speciality

#provide different values in the list and test your program
patient_medical_speciality_list=[301,'P',302, 'P' ,305, 'P' ,401, 'E' ,656, 'E']
medical_speciality={"P":"Pediatrics","O":"Orthopedics","E":"ENT"}
speciality=max_visited_speciality(patient_medical_speciality_list,medical_speciality)
print(speciality)
