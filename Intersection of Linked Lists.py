class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def getIntersectionNode(headA, headB):
    if not headA or not headB:
        return None
    
    pointerA, pointerB = headA, headB

    while pointerA != pointerB:
        pointerA = pointerA.next if pointerA else headB
        pointerB = pointerB.next if pointerB else headA

    return pointerA

a1 = ListNode(1)
a2 = ListNode(2)
c1 = ListNode(3)
c2 = ListNode(4)
c3 = ListNode(5)
b1 = ListNode(6)
b2 = ListNode(7)

a1.next = a2
a2.next = c1
c1.next = c2
c2.next = c3

b1.next = b2
b2.next = c1
intersection_node = getIntersectionNode(a1, b1)

if intersection_node:
    print("Intersection point at node with value:", intersection_node.value)
else:
    print("No intersection point")
