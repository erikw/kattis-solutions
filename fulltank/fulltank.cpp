#include <functional>
#include <iostream>
#include <vector>
#include <queue>
#include <map>

using namespace std;

const unsigned infinity = 1 << 28;


/** @brief Print the graph to standard out.

    @param G The graph to be printed.
*/
void print_graph(vector<vector<pair<unsigned, unsigned> > > &G)
{
    for (size_t i = 0; i < G.size(); ++i)
    {
        for (size_t j = 0; j < G[i].size(); ++j)
        {
            pair<unsigned, unsigned> p = G[i][j];
            cout << i << " - " << p.second << " -> " << p.first << endl;
        }
        if (G[i].empty())
        {
            cout << i << " - (X)" << endl;
        }
    }
}


struct Vertex
{
    Vertex(unsigned id, unsigned tank, unsigned cost) :
        id(id), tank(tank), cost(cost) {}
    unsigned id;
    unsigned tank;
    unsigned cost;
};

bool operator>(const Vertex &v0, const Vertex &v1)
{
    return v0.cost > v1.cost;
}


/** @brief Use Dijkstra's algorithm to compute the cheapest way to dst.

    @param G      The graph with the roads and lengths.
    @param prices The prices to fuel at the i:th city.
    @param src    The source city to start from
    @param dst    The destination city to look for.
    @param cap    The capacity of the vehicle.
    @return The cost to reach the destination, or 'infinity' if unreachable.
*/
unsigned shortest_path(vector<vector<pair<unsigned, unsigned> > > &G,
                       vector<unsigned> prices,
                       unsigned src,
                       unsigned dst,
                       unsigned cap)
{
    vector<vector<unsigned> > cost(G.size(), vector<unsigned>(100, infinity));
    vector<vector<bool> >     visited(G.size(), vector<bool>(100, false));
    priority_queue<Vertex, vector<Vertex>, greater<Vertex> > Q;

    cost[src][0] = 0;
    Q.push(Vertex(src, 0, 0));

    while (!Q.empty())
    {
        Vertex u = Q.top();
        Q.pop();
        // cout << u.id << " " << u.tank << " " << u.cost << endl;

        if (visited[u.id][u.tank])
        {
            continue;
        }

        if (dst == u.id)
        {
            break;
        }

        // Check if we can move to a neighboring vertex.
        if (u.tank < cap &&
            u.cost + prices[u.id] < cost[u.id][u.tank + 1])
        {
            unsigned new_cost = u.cost + prices[u.id];
            cost[u.id][u.tank + 1] = new_cost;
            Q.push(Vertex(u.id, u.tank + 1, new_cost));
        }

        for (size_t i = 0; i < G[u.id].size(); ++i)
        {
            unsigned v = G[u.id][i].first;
            unsigned d = G[u.id][i].second;
            if (u.tank >= d &&
                cost[u.id][u.tank] < cost[v][u.tank - d])
            {
                cost[v][u.tank - d] = cost[u.id][u.tank];
                Q.push(Vertex(v, u.tank - d, cost[v][u.tank - d]));
            }
        }
        visited[u.id][u.tank] = true;
    }
    return cost[dst][0];
}


int main()
{
    unsigned n = 0;
    unsigned m = 0;
    cin >> n >> m;

    vector<unsigned> prices(n);
    for (size_t i = 0; i < n; ++i)
    {
        cin >> prices[i];
    }

    vector<vector<pair<unsigned, unsigned> > > G(n);

    for (size_t i = 0; i < m; ++i)
    {
        unsigned u = 0;
        unsigned v = 0;
        unsigned d = 0;
        cin >> u >> v >> d;
        G[u].push_back(make_pair(v, d));
        G[v].push_back(make_pair(u, d));
    }

    unsigned q = 0;
    cin >> q;
    for (size_t i = 0; i < q; ++i)
    {
        unsigned c = 0;
        unsigned s = 0;
        unsigned e = 0;
        cin >> c >> s >> e;
        unsigned cost = shortest_path(G, prices, s, e, c);
        if (cost < infinity)
        {
            cout << cost << endl;
        }
        else
        {
            cout << "impossible" << endl;
        }
    }

    return 0;
}
