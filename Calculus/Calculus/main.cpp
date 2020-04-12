#include <iostream>
#include <fstream>
#include "calculation.h"




using namespace std;


double f(double x)
{
	return (x - 2.5) * (x - 2.5);

}

int main()
{
	ofstream results_file("Results.txt");

	double a = 10;
	double b = 15;
	double eps = 1;
	double puason_coef = 0.25; //steal
	double E = 200;

	Solution2 calc(a, b, eps, puason_coef, E, f);

	int N_x = 100;
	int N_y = 10;

	double h_x = a / N_x;
	double h_y = b / N_y;

	results_file << a << " " << b << " " << N_x << " " << N_y << endl;

	for (int j = 0; j <= N_y; ++j)
	{
		for (int i = 0; i <= N_x; ++i)
		{

			double x = i * h_x;
			double y = j * h_y;
			results_file << calc.sigma_Y(x, y) << " ";
		}

		results_file << endl;
	}

	system("pause");
	return 0;
}