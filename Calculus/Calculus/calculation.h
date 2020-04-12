#pragma once
#ifndef  CALCULATION_H
#define CALCULATION_H


class Solution1 {

	double a;
	double b;
	double eps;

	double(*load_function) (double);

	double puason_coef;
	double mu_0;
	double E;
	double G;
	double lambda;

	
	double b_pow_2, b_pow_4;
	double mu_0_pow_2, mu_0_pow_4;

	double derivative_Vn(double y, double alpha_n);

	double function_Un(double y, double alpha_n);
	double function_Vn(double y, double alpha_n);

	void calculate_coef(const double& alpha_n, double& C1, double& C2, double& C3, double& C4);

	double cos_integration(const double& a, const double& b, const double& alpha_n, double(*f) (double));

public:
	Solution1(double a, double b, double eps, double puason_coef, double E, double (*f)(double)) :a(a), b(b), eps(eps), puason_coef(puason_coef),
		mu_0(1.0 / (1 - 2 * puason_coef)), E(E), G(E / 2 / (1 + puason_coef)), lambda(puason_coef * E / (1 + puason_coef) / (1 - 2 * puason_coef)),
		b_pow_2(b * b), b_pow_4(b_pow_2 * b_pow_2), mu_0_pow_2(mu_0 * mu_0), mu_0_pow_4(mu_0_pow_2 * mu_0_pow_2),
		load_function(f) {}

	~Solution1() {}

	void check_function();

	double function_U(double x, double y);
	double function_V(double x, double y);
	double derivative_Ux(double x, double y);
	double derivative_Vy(double x, double y);
	double sigma_X(double x, double y);
	double sigma_Y(double x, double y);

};



class Solution2 {

	double a;
	double b;
	double eps;

	double(*load_function) (double);

	double puason_coef;
	double mu_0;
	double E;
	double G;
	double lambda;


	double b_pow_2, b_pow_4;
	double mu_0_pow_2, mu_0_pow_4;

	double derivative_Vn(double y, double alpha_n);

	double function_Un(double y, double alpha_n);
	double function_Vn(double y, double alpha_n);

	void calculate_coef(const double& alpha_n, double& C1, double& C2, double& C3, double& C4);

	double cos_integration(const double& a, const double& b, const double& alpha_n, double(*f) (double));

public:
	Solution2(double a, double b, double eps, double puason_coef, double E, double(*f)(double)) :a(a), b(b), eps(eps), puason_coef(puason_coef),
		mu_0(1.0 / (1 - 2 * puason_coef)), E(E), G(E / 2 / (1 + puason_coef)), lambda(puason_coef * E / (1 + puason_coef) / (1 - 2 * puason_coef)),
		b_pow_2(b * b), b_pow_4(b_pow_2 * b_pow_2), mu_0_pow_2(mu_0 * mu_0), mu_0_pow_4(mu_0_pow_2 * mu_0_pow_2),
		load_function(f) {}

	~Solution2() {}

	void check_function();

	double function_U(double x, double y);
	double function_V(double x, double y);
	double derivative_Ux(double x, double y);
	double derivative_Vy(double x, double y);
	double sigma_X(double x, double y);
	double sigma_Y(double x, double y);

};


#endif // ! CALCULATION_H

