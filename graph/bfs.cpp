#include <iostream>
#include <list>
#include <vector>

using namespace std;

class Graph{
    public:
        vector<list<int> > adjacentList;
        int numberVertices;

        Graph(int vernumberVerticestices);

        void addEdge(int vertice, int edge);

        void BFS(int startNode, int goalNode);
};

Graph::Graph(int numberVertices){
    this->numberVertices = numberVertices;
    adjacentList.resize(numberVertices);
};

void Graph::addEdge(int vertice, int edge){
    adjacentList[vertice].push_back(edge);
};

void Graph::BFS(int startNode, int goalNode){
    vector<bool> visited;
    visited.resize(numberVertices, false);

    list<int> frontier;
    visited[startNode] = true;
    frontier.push_back(startNode);

    while (!frontier.empty()) {
        startNode = frontier.front();
        frontier.pop_front();

        if (startNode == goalNode) {
            cout << "found node" << endl;
            cout << "Found at startNode" << endl;
        }

        for (auto adjacent: adjacentList[startNode]) {
            if (adjacent == goalNode) {
                cout << "goal state found" << endl; 
                cout << adjacent <<  " is located at " << "vertice " << startNode << endl;
            } else if (!visited[adjacent]) {
                visited[adjacent] = true;
                frontier.push_back(adjacent);
            }
        }
    }
}

int main() {
    Graph g(4);
    g.addEdge(0, 1);
    g.addEdge(0, 2);
    g.addEdge(1, 2);
    g.addEdge(2, 0);
    g.addEdge(2, 3);
    g.addEdge(3, 3);
    g.BFS(0,3);
}

