from sklearn.metrics import r2_score, mean_squared_error
import seaborn as sns


def scatter_plot(x,y,ax=None):
    ax = sns.regplot(x=x, y=y, ax=ax)
    r2 = r2_score(x, y)
    mse = mean_squared_error(x, y)
    ax.set_title(f'R2={r2:.2f}, MSE={mse:.2e}')
    return ax