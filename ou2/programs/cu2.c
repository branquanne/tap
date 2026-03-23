#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <stdbool.h>

/**
 * Implementation av billigaste-insättning heuristiken
 * 
 * Algoritm:
 * 	Börja med en triangel av tre punkter (de som är längst från varandra)
 * 	För varje punkt utom triangelpunkterna:
 * 		Beräkna kostnaden att sätta in punkten på varje position i turen
 * 		Kostnad = avstånd från föregående + avstånd till nästa - bortagen kant
 * 		Välj den punkt och position som ger lägsta totalkostnaden
 */

typedef struct {
	int x, y;
	bool in_tour;
} Point;

typedef struct {
	Point *points;
	int *tour;
	int n;
	int tour_size;
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
	g->tour = malloc(g->n * sizeof(int));
	if (g->points == NULL || g->tour == NULL) {
		perror("malloc");
		free(g);
		return NULL;
	}
	
	for (int i = 0; i < g->n; i++) {
		fscanf(in, "%d %d", &g->points[i].x, &g->points[i].y);
		g->points[i].in_tour = false;
	}
	
	g->tour_size = 0;
	
	return g;
}

// Beräkna avstånd mellan två punkter
double distance(Point *p1, Point *p2) {
	double dx = p2->x - p1->x;
	double dy = p2->y - p1->y;
	return sqrt(dx * dx + dy * dy);
}

// Hitta de tre punkter som bildar största triangeln (approximation)
void find_initial_triangle(Graph *g) {
	// Hitta två punkter som är längst från varandra
	double max_dist = -1;
	int p1 = 0, p2 = 1;
	
	for (int i = 0; i < g->n; i++) {
		for (int j = i + 1; j < g->n; j++) {
			double d = distance(&g->points[i], &g->points[j]);
			if (d > max_dist) {
				max_dist = d;
				p1 = i;
				p2 = j;
			}
		}
	}
	
	// Hitta tredje punkt som är längst från de två första
	max_dist = -1;
	int p3 = -1;
	for (int i = 0; i < g->n; i++) {
		if (i == p1 || i == p2) continue;
		double d1 = distance(&g->points[i], &g->points[p1]);
		double d2 = distance(&g->points[i], &g->points[p2]);
		double d = d1 + d2;
		if (d > max_dist) {
			max_dist = d;
			p3 = i;
		}
	}
	
	// Bygg initial triangel
	g->tour[0] = p1;
	g->tour[1] = p2;
	g->tour[2] = p3;
	g->tour_size = 3;
	
	g->points[p1].in_tour = true;
	g->points[p2].in_tour = true;
	g->points[p3].in_tour = true;
}

// Beräkna kostnaden att sätta in punkt k mellan position i och i+1 i turen
double insertion_cost(Graph *g, int k, int pos) {
	int next_pos = (pos + 1) % g->tour_size;
	
	Point *prev = &g->points[g->tour[pos]];
	Point *next = &g->points[g->tour[next_pos]];
	Point *new_point = &g->points[k];
	
	// Kostnad = ny väg (prev->new + new->next) - gammal väg (prev->next)
	double old_dist = distance(prev, next);
	double new_dist = distance(prev, new_point) + distance(new_point, next);
	
	return new_dist - old_dist;
}

// Sätt in punkt k på position pos i turen
void insert_in_tour(Graph *g, int k, int pos) {
	// Skifta alla element efter pos ett steg åt höger
	for (int i = g->tour_size; i > pos + 1; i--) {
		g->tour[i] = g->tour[i - 1];
	}
	
	// Sätt in nya punkten
	g->tour[pos + 1] = k;
	g->tour_size++;
	g->points[k].in_tour = true;
}

// Cheapest insertion algoritm
void cheapest_insertion(Graph *g) {
	// Börja med triangel
	find_initial_triangle(g);
	
	// Sätt in resterande punkter en i taget
	while (g->tour_size < g->n) {
		double min_cost = INFINITY;
		int best_point = -1;
		int best_position = -1;
		
		// Testa alla obesökta punkter
		for (int k = 0; k < g->n; k++) {
			if (g->points[k].in_tour) continue;
			
			// Testa alla positioner i turen
			for (int pos = 0; pos < g->tour_size; pos++) {
				double cost = insertion_cost(g, k, pos);
				
				if (cost < min_cost) {
					min_cost = cost;
					best_point = k;
					best_position = pos;
				}
			}
		}
		
		// Sätt in den bästa punkten på bästa positionen
		if (best_point != -1) {
			insert_in_tour(g, best_point, best_position);
		}
	}
}

// Skriv ut turen
void print_tour(Graph *g) {
	printf("%d\n", g->n);
	for (int i = 0; i < g->tour_size; i++) {
		printf("%d %d\n", g->points[g->tour[i]].x, g->points[g->tour[i]].y);
	}
}

int main(void) {
	Graph *g = read_graph(stdin);
	
	if (g == NULL) {
		fprintf(stderr, "Error: Could not read graph\n");
		return 1;
	}
	
	cheapest_insertion(g);
	print_tour(g);
	
	free(g->tour);
	free(g->points);
	free(g);
	return 0;
}