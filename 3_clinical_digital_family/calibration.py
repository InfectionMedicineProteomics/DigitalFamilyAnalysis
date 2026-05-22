import pandas as pd

def calc_bootstrap_counts(combined_results, estimator, base_col, target_col):
    bootstrap_counts = []

    for bootstrap_iteration in estimator.bootstrap_columns:

        col_range = combined_results[bootstrap_iteration].unique()
        col_range.sort()
        actual_values = []

        counts_per_bin = []

        for val in col_range:

            counts = combined_results[combined_results[bootstrap_iteration] == val][target_col].value_counts()
            actual_values.append(counts.get(1, 0) / (counts.get(0, 0) + counts.get(1, 0)))
            counts_per_bin.append(counts.sum())

        estimated_ = pd.DataFrame(
            {
                f"Actual {base_col}": actual_values,
                f"Estimated {base_col}": col_range,
                "Counts": counts_per_bin
            }
        )

        bootstrap_counts.append(estimated_)

    bootstrap_counts = pd.concat(bootstrap_counts)

    return bootstrap_counts


def calc_linregress(bootstrap_counts, base_col, linregress_results):

    predictions = linregress_results.intercept + linregress_results.slope*bootstrap_counts[f'Estimated {base_col}'].unique()

    predictions = pd.DataFrame(
    {
            "x": bootstrap_counts[f'Estimated {base_col}'].unique(),
            "y": predictions
        }
    )

    predictions = predictions.sort_values("x")

    predictions['x'] = predictions['x'].astype("str")

    return predictions


