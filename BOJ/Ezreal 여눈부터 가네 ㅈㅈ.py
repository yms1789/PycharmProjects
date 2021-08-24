# 어떤 수 x(x는 15의 배수) 앞에는 1 or 5만 올 수 있음. 10^n 은 15로 나눈 나머지가 10,  5*(10^n) 는 15로 나눈 나머지가 5
# 나머지 경우의 수 = 0 or 5 or 10 앞에 5가 온다면 x는 나머지가 10이 되도록하면 됨 앞에 1이 온다면 x는 나머지가 5가 되게 해야 함.
import sys
input = sys.stdin.readline

N = int(input())
dp = [[0 for i in range(3)] for i in range(1516)]
# 한자리 일 땐 5만 존재
dp[1][1] = 1
# 두자리 일 땐 15, 55 두 개 존재
dp[2][0] = 1
dp[2][2] = 1

for i in range(3, 1516):
    dp[i][0] = dp[i - 1][1] + dp[i - 1][2]  # 현 시점 자리수에서 나머지가 0인 수 = 이전 자리에서 나머지 5 or 나머지 10
    dp[i][1] = dp[i - 1][0] + dp[i - 1][2]  # 나머지가 5인 수 = 이전 자리에서 나머지가 0인수 + 이전자리에서 나머지가 10인수
    dp[i][2] = dp[i - 1][0] + dp[i - 1][1]  # 나머지가 10인 수 = 이전 자리에서 나머지가 0인수 + 이전자리에서 나머지가 5인 수
    for j in range(3):
        dp[i][j] %= 1000000007

print(dp[N][0]) #나머지가 해당 자리 수에서 0인 값 출력
