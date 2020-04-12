#include "calculation.h"

#include <math.h>

const double PI = 3.141592653589793238463;


void Solution1::check_function()
{

	double C1, C2, C3, C4;

	double alpha_n = 2 * PI / a;
	double e = exp(alpha_n * b);
	double pn = cos_integration(0, a, alpha_n, load_function);

	double b1 = -pn * alpha_n * 4 * (1 + mu_0);
	double b2 = b1 * alpha_n;


	calculate_coef(alpha_n, C1, C2, C3, C4);

	double a1 = C1 * (2 * alpha_n + 2 * alpha_n * mu_0) + C3 * (2 * alpha_n + 2 * alpha_n * mu_0);

	double a2 = C2 * (2 + mu_0) + C4 * (-2 - mu_0);

	double a3 = C1 * e * (b * alpha_n * alpha_n * mu_0 + 2 * alpha_n + 2 * alpha_n * mu_0) + C2 * e * (b * alpha_n * alpha_n * mu_0 + alpha_n * mu_0)
		+ C3 / e * (-b * alpha_n * alpha_n * mu_0 + 2 * alpha_n + 2 * alpha_n * mu_0) + C4 / e * (b * alpha_n * alpha_n * mu_0 - alpha_n * mu_0);

	double a4 = C1 * e * (-b * alpha_n * mu_0) + C2 * e * (-b * alpha_n * mu_0 + 2 + mu_0) + C3 / e * (b * alpha_n * mu_0) + C4 / e * (-b * alpha_n * mu_0 - 2 - mu_0);

	double a5 = function_Vn(b, alpha_n);

}


double Solution1::cos_integration(const double& a, const double& b, const double& alpha_n, double(*f) (double))
{
	double result = 0, prev_result = 0;

	int N = 100;

	double h = (b - a) / N;

	for (int i = 1; i < N; ++i)
	{
		double x = a + i * h;;
		result += f(x) * cos(alpha_n * x);
	}

	result *= h;

	do {
		N *= 2;
		h /= 2;
		prev_result = result;
		result = 0;

		for (int i = 1; i < N; ++i)
		{
			double x = a + i * h;
			result += f(x) * cos(alpha_n * x);
		}
		result *= h;

	} while (fabs(result - prev_result) > eps);

	return result;
}

