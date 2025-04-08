import numpy as np

def matrix_chain_order(p):
    n = len(p) - 1  # 矩陣數量
    m = np.zeros((n+1, n+1))  # 儲存最優值
    s = np.zeros((n+1, n+1), dtype=int)  # 儲存最優分割點
    
    # l 是鏈長
    for l in range(2, n+1):
        for i in range(1, n-l+2):
            j = i + l - 1
            m[i, j] = float('inf')
            for k in range(i, j):
                q = m[i, k] + m[k+1, j] + p[i-1] * p[k] * p[j]
                if q < m[i, j]:
                    m[i, j] = q
                    s[i, j] = k
    
    # 打印表格
    print("M表格 (最小運算次數):")
    print(m[1:n+1, 1:n+1])
    print("\nS表格 (最優分割點):")
    print(s[1:n+1, 1:n+1])
    
    return m, s

def print_optimal_parens(s, i, j):
    if i == j:
        return f"A{i}"
    else:
        return f"({print_optimal_parens(s, i, s[i, j])}·{print_optimal_parens(s, s[i, j]+1, j)})"

# 維度序列
p = [5, 10, 3, 12, 5, 50, 6]
m, s = matrix_chain_order(p)

# 打印最優括號化和最小乘法次數
print("\n最優括號化方案:")
print(print_optimal_parens(s, 1, 6))
print(f"最小乘法運算次數: {int(m[1, 6])}")