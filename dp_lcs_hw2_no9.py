def lcs(X, Y):
    """
    計算兩個序列的最長公共子序列(LCS)
    
    參數:
        X: 第一個序列
        Y: 第二個序列
        
    返回:
        LCS的長度和LCS本身
    """
    # 獲取序列長度
    m = len(X)
    n = len(Y)
    
    # 創建DP表格，初始值為0
    L = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    # 填充DP表格
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    # 回溯找出LCS
    lcs_result = []
    i, j = m, n
    
    while i > 0 and j > 0:
        # 如果當前字符相同，加入LCS
        if X[i-1] == Y[j-1]:
            lcs_result.append(X[i-1])
            i -= 1
            j -= 1
        # 否則，移動到較大的方向
        elif L[i-1][j] > L[i][j-1]:
            i -= 1
        else:
            j -= 1
    
    # 因為是從後往前回溯，需要反轉結果
    lcs_result.reverse()
    
    return L[m][n], lcs_result

# 視覺化DP表格的函數(可選)
def print_dp_table(X, Y):
    """打印DP表格以可視化LCS的計算過程"""
    m, n = len(X), len(Y)
    
    # 創建DP表格
    L = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    # 填充DP表格
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    # 打印表頭
    print("\nDP表格:")
    print("    |", end="")
    print("   |", end="")
    for j in range(n):
        print(f" {Y[j]} |", end="")
    print("\n----+---+", end="")
    print("---+".join(["" for _ in range(n+1)]))
    
    # 打印表格內容
    for i in range(m+1):
        if i == 0:
            print("    |", end="")
        else:
            print(f" {X[i-1]} |", end="")
        
        for j in range(n+1):
            print(f" {L[i][j]} |", end="")
        print()
    
    return L[m][n]

if __name__ == "__main__":

  # 範例1: 數字序列
  X = [1, 0, 0, 1, 0, 1, 0, 1]
  Y = [0, 1, 0, 1, 1, 0, 1, 1, 0]

  length, result = lcs(X, Y)
  print(f"序列 {X} 和 {Y} 的LCS長度為: {length}")
  print(f"LCS為: {result}")


  # 範例2: 字串
  A = "ABCBDAB"
  B = "BDCABA"

  length, result = lcs(A, B)
  print(f"\n字串 '{A}' 和 '{B}' 的LCS長度為: {length}")
  print(f"LCS為: {''.join(result)}")

  # 視覺化範例
  # print("\n視覺化DP表格:")
  print_dp_table("ABCBDAB", "BDCABA")