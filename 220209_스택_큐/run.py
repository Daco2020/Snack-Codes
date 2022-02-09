'''
< 스택 과 큐 >
'Stack'은 나중에 들어온 것을 먼저 내보내는 후입선출을 뜻한다.
'Queue'는 먼저 들어온 것을 먼저 내보내는 선입선출을 뜻한다. 

이를 파이썬 코드로 구현하자면 다음과 같다.
'''


stack_list = []

for i in range(5):
    stack_list.append(i)
    print(f"stack_push :: {stack_list}")

for _ in range(5):
    stack_list.pop()
    print(f"stack_pop :: {stack_list}")


'''
<스택 용어>
top - 스택의 가장 윗부분 (꼭대기)
bottom - 스택의 가장 아랫부분 (바닥)
push(item) - 데이터를 넣는 작업
pop() - 데이터를 꺼내는 작업
peek() - 스택의 가장 위에 있는 항목 조회

stack_push :: [0]
stack_push :: [0, 1]
stack_push :: [0, 1, 2]
stack_push :: [0, 1, 2, 3]
stack_push :: [0, 1, 2, 3, 4]
stack_pop  :: [0, 1, 2, 3]
stack_pop  :: [0, 1, 2]
stack_pop  :: [0, 1]
stack_pop  :: [0]
stack_pop  :: []

스택은 가장 나중에 들어온 4부터 차례대로 꺼낸다.
'''


queue_list = []

for i in range(5):
    queue_list.append(i)
    print(f"queue_enqueue :: {queue_list}")

for _ in range(5):
    queue_list.pop(0)
    print(f"queue_dequeue :: {queue_list}")


'''
<큐 용어>
front - 데이터를 꺼내는 쪽(맨 앞)
rear - 데이터를 넣는 쪽(맨 뒤)
enqueue(item) - 데이터를 넣는 작업
dequeue() - 데이터를 꺼내는 작업
peek() - 큐의 가장 앞에 있는 항목 조회

queue_enqueue :: [0]
queue_enqueue :: [0, 1]
queue_enqueue :: [0, 1, 2]
queue_enqueue :: [0, 1, 2, 3]
queue_enqueue :: [0, 1, 2, 3, 4]
queue_dequeue ::    [1, 2, 3, 4]
queue_dequeue ::       [2, 3, 4]
queue_dequeue ::          [3, 4]
queue_dequeue ::             [4]
queue_dequeue ::              []

큐는 가장 먼저들어온 0부터 차례로 꺼낸다.
'''
