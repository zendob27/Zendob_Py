if __name__ == '__main__':
    f=open('students',encoding='utf-8')
    lines=f.readlines()
    answers={}
    for line in lines:
        temp_list=line.strip().split('\t')
        
        xueyuan=temp_list[2]
        if xueyuan in answers.keys():
            answers[xueyuan]+=1
        else:
            answers[xueyuan]=1

    for p in answers:
        print(answers[p],p)