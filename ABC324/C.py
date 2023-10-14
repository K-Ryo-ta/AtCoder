N,T_dush = input().split()
N = int(N)
S = [input() for i in range(N)]
Aruphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
             "o","p","q","r","s","t","u","v","w","x","y","z"]
T_dush_aruphabet:str = ''
ans = []

for i in range(N):
    length = len(T_dush)
    if(S[i] == T_dush):
        ans.append(i)
    elif(S[i] in T_dush):
        ans.append(i)
    else:
        for j in range(length):
            if(T_dush[:j]+T_dush[j+1:] == S[i]):
                ans.append(i)
            else:
                for j in range(length):
                    for k in range(25):
                        if(T_dush.replace(T_dush[j], Aruphabet[k]) == S[i]):
                           ans.append(i)

print(ans)

