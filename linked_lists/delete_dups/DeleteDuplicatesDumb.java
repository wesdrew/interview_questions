import java.util.LinkedList;



// Remove duplicates from an unsorted linked list
// Since we don't have access to the node data struct in LinkedList,
// pop the first element off (Object o) the list and add to LinkedList ret. 
// Scan the passed-in LinkedList in for o and remove it from in. 


public class DeleteDuplicatesDumb {

    public static LinkedList<Object> removeAllDuplicates(LinkedList<Object> in) { 
	LinkedList<Object> ret = new LinkedList<Object>();
	while (in.size() > 0) {
	    Object o = in.removeFirst();
	    in = removeDuplicate(o, in);
	    ret.add(o);
	}
	return ret;
    }

    public static boolean isDuplicate(Object o1, Object o2) {
	return o1.equals(o2); 
    }

    public static LinkedList<Object> removeDuplicate(Object o, LinkedList<Object> in) { 
	LinkedList<Object> ret = new LinkedList<Object>();
	for (Object o2 : in) {
	    if (!isDuplicate(o, o2)) {
		ret.add(o2);
	    }
	}
	return ret;
    }

    public static void main(String[] args) { 
	LinkedList<Object> test = new LinkedList<Object>();
	String[] names = {"wes", "wes", "drew", "wes" };
	for (String name: names) {
	    test.add((Object) name);
	}
	test = removeAllDuplicates(test);
	for (Object s : test) {
	    System.out.println((String) s);
	}
    } 

}