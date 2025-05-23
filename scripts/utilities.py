import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway, kruskal


def load_country_data(filepath, country_name):
    try:
        df = pd.read_csv(filepath)
        df['Country'] = country_name
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Unexpected error loading {country_name}: {e}")
        return pd.DataFrame()


def plot_boxplot(data, metric):
    try:
        plt.figure(figsize=(8, 5))
        sns.boxplot(data=data, x='Country', y=metric, palette='Set2')
        plt.title(f'{metric} Distribution by Country')
        plt.ylabel(f'{metric} (kWh/m²/day)')
        plt.xlabel('')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error plotting boxplot for {metric}: {e}")


def generate_summary_table(df, metrics):
    return df.groupby('Country')[metrics].agg(['mean', 'median', 'std']).round(2)


def perform_statistical_tests(ghi_series_list, test_names):
    try:
        results = {}
        if 'anova' in test_names:
            f_stat, p_anova = f_oneway(*ghi_series_list)
            results['anova'] = p_anova
        if 'kruskal' in test_names:
            h_stat, p_kruskal = kruskal(*ghi_series_list)
            results['kruskal'] = p_kruskal
        return results
    except Exception as e:
        print(f"Statistical test failed: {e}")
        return {}


def plot_avg_bar_chart(df, metric):
    try:
        avg = df.groupby('Country')[metric].mean().sort_values(ascending=False)
        plt.figure(figsize=(6, 4))
        sns.barplot(x=avg.values, y=avg.index, palette='Set3')
        plt.xlabel(f'Average {metric} (kWh/m²/day)')
        plt.title(f'Average {metric} by Country')
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Error plotting bar chart for {metric}: {e}")
