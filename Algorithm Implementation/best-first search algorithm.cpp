#include <bits/stdc++.h>
using namespace std;

// A Node class for GBFS Pathfinding

// destination vertex v
// weight edge weight

class Node
{
public:
    int v, weight;
    Node(int V, int Weight)
    {
        v = V;
        weight = Weight;
    }
};

// pathNode class will help to store the path from src to dest.

/// node current vertex
/// parent ita pointer indicates the previous index

class pathNode
{
public:
    int node;
    pathNode *parent;
    pathNode(int Node)
    {
        node = Node;
        parent = NULL;
    }
    pathNode(int Node, pathNode *Parent)
    {
        node = Node;
        parent = Parent;
    }
};

// Declaring the adjacency list


static vector<vector<Node *>> adj;

// Function to add edge in the graph
void addEdge(int u, int v, int weight)
{
    adj[u].push_back(new Node(v, weight));
}

// Greedy best first search algorithm function
// h[]: Heuristic values for each node
// V: Number of vertices
// src: Source node
// dest: Destination node

vector<int> GBFS(int h[], int V, int src, int dest)
{
    vector<pathNode *> openList;
    vector<pathNode *> closeList;

    openList.push_back(new pathNode(src));

    while (!openList.empty())
    {
        pathNode *currentNode = openList[0];
        int currentIndex = 0;

        // Finding the node with the least 'h' value.
        // openList: Nodes to be explored
        //  closeList: Already explored nodes

        for (int i = 0; i < openList.size(); i++)
        {
            if (h[openList[i]->node] < h[currentNode->node])
            {
                currentNode = openList[i];
                currentIndex = i;
            }
        }

        openList.erase(openList.begin() + currentIndex);
        closeList.push_back(currentNode);

        if (currentNode->node == dest)
        {
            vector<int> path;
            pathNode *cur = currentNode;
            while (cur != NULL)
            {
                path.push_back(cur->node);
                cur = cur->parent;
            }
            reverse(path.begin(), path.end());
            return path;
        }

        /// if no list foud in the block create path node and add opne list to explore it later

        for (Node *node : adj[currentNode->node])
        {
            bool foundInOpenList = false, foundInCloseList = false;

            ///  x points to each individual node in the openList.

            /// here open list stores poninter

            for (pathNode *x : openList)
            {
                if (x->node == node->v)
                {
                    foundInOpenList = true;
                    break;
                }
            }
            for (pathNode *x : closeList)
            {
                if (x->node == node->v)
                {
                    foundInCloseList = true;
                    break;
                }
            }
            if (!foundInOpenList && !foundInCloseList)
            {
                openList.push_back(new pathNode(node->v, currentNode));
            }
        }
    }
    return vector<int>();
}

int main()
{
    int V, E;

    // Taking user input for number of vertices and edges
    cout << "Enter the number of vertices: ";
    cin >> V;

    adj.resize(V);

    cout << "Enter the number of edges: ";
    cin >> E;

    cout << "Enter the edges (u v weight) one by one:" << endl;
    for (int i = 0; i < E; i++)
    {
        int u, v, weight;
        cin >> u >> v >> weight;
        addEdge(u, v, weight);
    }

    // Taking heuristic values for each vertex

    int h[V];
    cout << "Enter the heuristic values for each vertex:" << endl;
    for (int i = 0; i < V; i++)
    {
        cin >> h[i];
    }

    // Taking source and destination nodes

    int src, dest;
    cout << "Enter the source node: ";
    cin >> src;
    cout << "Enter the destination node: ";
    cin >> dest;

    vector<int> path = GBFS(h, V, src, dest);

    if (path.empty())
    {
        cout << "No path found from " << src << " to " << dest << endl;
    }
    else
    {
        cout << "Path from " << src << " to " << dest << ": ";
        for (int i = 0; i < path.size() - 1; i++)
        {
            cout << path[i] << " --> ";
        }
        cout << path[path.size() - 1] << endl;
    }

    return 0;
}
