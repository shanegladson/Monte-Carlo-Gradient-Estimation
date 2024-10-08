from src._distributions._univariate_exponential import _UnivariateExponentialDistribution
from src._distributions._univariate_gamma import _UnivariateGammaDistribution
from src._distributions._univariate_maxwell import _UnivariateDSMaxwellDistribution
from src._distributions._univariate_normal import _UnivariateNormalDistribution
from src._distributions._univariate_poisson import _UnivariatePoissonDistribution
from src._distributions._univariate_uniform import _UnivariateUniformDistribution
from src._distributions._univariate_weibull import _UnivariateWeibullDistribution


class UnivariateUniformDistribution(_UnivariateUniformDistribution):
    pass


class UnivariateNormalDistribution(_UnivariateNormalDistribution):
    pass


class UnivariateDSMaxwellDistribution(_UnivariateDSMaxwellDistribution):
    pass


class UnivariateWeibullDistribution(_UnivariateWeibullDistribution):
    pass


class UnivariateGammaDistribution(_UnivariateGammaDistribution):
    pass


class UnivariateExponentialDistribution(_UnivariateExponentialDistribution):
    pass


class UnivariatePoissonDistribution(_UnivariatePoissonDistribution):
    pass
