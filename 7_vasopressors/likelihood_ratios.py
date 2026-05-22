import pandas as pd
import numpy as np
from sklearn.metrics import class_likelihood_ratios, recall_score, roc_auc_score

def calc_likelihood_ratios(combined_results, label_col, title, cutoffs, bootstrap_columns):

    bootstrapped_recalls = []
    bootstrapped_aucs = []
    bootstrapped_precisions = []
    plr_gp = []
    thresholds = []

    subsample = combined_results.copy()

    for col in bootstrap_columns:

        bootstrapped_recalls.append(
            recall_score(subsample[label_col], np.where(subsample[col] > 0.0, 1, 0))
        )


        bootstrapped_aucs.append(
            roc_auc_score(
                subsample[label_col], subsample[col]
            )
        )

        for cutoff in cutoffs:
            plr_gp.append(
                class_likelihood_ratios(subsample[label_col], np.where(subsample[col] > cutoff, 1, 0))[0]
            )
            thresholds.append(cutoff)

    lr_df = pd.DataFrame(
        {
            "LR+": plr_gp,
            "Cutoff": thresholds,
            "Label": [title for _ in range(len(plr_gp))],
        }
    )

    bs_df = pd.DataFrame(
        {
            "Recall": bootstrapped_recalls,
            "AUC": bootstrapped_aucs,
            "Label": [title for _ in range(len(bootstrapped_recalls))],
        }
    )

    return bs_df, lr_df
