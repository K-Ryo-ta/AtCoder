# 条件の標準入力
N,M,K = map(int,input().split())
    
# ビットマスクを生成している
ks = [0] * M
# 開くか開かないかのフラグを生成している
r = [0] * M

for i in range(M):
    k = 0
    data = list(input().split())

    # 鍵の本数の入力
    C = int(data[k])
    k += 1

    for j in range(C):
        
        # 鍵のビットマスクの入力
        a = int(data[k])

        # 鍵のビットマスクを生成している
        a -= 1
        ks[i] |= (1 << a)
        k += 1
    
# フラグの判定を行なっている
    if data[k] == 'o':
            r[i] = 1
    else:
        r[i] = 0
    k += 1

# 出力する答えを定義
res = 0

# ビット全探索を行なっている
for i in range(1 << N):
    jud = True
    for j in range(M):

        # ビット演算と論理積を用いて、条件を満たすかどうかを判定している
        ok = bin(i & ks[j]).count('1')

        # ここで矛盾をチェックしている
        if ok >= K and r[j] == 0:
            jud = False
            break
        if ok < K and r[j] == 1:
            jud = False
            break
    if jud:
        res += 1

# 答えを出力       
print(res)
