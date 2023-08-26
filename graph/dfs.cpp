#include <iostream>
#include <map>
#include <list>

using namespace std;

class Graph {
public:
    map<int, bool> visited;
    map<int, list<int> > adj;

    void addEdge(int vertex, int edge);

    void DFS(int state, int goalState);
};

void Graph::addEdge(int vertex, int edge) {
    adj[vertex].push_back(edge);
};

void Graph::DFS(int state, int goalState) {
    visited[state] = true;

    if (state == goalState) {
        cout << "Goal state found at node " << state << endl;
    }

    for (auto adjacent: adj[state]) {
        if (!visited[adjacent]) {
            DFS(adjacent, goalState);
        }
    }
    

}


int main() {
    Graph g;
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);
    g.DFS(0,2);
}