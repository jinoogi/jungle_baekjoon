import sys
sys.setrecursionlimit(10**6)
input_list=[]
tree_dict={}

def formtree_from_preorder(node,list): #리스트와 노드를 받아서 left,right로 쪼개고 딕셔너리에 추가. 1개 요소로 나올때까지 재귀적으로 함
    if len(list)==1:
        tree_dict[node]=['.','.']
        return
    else: 
        right_idx = next((i for i, num in enumerate(list) if num > node), None) # node보다 큰 수가 처음 나오는 인덱스 반환. 없으면 none 반환
        left_idx = next((len(list) - i - 1 for i, num in enumerate(reversed(list)) if num < node), None)
        if left_idx!=None and right_idx!=None:
            left_tree=list[1:left_idx+1]
            right_tree=list[right_idx:]
            tree_dict[node]=[left_tree[0],right_tree[0]]
            formtree_from_preorder(left_tree[0],left_tree)
            formtree_from_preorder(right_tree[0],right_tree)
        elif left_idx!=None and right_idx==None:
            left_tree=list[1:left_idx+1]
            tree_dict[node]=[left_tree[0],'.']
            formtree_from_preorder(left_tree[0],left_tree)
        elif left_idx==None and right_idx!=None:
            right_tree=list[right_idx:]
            tree_dict[node]=['.',right_tree[0]]
            formtree_from_preorder(right_tree[0],right_tree)

def postorder_traversal(N): #노드를 받아 후위순회 결과출력

    if tree_dict[N][0]!='.':
        postorder_traversal(tree_dict[N][0])
    if tree_dict[N][1]!='.':
        postorder_traversal(tree_dict[N][1])
    print(N)

while True: #입력 종료시까지 입력받음    user_input=sys.stdin.readline()
    user_input = sys.stdin.readline().rstrip('\n')
    if user_input != '':
        input_list.append(int(user_input))
    else:
        break

# print(input_list)
formtree_from_preorder(input_list[0],input_list)
# print(tree_dict)
postorder_traversal(input_list[0])