void Solution1::calculate_coef(const double& alpha_n, double& C1, double& C2, double& C3, double& C4)
{
	double pn = cos_integration(0, a, alpha_n, load_function);

	double alpha_pow_2 = alpha_n * alpha_n, alpha_pow_4 = alpha_pow_2 * alpha_pow_2;
	double e = exp(2 * alpha_n * b);
	double e1 = exp(alpha_n * b);

	double det = 4 * alpha_pow_2 * e * e * mu_0_pow_4 + 24 * alpha_pow_2 * e * e * mu_0_pow_2 * mu_0 + 52 * alpha_pow_2 * e * e * mu_0_pow_2 + 48 * alpha_pow_2 * e * e * mu_0 + 16 * alpha_pow_2 * e * e 
		- 8 * alpha_pow_2 * e * mu_0_pow_4 - 48 * alpha_pow_2 * e * mu_0_pow_2 * mu_0 - 104 * alpha_pow_2 * e * mu_0_pow_2 - 96 * alpha_pow_2 * e * mu_0
		- 32 * alpha_pow_2 * e + 4 * alpha_pow_2 * mu_0_pow_4 + 24 * alpha_pow_2 * mu_0_pow_2 * mu_0 + 52 * alpha_pow_2 * mu_0_pow_2 + 48 * alpha_pow_2 * mu_0 + 16 * alpha_pow_2;
	det /= -e;

	double detC1 = 16 * alpha_pow_4 * b * e * mu_0_pow_4 * pn + 64 * alpha_pow_4 * b * e * mu_0_pow_2 * mu_0 * pn + 80 * alpha_pow_4 * b * e * mu_0_pow_2 * pn + 32 * alpha_pow_4 * b * e * mu_0 * pn
		+ 16 * alpha_pow_4 * b * mu_0_pow_4 * pn + 64 * alpha_pow_4 * b * mu_0_pow_2 * mu_0 * pn + 80 * alpha_pow_4 * b * mu_0_pow_2 * pn + 32 * alpha_pow_4 * b * mu_0 * pn
		- 16 * alpha_pow_2 * alpha_n * e  * mu_0_pow_2 * mu_0 * pn - 64 * alpha_pow_2 * alpha_n * e * mu_0_pow_2 * pn - 80 * alpha_pow_2 * alpha_n * e * mu_0 * pn - 32 * alpha_pow_2 * alpha_n * e * pn
		+ 16 * alpha_pow_2 * alpha_n * mu_0_pow_2 * mu_0 * pn + 64 * alpha_pow_2 * alpha_n * mu_0_pow_2 * pn + 80 * alpha_pow_2 * alpha_n * pn + 32 * alpha_pow_2 * alpha_n * pn;
	detC1 /= -e1;

	double detC2 = 16 * alpha_pow_4 * b * e * mu_0_pow_4 * pn + 64 * alpha_pow_4 * b * e * mu_0_pow_2 * mu_0 * pn + 80 * alpha_pow_4 * b * e * mu_0_pow_2 * pn + 32 * alpha_pow_4 * b * e * mu_0 * pn
		+ 16 * alpha_pow_4 * b * mu_0_pow_4 * pn + 64 * alpha_pow_4 * b * mu_0_pow_2 * mu_0 * pn + 80 * alpha_pow_4 * b * mu_0_pow_2 * pn + 32 * alpha_pow_4 * b * mu_0 * pn
		+ 16 * alpha_pow_2 * alpha_n * e * mu_0_pow_4 * pn + 80 * alpha_pow_2 * alpha_n * e * mu_0_pow_2 * mu_0 * pn + 144 * alpha_pow_2 * alpha_n * e * mu_0_pow_2 * pn
		+ 112 * alpha_pow_2 * alpha_n * e * mu_0 * pn + 32 * alpha_pow_2 * alpha_n * e * pn - 16 * alpha_pow_2 * alpha_n * mu_0_pow_4 * pn - 80 * alpha_pow_2 * alpha_n * mu_0_pow_2 * mu_0 * pn 
		- 144 * alpha_pow_2 * alpha_n * mu_0_pow_2 * pn	- 112 * alpha_pow_2 * alpha_n * mu_0 * pn - 32 * alpha_pow_2 * alpha_n * pn;
	detC2 /= e1;

	C1 = detC1 / det;
	C2 = detC2 / det;
	C3 = -C1;
	C4 = C2;

}

double Solution1::function_Un(double y, double alpha_n)
{
	double result = 0;

	double coef1 = 1.0 / alpha_n / 4.0 / (1 + mu_0);

	double C1 = 0, C2 = 0, C3 = 0, C4 = 0;
	double e = exp(alpha_n * y), e1 = exp(-alpha_n * y);

	calculate_coef(alpha_n, C1, C2, C3, C4);
	
	result = C1 * e * (y * alpha_n * mu_0 + 2 + mu_0) + C2 * e * y * alpha_n * mu_0 + C3 * e1 * (y * mu_0 * alpha_n - 2 - mu_0) + C4 * e1 * (-y * alpha_n * mu_0);

	result *= coef1;

	return result;
}

double Solution1::function_Vn(double y, double alpha_n)
{
	double result = 0;

	double coef1 = 1.0 / alpha_n / 4.0 / (1 + mu_0);

	double C1, C2, C3, C4;
	double e = exp(alpha_n * y), e1 = exp(-alpha_n * y);

	calculate_coef(alpha_n, C1, C2, C3, C4);

	result = C1 * e * (-y * alpha_n * mu_0) + C2 * e * (-y * alpha_n * mu_0 + 2 + mu_0) + C3 * e1 * (y * alpha_n * mu_0) + C4 * e1 * (-y * alpha_n * mu_0 - 2 - mu_0);

	result *= coef1;

	return result;
}



