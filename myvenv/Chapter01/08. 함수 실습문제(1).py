def printSumAvg(x, y, z):
    """
    입력받은 세가지 수의 합과 평균을 구하는 함수
    x : int
    y : int
    z : int
    """
    sum = x + y + z
    avg = sum / 3
    print (f"합계 : {sum} 평균 : {avg}")

printSumAvg(10, 20, 30)