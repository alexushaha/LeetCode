/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseList(ListNode head) {
        Stack<Integer> stack = new Stack<Integer>();
        ListNode cur = head;
        // use a stack to store values of LL, then replace values with popped out values from stack
        while(cur != null){
            stack.push(cur.val);
            cur = cur.next;
        }
        cur = head;
        while(cur != null){
            cur.val = stack.pop();
            cur = cur.next;
        }
        return head;
    }
}