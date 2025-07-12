#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>
using namespace std;


bool bidirectional_search(vector<vector<int>> &graph, int start, int goal)
{
    unordered_set<int> visited_f, visited_b;  /// f for forward b for backward
    queue<int> q_f, q_b;  //// ques for perfrom BFS

    q_f.push(start);    /// add start to the queue
    q_b.push(goal);    /// add goal to the queue
    visited_f.insert(start);    /// mark them visited
    visited_b.insert(goal);   /// mark them visitited



    while (!q_f.empty() && !q_b.empty())
    {
        int f = q_f.front();   /// pop front elemnt
        q_f.pop();
        int b = q_b.front();
        q_b.pop();

     

         //// If the current node in the forward search (f) has already been visited by the

        //// backward search or vice versa, a meeting point is found, meaning a path has been found between the start and goal.
       
        //// The function returns true and prints the meeting point.

        if (visited_b.count(f) || visited_f.count(b))
        {
            cout << "Path found (meeting point at " << f << " or " << b << ")\n";
            return true;
        }
      

        /// for every neighbour of f if it is not visited then make it visited 

        for (int neigh : graph[f])
        {
            if (!visited_f.count(neigh))
            {
                visited_f.insert(neigh);
                q_f.push(neigh);
            }
        }

        /// also apply for backward search same as f 

        for (int neigh : graph[b])
        {
            if (!visited_b.count(neigh))
            {
                visited_b.insert(neigh);
                q_b.push(neigh);
            }
        }
    }

    return false;  // if f and b eempty them retutrn false
}

int main()
{
    int n, e;
    cout << "Enter number of nodes and edges: ";
    cin >> n >> e;
    vector<vector<int>> graph(n);
    cout << "Enter edges:\n";
    for (int i = 0; i < e; ++i)
    {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
        graph[v].push_back(u); // undirected
    }

    int start, goal;
    cout << "Enter start and goal: ";
    cin >> start >> goal;

    if (!bidirectional_search(graph, start, goal))
    {
        cout << "No path found.\n";
    }
}
