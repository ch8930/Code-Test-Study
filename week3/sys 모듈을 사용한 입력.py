# 한 줄 입력받아 출력하는 소스코드
# 입력값이 커질 경우 input() 함수를 사용하면 동작 속도가 느려서 시간 초과로 오답 판정을 받을 수 있음
# 해당 코드는 대화형 환경인 주피터 노트북에서는 제대로 동작되지 않음
import sys

input_data = sys.stdin.readline().rstrip()

print(input_data)