import java.util.Deque;
import java.util.HashSet;
import java.util.LinkedList;

public class LRUCache {

    // store keys of cache
    // first element is least recently used
    LinkedList<Integer> dq;

    // store references of key in cache
    private HashSet<Integer> map;

    // maximum capacity of cache
    int csize;

    LRUCache(int n) {
        dq = new LinkedList<>();
        map = new HashSet<>();
        csize = n;
    }

    void refer(int x) {
        Integer key = Integer.valueOf(x);
        if (map.contains(key)) {
            dq.remove(key);
            dq.add(key);
        } else {
            while (map.size() >= csize) {
                Integer oldKey = dq.remove();
                map.remove(oldKey);
            }
            map.add(key);
            dq.add(key);
        }
    }

    // display contents of cache
    private void display() {
        for (Integer integer : dq) {
            System.out.print(integer + " ");
        }
        System.out.println("");
    }

    public static void main(String[] args) {
        LRUCache ca = new LRUCache(4);
        ca.refer(1);
        ca.refer(2);
        ca.refer(3);
        ca.refer(1);
        ca.refer(4);
        ca.refer(5);
        ca.display();
    }

}
