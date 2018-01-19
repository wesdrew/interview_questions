//////////////////////////////////////////////////////////
// find the kth to last element of a singly linked list //
//////////////////////////////////////////////////////////

import java.util.LinkedList;
import java.util.Queue;



public class KthToLast {

    public static void main(String[] args) {
	if (args.length > 0) {
	    int k = Integer.parseInt(args[0]);
	    if (k >= args.length) { // check user input
		System.out.println("k is greater than provided list");
	    }
	    else if (k == 0) {
		System.out.println("k cannot be 0");
	    }
	    else {
		Queue<String> list = new LinkedList<String>();
		for (int i = 1; i < args.length; i++) {
		    list.add(args[i]); // load queue
		}
		// removing kth to last --> travel sub-list.length (arg.length - 1) - k elements 
		System.out.println("kth element == " + getK(args.length - 1 - k, list).toString());
	    }
	}
	else {			// user did not provide any input!
	    System.out.println("format: k element_1 element_2 ....element_n");
	}
    }

    // finding kth to LAST element in linked list
    public static String getK(int k, Queue<String> list) {
	if (k == 0) {
	    return list.poll();
	}
	else {
	    list.poll(); 	// throw away the head of this list
	    return getK(--k, list);	    
	}
    }

}