double Solution1::function_U(double x, double y)
{
	double result = 0, prev_result = 0;

	int N = 10;
	
	if (x != a && x != 0)
	{
		for (int i = 1; i < N; ++i)
		{
			double alpha_n = PI * i / a;
			result += 2 * function_Un(y, alpha_n) * sin(alpha_n * x) / a;
		}
	}

	do {
		prev_result = result;
		N *= 2;
		result = 0;

		if (x != a && x != 0) {
			for (int i = 1; i < N; ++i)
			{
				double alpha_n = PI * i / a;
				result += 2 * function_Un(y, alpha_n) * sin(alpha_n * x) / a;
			}
		}

	} while (fabs(result - prev_result) > eps);

	return result;
}

double Solution1::function_V(double x, double y)
{
	double result = 0, prev_result = 0;

	int N = 10;

	double p0 = cos_integration(0, a, 0, load_function);

	result = -p0 * y / a /  b;

	for (int i = 1; i < N; ++i)
	{
		double alpha_n = PI * i / a;
		result += 2 * function_Vn(y, alpha_n) * cos(alpha_n * x) / a;
	}

	do {
		N *= 2;
		prev_result = result;
		result = -p0 * y / a / b;

		for (int i = 1; i < N; ++i)
		{
			double alpha_n = PI * i / a;
			result += 2 * function_Vn(y, alpha_n) * cos(alpha_n * x) / a;
		}

	} while (fabs(result - prev_result) > eps);

	return result;
}

double Solution1::derivative_Ux(double x, double y)
{
	double result = 0, prev_result = 0;

	int N = 80;

	for (int i = 1; i < N; ++i)
	{
		double alpha_n = PI * i / a;
		if (x != a && x != 0)
			result += 2 * alpha_n * function_Un(y, alpha_n) * cos(alpha_n * x) / a;
	}

	/*
	do {
		prev_result = result;
		N += 10;
		result = 0;

		for (int i = 1; i < N; ++i)
		{
			double alpha_n = PI * i / a;
			if (x != a && x != 0)
				result += 2 * alpha_n * function_Un(y, alpha_n) * cos(alpha_n * x) / a;
		}

	} while (fabs(result - prev_result) > eps); */

	return result;
}

double Solution1::derivative_Vn(double y, double alpha_n)
{
	double result = 0;

	double coef1 = 1.0 / alpha_n / 4.0 / (1 + mu_0);

	double C1, C2, C3, C4;
	double e = exp(alpha_n * y), e1 = exp(-alpha_n * y);

	calculate_coef(alpha_n, C1, C2, C3, C4);

	result = C1 * e * (-y * alpha_n * alpha_n * mu_0 - alpha_n * mu_0) + C2 * e * (-y * alpha_n * alpha_n * mu_0 + 2 * alpha_n) 
		+ C3 * e1 * (-y * alpha_n * alpha_n * mu_0 + alpha_n * mu_0) + C4 * e1 * (y * alpha_n * alpha_n * mu_0 + 2 * alpha_n);

	result *= coef1;

	return result;
}

double Solution1::derivative_Vy(double x, double y)
{
	double result = 0, prev_result = 0;

	int N = 90;

	double p0 = cos_integration(0, a, 0, load_function);

	result = -p0  / a / b;

	for (int i = 1; i < N; ++i)
	{
		double alpha_n = PI * i / a;
		result += 2 * derivative_Vn(y, alpha_n) * cos(alpha_n * x) / a;
	}

	/*
	do {
		N += 10;
		prev_result = result;
		result = -p0 / a / b;

		for (int i = 1; i < N; ++i)
		{
			double alpha_n = PI * i / a;
			result += 2 * derivative_Vn(y, alpha_n) * cos(alpha_n * x) / a;
		}

	} while (fabs(result - prev_result) > eps); */

	return result;
}

double Solution1::sigma_Y(double x, double y)
{
	double dUx = derivative_Ux(x, y);
	double dVy = derivative_Vy(x, y);

	return 2 * G * dVy + lambda * dVy + lambda * dUx;
}

double Solution1::sigma_X(double x, double y)
{
	double dUx = derivative_Ux(x, y);
	double dVy = derivative_Vy(x, y);

	return 2 * G * dUx + lambda * dVy + lambda * dUx;
}