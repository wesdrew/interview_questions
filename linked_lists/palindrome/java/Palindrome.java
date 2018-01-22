import java.util.LinkedList;
import java.util.Queue;

/**

Using Queue as singly-linked list:

    1. return whether linked-list of integers represents a palindrome 

    ex: 0 -> 1 -> 2 -> 3 -> 2 -> 1 -> 0 is a palindrome

 */


public class Palindrome {


    public static void main(String[] args) {
	Queue<Integer> list = getLinkedList(args);
	System.out.println(isPalindrome(list, list.size()));
    }


    /**
        list --> head (sublist) tail			   
        list is a palindrome if head and tail are same Integer 
        and sublist is a palindrome			      
    */

    public static boolean isPalindrome(Queue<Integer> subList, int length) {
	if (length == 1 ) { // sublist is of length 1 or 0, return True
	    subList.remove();	// if 1, remove that element so it won't mess up logic in else clause
	    return true; 
	}
	else if (length == 0) {
	    return true;
	}
	else {
	    Integer subHead = subList.remove();
	    return isPalindrome(subList, length - 2) && (subHead == subList.remove());
	}
    }
	    


    // process cmd line args into linked-list
    public static Queue<Integer> getLinkedList(String[] args) {
	Queue<Integer> list = new LinkedList<Integer>();
	for (int i = 0; i < args.length; i++) {
	    list.add(Integer.parseInt(args[i]));
	}
	return list;
    }
}