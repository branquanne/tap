#include <iomanip>
#include <iostream>
#include <list>
#include <vector>
#include <bits/stdc++.h>

using namespace std;

class Node
{
    public:
        double x;
        double y;
        bool visited;
    Node( double a, double b);
};

Node::Node( double a, double b) {
    x=a;
    y=b;
    visited=false;
}

double calculate_dist(Node* a, Node* b) {
    double dx = (b->x - a->x);
    double dy = (b->y - a->y);
    return sqrt((pow(dx,2) + pow(dy,2)));
}

/**
 * @brief Finds the closest node to the from node

 * @param set list of unvisited nodes
 * @param from node to search from
 * @return Node* the nearest node
 */
static Node* find_nearest_neighbor(std::list<Node*> set, Node* from) {
    Node* next;
    double smallest = std::numeric_limits<double>::infinity();
    for (Node* n : set) {
        double dist = calculate_dist(from, n);
        if (dist < smallest) {
            smallest=dist;
            next = n;
        }   
    }
    return next; 
}

/**
 * @brief Helper function for modified nearest (pair) not really 
 * 
 * @param vec vector of nodes 
 * @param start starting node
 * @return std::list<Node*> list of nodes visited in order
 */
std::list<Node*> my_own_heuristic_h(std::vector<Node*> vec, Node* start) {
    std::list<Node*> finalTour;
    std::list<Node*> to_Visit(vec.begin(),vec.end());
    //Distance calculation mostly for development
    to_Visit.remove(start);
    finalTour.push_back(start);
    Node* left;
    Node* right;
    Node* temp;
    while (!to_Visit.empty()) {
        left = finalTour.front();
        right = finalTour.back();
        //Find the closest neighbor to the left and insert in the front of the list
        temp = find_nearest_neighbor(to_Visit, left);
        to_Visit.remove(temp);
        //Push the one closest from the left one to the front of the list
        finalTour.push_front(temp);
        //Ugly solution to the case where left finds the last node
        if (!to_Visit.empty()) {
            temp = find_nearest_neighbor(to_Visit, right);
            to_Visit.remove(temp);
            //Push the one closest from the right to the back of the list
            finalTour.push_back(temp);
        }
    }
    
    return finalTour;  
}

vector<Node*> parseInput() {
    int num_nodes;
    vector<Node*> node_list;
    string line;
    //Skip through all comment lines
    while(getline(cin, line)) {
        if (!(line[0] == '#')) {
            num_nodes = stoi(line);
            break;
        }
    }
    
    for (int i = 0; i < num_nodes; i++) {
        double x, y;
        cin >> x >> y;
        node_list.push_back(new Node(x,y));
    }

    return node_list;
}

double calculate_path(list<Node*> tour) {
    double distance = 0;
    Node* start = tour.front();
    Node* temp = start;
    for (const auto& node : tour) {
        distance += calculate_dist(temp, node);
        temp = node;
    }
    distance += calculate_dist(temp, start);
    return distance;
}

/**
 * @brief An Nearest Neighbor heuristic modified by searching for the best starting node 
 * 
 * @param vec input vector of nodes
 * @return std::list<Node*> list of nodes in order of traversal
 */
std::list<Node*> my_own_heuristic(std::vector<Node*> vec) {
    std::list<Node*> visited;
    std::list<Node*> temp;
    double shortest_path = std::numeric_limits<double>::infinity();
    //Brute-force step, try each node in the vector as start
    for(const auto& node : vec) {
        temp = my_own_heuristic_h(vec, node);
        double temp_d = calculate_path(temp);

        if (temp_d < shortest_path) {
            shortest_path=temp_d;            
            visited=temp;
        }
    }
    return visited;
}

int main() {
    std::vector<Node*> node_list = parseInput();
    double initial_tour = calculate_path(std::list<Node*>(node_list.begin(), node_list.end()));
    std::list<Node*> tour = my_own_heuristic(node_list);
    double heuristicTour = calculate_path(tour);
    double percentage = heuristicTour/initial_tour*100;

    std::cout << "# Input file distance: " << std::fixed << std::setprecision(2)<< initial_tour << std::endl;
    std::cout << "# This path distance: " << std::fixed << std::setprecision(2)<< heuristicTour << std::endl;
    std::cout << "# " << std::fixed << std::setprecision(2) << percentage << "\% of the original" << std::endl;
    std::cout << tour.size() << std::endl;
    for (const auto& node : tour) {
        std::cout << (long) node->x << " " << (long) node->y << std::endl;
    }

    return 0;
}
