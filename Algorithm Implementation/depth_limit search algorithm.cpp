#include <iostream>
#include <vector>
using namespace std;

bool DLS(const vector<vector<int>> &graph, int current, int goal, int limit, vector<bool> &visited)
{
    if (current == goal){
        cout << "Goal found at node: " << current << "\n";
        return true;
    }

    if (limit == 0)
        return false;

    visited[current] = true;
    for (int neighbor : graph[current]){
        if (!visited[neighbor]){
            if (DLS(graph, neighbor, goal, limit - 1, visited))
                return true;
        }
    }
       return false;
}

int main()
{
    int n, e;
    cout << "Enter number of nodes and edges: ";
    cin >> n >> e;
    vector<vector<int>> graph(n);

    cout << "Enter edges (u v):\n";
    for (int i = 0; i < e; ++i)
    {
        int u, v;
        cin >> u >> v;
        graph[u].push_back(v);
    }

    int start, goal, limit;
    cout << "Enter start, goal, and depth limit: ";
    cin >> start >> goal >> limit;

    vector<bool> visited(n, false);  /// if n=5 then  visited=[false,false,false]false,false]

    if (!DLS(graph, start, goal, limit, visited))
        cout << "Goal not reachable within depth limit.\n";

    return 0;
}
