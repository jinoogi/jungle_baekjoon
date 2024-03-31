class Node:
    def __init__(self):
        self.data=None
        self.left_ptr=None
        self.right_ptr=None


def tree_former(data,parent): #루트 데이터를 입력받아 딕셔너리를 조회하고 연속적으로 연결리스트 형성
    
    parent.data=data
    left_data=input_dict[parent.data][0]
    right_data=input_dict[parent.data][1]
    if left_data!=".": #left가 있으면
        left=Node()
        parent.left_ptr=left
        tree_former(left_data,left) #left 데이터를 입력해서 연속 연결리스트 형성
    if right_data!=".": #right가 있으면
        right=Node()
        parent.right_ptr=right
        tree_former(right_data,right) #right 데이터를 입력해서 연속 연결리스트 형성

def preorder_traversal(root): #루트 포인터를 입력받아 전위순회 결과 반환
    global preorder_result

    preorder_result=preorder_result+root.data
    if root.left_ptr!=None:
        preorder_traversal(root.left_ptr)
    if root.right_ptr!=None:
        preorder_traversal(root.right_ptr)



def inorder_traversal(root): #루트 포인터를 입력받아 전위순회 결과 반환
    global inorder_result


    if root.left_ptr!=None:
        inorder_traversal(root.left_ptr)
    inorder_result=inorder_result+root.data
    if root.right_ptr!=None:
        inorder_traversal(root.right_ptr)

def postorder_traversal(root): #루트 포인터를 입력받아 전위순회 결과 반환
    global postorder_result

    if root.left_ptr!=None:
        postorder_traversal(root.left_ptr)
    
    if root.right_ptr!=None:
        postorder_traversal(root.right_ptr)
    postorder_result=postorder_result+root.data

input_dict={}
preorder_result=""
inorder_result=""
postorder_result=""
N=int(input()) # 이진트리의 노드개수
for i in range(1,N+1):
    input_string=input()
    input_string=input_string.split()
    root,left,right=input_string[0],input_string[1],input_string[2]
    input_dict[root]=(left,right)

root=Node()
tree_former('A',root)


preorder_traversal(root)
inorder_traversal(root)
postorder_traversal(root)
# print(root.right_ptr.right_ptr.right_ptr.data)
print(preorder_result)
print(inorder_result)
print(postorder_result)