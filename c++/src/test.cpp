// Standards
#include <iostream>
#include <string>
#include <list>
#include <iterator>
#include <unordered_map>

class LRUCache {
    // store keys of cache
    std::list<int> dq;

    // store references of key in cache
    std::unordered_map<int, std::list<int>::iterator> ma;
    int csize; //maximum capacity of cache

public:
    LRUCache(int);
    void refer(int);
    void display();
};

LRUCache::LRUCache(int n)
{
    csize = n;
}

/* Refers key x with in the LRU cache */
void LRUCache::refer(int x)
{
    // not present in cache
    if (ma.find(x) == ma.end()) {
        // cache is full
        if (dq.size() == csize) {
            //delete least recently used element
            int last = dq.back();
            dq.pop_back();
            ma.erase(last);
        }
    }
    // present in cache
    else {
        dq.erase(ma[x]);
    }

    // update reference
    dq.push_front(x);
    ma[x] = dq.begin();
}

// display contents of cache
void LRUCache::display()
{
    for (auto it = dq.begin(); it != dq.end(); it++) {
        std::cout << (*it) << " ";
    }

    std::cout << std::endl;
}

// Driver program to test above functions
int main()
{
    LRUCache ca(4);

    ca.refer(1);
    ca.refer(2);
    ca.refer(3);
    ca.refer(1);
    ca.refer(4);
    ca.refer(5);
    ca.display();

    return 0;
}
