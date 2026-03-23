#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

/** 
 * Implementation av närmsta-par-heuristiken.
 * 
 * Algoritm:
 * 	Börja med varje punkt som en egen väg (singleton)
 * 	Hitta det närmaste paret av ändpunkter från olika vägar
 * 	Koppla ihop dessa vägar
 * 	Upprepa tills vi har en enda väg
 * 	Stäng cykeln genom att koppla de två sista ändpunkterna
 */

typedef struct {
	int x;
	int y;
	int next;
	int prev;
	int path_id;
} Point;

typedef struct {
	Point *points;
	int n;
} Graph;

// Läs in grafen från stdin
Graph* read_graph(FILE *in) {
	Graph *g = malloc(sizeof(Graph));
	if (g == NULL) {
		perror("malloc");
		return NULL;
	}
	
	char line[256];
	while (fgets(line, sizeof(line), in)) {
		if (line[0] != '#') {
			sscanf(line, "%d", &g->n);
			break;
		}
	}
	
	g->points = malloc(g->n * sizeof(Point));
	
	for (int i = 0; i < g->n; i++) {
		fscanf(in, "%d %d", &g->points[i].x, &g->points[i].y);
		g->points[i].next = -1;
		g->points[i].prev = -1;
		g->points[i].path_id = i;  // Varje punkt börjar som egen väg
	}
	
	return g;
}

// Beräkna avstånd mellan två punkter
double distance(Point *p1, Point *p2) {
	double dx = p2->x - p1->x;
	double dy = p2->y - p1->y;
	return sqrt(dx * dx + dy * dy);
}

// Kolla om en punkt är en ändpunkt (har minst ett -1)
bool is_endpoint(Point *p) {
	return (p->next == -1 || p->prev == -1);
}

// Koppla ihop två ändpunkter
void connect_endpoints(Graph *g, int i, int j) {
	Point *pi = &g->points[i];
	Point *pj = &g->points[j];
	
	// Hitta den fria änden på varje punkt och koppla
	if (pi->next == -1) {
		pi->next = j;
	} else {
		pi->prev = j;
	}
	
	if (pj->next == -1) {
		pj->next = i;
	} else {
		pj->prev = i;
	}
	
	// Uppdatera path_id för alla punkter i pj's väg
	int old_id = pj->path_id;
	int new_id = pi->path_id;
	
	for (int k = 0; k < g->n; k++) {
		if (g->points[k].path_id == old_id) {
			g->points[k].path_id = new_id;
		}
	}
}

// Närmsta-par algoritmen
void nearest_pair(Graph *g) {
	int num_paths = g->n;
	
	// Merga vägar tills vi har en enda väg
	while (num_paths > 1) {
		double min_dist = INFINITY;
		int best_i = -1, best_j = -1;
		
		// Hitta närmaste paret av ändpunkter från olika vägar
		for (int i = 0; i < g->n; i++) {
			if (!is_endpoint(&g->points[i])) continue;
			
			for (int j = i + 1; j < g->n; j++) {
				if (!is_endpoint(&g->points[j])) continue;
				if (g->points[i].path_id == g->points[j].path_id) continue;
				
				double d = distance(&g->points[i], &g->points[j]);
				if (d < min_dist) {
					min_dist = d;
					best_i = i;
					best_j = j;
				}
			}
		}
		
		// Koppla ihop de närmaste
		if (best_i != -1 && best_j != -1) {
			connect_endpoints(g, best_i, best_j);
			num_paths--;
		}
	}
	
	// Stäng cykeln genom att koppla de två sista ändpunkterna
	int ep1 = -1, ep2 = -1;
	for (int i = 0; i < g->n; i++) {
		if (is_endpoint(&g->points[i])) {
			if (ep1 == -1) {
				ep1 = i;
			} else {
				ep2 = i;
				break;
			}
		}
	}
	
	if (ep1 != -1 && ep2 != -1) {
		connect_endpoints(g, ep1, ep2);
	}
}

// Skriv ut turen
void print_tour(Graph *g) {
	printf("%d\n", g->n);
	
	int curr = 0;
	int prev = -1;
	
	for (int i = 0; i < g->n; i++) {
		Point *p = &g->points[curr];
		printf("%d %d\n", p->x, p->y);
		
		// Hitta nästa (den vi inte kom ifrån)
		int next = (p->next != prev) ? p->next : p->prev;
		prev = curr;
		curr = next;
	}
}

int main(void) {
	Graph *g = read_graph(stdin);
	
	if (g == NULL) {
		fprintf(stderr, "Error: Could not read graph\n");
		return 1;
	}
	
	nearest_pair(g);
	print_tour(g);
	
	free(g->points);
	free(g);

	return 0;
}