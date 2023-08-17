#include <iostream>
#include <queue>
#include <list>
#include <vector>

using namespace std;

class Graph{
    public:
        vector<list<int>> adjacentList;
        int numberVertices;

        Graph(int vernumberVerticestices);

        void addEdge(int vertice, int edge);

        void BFS(int initialState);
};

Graph::Graph(int numberVertices){
    this->numberVertices = numberVertices;
    adjacentList.resize(numberVertices);
};

void Graph::addEdge(int vertice, int edge){
    adjacentList[vertice].push_back(edge);
};

void Graph::BFS(int initialState){

}

