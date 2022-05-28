#include <iostream>
#include <queue>
#include <stack>
using namespace std;
 
int main(int argc, char *argv[])
{
    int n, c, d, ele;
    bool sw1, sw2, sw3;
    while (cin >> n)
    {
        sw1 = true;
        sw2 = true;
        sw3 = true;
        stack <int> p;
        queue<int> q;
        priority_queue<int> pq;
        while (n--)
        {
            cin >> c >> d;
            if (c == 1)
            {
                p.push(d);
                q.push(d);
                pq.push(d);
            }
            else
            {
                if (!p.empty() && sw1)
                {
                    ele = p.top();
                    p.pop();
                    if (d != ele)
                        sw1 = false;
                }
                else
                    sw1 = false;
                if (!q.empty() && sw2)
                {
                    ele = q.front();
                    q.pop();
                    if (d != ele)
                        sw2 = false;
                }
                else
                    sw2 = false;
                if (!pq.empty() && sw3)
                {
                    ele = pq.top();
                    pq.pop();
                    if (d != ele)
                        sw3 = false;
                }
                else
                    sw3 = false;
            }
        }
        if (sw1 && !sw2 && !sw3)
            cout << "stack";
        else if (!sw1 && sw2 && !sw3)
            cout << "queue";
        else if (!sw1 && !sw2 && sw3)
            cout << "priority queue";
        else if (!sw1 && !sw2 && !sw3)
            cout << "impossible";
        else
            cout << "not sure";
        cout << '\n';
    }
}