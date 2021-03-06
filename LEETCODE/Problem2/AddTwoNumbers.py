# Runtime: 56 ms, faster than 99.03% of Python3 online submissions for Add Two Numbers.
# Memory Usage: 14.3 MB, less than 44.61% of Python3 online submissions for Add Two Numbers.


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        head=ListNode(0)
        p=head
        carry=0
        while l1!=None or l2!=None:
            x=0
            y=0
            if l1:
               x=l1.val
               l1=l1.next
            if l2:
                y=l2.val
                l2=l2.next
            
            val=x+y+carry

            p.next=ListNode(val%10)

            carry=val//10

            p=p.next
        
        if carry:
            p.next=ListNode(carry)

        return head.next
             


class Main:
   def main(self):
       list1=[9,9,9,9,9,9,9]
       list2=[9,9,9,9]
       count=0
       for i in list1:
           if count==0:
              l1=ListNode(i)
              p=l1
           else:
              p.next=ListNode(i) 
              p=p.next 
           count+=1

       count=0
       for j in list2:
            if count==0:
              l2=ListNode(j)
              p=l2
            else:
              p.next=ListNode(j) 
              p=p.next 
            count+=1  
           

       p=Solution().addTwoNumbers(l1,l2)

       while p!=None:
           print(p.val)
           p=p.next

if __name__=="__main__":
    Main().main()






# space complexity O(1) approach

# def addTwoNumbers(self, l1, l2):          
    #     x,y=l1,l2
    #     flag=0
    #     while x!=None and y!=None:
    #         x=x.next
    #         y=y.next

    #     if y!=None:
    #         flag=1
    #         p,q=l2,l1
    #     else:
    #         p,q=l1,l2
    #     carry=0
    #     while p!=None and q!=None:
    #         p.val+=q.val
    #         if len(str(p.val))!=1:
    #             carry=p.val//10
    #             p.val=p.val%10
    #             if p.next ==None:
    #                 p.next=ListNode(carry)
    #             else:
    #                p.next.val+=carry
    #         p=p.next
    #         q=q.next
 
    #     if p!=None:
    #         if len(str(p.val))!=1:
    #             while p!=None:
    #                 carry=p.val//10
    #                 p.val%=10
    #                 if p.next!=None:
    #                     p.next.val+=carry
    #                 if p.next==None and carry!=0:
    #                     p.next=ListNode(carry)
    #                 p=p.next

    #     if flag==1:
    #         return l2
    #     else:
    #         return l1
     
     
     
