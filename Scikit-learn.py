from sklearn.model_selection import GridSearchCV
from sklearn import linear_model, datasets
import numpy as np
from sklearn.linear_model import Lasso
from sklearn import datasets

diabetes = datasets.load_diabetes()

X = diabetes.data
y = diabetes.target

X.shape
X[:5]

y.shape
y[:10]

feature_names = ['age', 'sex', 'bmi', 'bp', 's1', 's2', 's3', 's4', 's5', 's6']

X_train = diabetes.data[:310]
y_train = diabetes.target[:310]

X_test = diabetes.data[310:]
y_test = diabetes.data[310:]

lasso = Lasso(random_state=0)
alphas = np.logspace(-4, -0.5, 30)

estimator = GridSearchCV(lasso, dict(alpha=alphas))
estimator.fit(X_train, y_train)

GridSearchCV(cv=None, error_score='raise',
             estimator=Lasso(alpha=1.0, copy_X=True, fit_intercept=True, max_iter=1000,
                             normalize=False, positive=False, precompute=False, random_state=0,
                             selection='cyclic', tol=0.0001, warm_start=False),
             fit_params={}, iid=True, n_jobs=1,
             param_grid={'alpha': array([1.00000e-04, 1.32035e-04, 1.74333e-04, 2.30181e-04,
                                         3.03920e-04, ..., 2.39503e-01, 3.16228e-01])},
             pre_dispatch='2*n_jobs', refit=True, return_train_score=True, scoring=None,
             verbose=0)

estimator.best_score_
estimator.best_estimator_

estimator.predict(X_test)