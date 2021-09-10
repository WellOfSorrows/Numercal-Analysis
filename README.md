# Numercal-Analysis
This is the Python implementations of some numerical methods, based on the pseudo-codes provided in the Numerical Analysis book by Richard L. Burden & J. Douglas Faires.

The project includes
* Root finding algorithms.
* Interpolation techniques.
* Numercial integration methods.
* Methods of solving ODE and initial-value problems.
* Matrix elimination and factorization algorithms.
* Iterative techniques for approximating linear equations.


### Root-finding
Currently, the project contains following root-finding methods:
* [Bisection method](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/root_finding/bisection_method.py)
* [False position method](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/root_finding/false_position_method.py)
* [Fixed-point iteration method](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/root_finding/fixed_point_iteration_method.py)
* [Müller's method](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/root_finding/muller_method.py)
* [Newton-Horner method](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/root_finding/newton_horner_method.py)
* [Newton-Raphson method](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/root_finding/newton_raphson_method.py)
* [Secant method](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/root_finding/secant_method.py)
* [Steffensen's method](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/root_finding/steffensen_method.py)


### Interpolation
Currently, the project contains following interpolation techniques:
* [Lagrange polynomials](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/interpolation/lagrange_interpolation_polynomials.py)
* [Neville's iterated interpolation](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/interpolation/neville_iterated_interpolation.py)
* [Newton's divided difference](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/interpolation/newton_divided_difference.py)
* [Hermite interpolation](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/interpolation/hermite_interpolation.py)
* [Natural cubic spline](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/interpolation/cubic_spline_natural.py)
* [Clamped cubic spline](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/interpolation/cubic_spline_clamped.py)
* [Bezier's curve](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/interpolation/bezier_curve.py)


### Integration
Currently, the project contains following numercial integration methods:
* [Composite midpoint rule](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/integration/composite_midpoint_rule.py)
* [Composite Simpson's rule](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/integration/composite_simpson_rule.py)
* [Composite trapezoidal rule](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/integration/composite_trapezoidal_rule.py)
* [Romberg's integration](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/integration/romberg_integration.py)
* [Adaptive quadrature](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/integration/adaptive_quadrature.py)
* [Simpson's double integral](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/integration/simpson_double_integral.py)
* [Gaussian double integral](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/integration/gaussian_double_integral.py)


### ODE and initial-value problems
Currently, the project contains following methods of solving ODE and initial-value problems:
* [Euler's method](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/ode/euler_method.py)
* [Runge-Kutta order four method](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/ode/runge_kutta_method.py)

More methods will be implemented soon.


### Matrix elimination and factorization
Currently, the project contains following elimination and factorization techniques:
* [Gaussian elimination with backward substitution](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/linear_direct_methods/gaussian_elimination_backward_substitution.py)
* [Gaussian elimination with partial pivoting](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/linear_direct_methods/gaussian_elimination_partial_pivoting.py)
* [Gaussian elimination with scaled partial pivoting](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/linear_direct_methods/gaussian_elimination_partial_pivoting_scaled.py)
* [LU factorization](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/linear_direct_methods/lu_factorization.py)
* [LDL<sup>T</sup> factorization](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/linear_direct_methods/ldlt_factorization.py)
* [Cholesky's factorization](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/linear_direct_methods/cholesky_factorization.py)
* [Crout factorization](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/linear_direct_methods/crout_factorization.py)


### Matrix iterative techniques
Currently, the project contains following matrix iterative techniques:
* [Jacobi's iterative technique](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/linear_iterative_techniques/jacobi_iterative_technique.py)
* [Gauss-Seidel iterative method](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/linear_iterative_techniques/gauss_seidel_iterative_method.py)
* [Successive over-relaxation (SOR) method](https://github.com/WellOfSorrows/Numercal-Analysis/blob/main/src/linear_iterative_techniques/sor.py)
