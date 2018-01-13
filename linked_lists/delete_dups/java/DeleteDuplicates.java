import java.util.HashSet;
import java.util.LinkedList;



// Remove duplicates from an unsorted linked list
// Use HashSet to check if we already saw this Object

public class DeleteDuplicates {

    public static HashSet<Object> set = new HashSet<Object>();

    public static LinkedList<Object> removeAllDuplicates(LinkedList<Object> in) { 
	LinkedList<Object> ret = new LinkedList<Object>();
	for (Object o : in) {
	    if (!isDuplicate(o)) {
		set.add(o);
		ret.add(o);
	    }
	}
	return ret;

    }

    public static boolean isDuplicate(Object o) {
	return set.contains(o);
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