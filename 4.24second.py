if __name__ == '__main__':
    f=open('students',encoding='utf-8')
    lines=f.readlines()
    answer={}
    for line in lines:
        temp_list=line.strip().split('\t')
        sex=temp_list[1]
        xueyuan=temp_list[2]
        if xueyuan not in answer:
            answer[xueyuan]=[0,0]
            if sex=='男':
                answer[xueyuan][0]=1
            else:
                answer[xueyuan][1]=1
        else:
            if sex=='男':
                answer[xueyuan][0]+=1
            else:
                answer[xueyuan][1]+=1

    for each_xueyuan in answer:
        sex_arr=answer[each_xueyuan]
        boy=sex_arr[0]
        girl=sex_arr[1]
        print(each_xueyuan,'\t\t\t',1,':',boy/girl)            