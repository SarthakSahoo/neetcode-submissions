class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binary_search(arr, target):
            print('1: ', arr, target)
            n_left, n_right = 0, len(arr) - 1
            while n_left <= n_right:
                n_mid = n_left + (n_right - n_left) // 2
                print('2: ', n_left, n_mid, n_right)
                if arr[n_mid] == target:
                    return True
                elif arr[n_mid] >= target:
                    n_right = n_mid - 1
                else:
                    n_left = n_mid + 1
            return False
        
        m_left, m_right = 0, len(matrix) - 1
        while m_left <= m_right:
            m_mid = m_left + (m_right - m_left) // 2
            temp_arr = matrix[m_mid]
            print(temp_arr)
            if temp_arr[0] <= target and temp_arr[-1] >= target:
                print(1)
                return binary_search(temp_arr, target)
            elif target > temp_arr[-1]:
                m_left = m_mid + 1
            else:
                m_right = m_mid - 1

        return False
