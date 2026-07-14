# Part E – AI Libraries Research

## Comparison Table: NumPy, Pandas, Scikit-learn, TensorFlow, PyTorch

| Library | Purpose | Typical Applications |
|---|---|---|
| **NumPy** | Core library for numerical computing — provides the `ndarray` object for fast, memory-efficient N-dimensional arrays and vectorized math operations. | Linear algebra, numerical simulations, the low-level array engine underneath Pandas/Scikit-learn/TensorFlow/PyTorch. |
| **Pandas** | Data manipulation and analysis library built on NumPy — provides `Series`/`DataFrame` structures for labeled, tabular data. | Loading/cleaning CSV/Excel/SQL data, exploratory data analysis (EDA), feature preparation before modeling. |
| **Scikit-learn** | General-purpose machine learning library implementing classical ML algorithms and a consistent `fit`/`predict` API. | Regression, classification, clustering, dimensionality reduction, model evaluation and hyperparameter tuning for tabular data. |
| **TensorFlow** | End-to-end deep learning framework (by Google) with support for building, training, and deploying neural networks at scale, including on mobile/edge devices. | Image recognition, NLP, production-scale deep learning pipelines, deployment via TensorFlow Serving/TF Lite. |
| **PyTorch** | Deep learning framework (by Meta) known for its dynamic computation graph and Pythonic, research-friendly API. | Research prototyping, computer vision, NLP, generative AI — currently the dominant framework in ML research and increasingly in production. |

## Notes
- NumPy and Pandas are used in almost every data project, regardless of
  whether classical ML or deep learning is involved — they form the data
  layer.
- Scikit-learn is the go-to choice for classical/tabular ML problems where
  the dataset is small-to-medium sized and interpretability matters.
- TensorFlow and PyTorch are used when the problem requires deep neural
  networks (large datasets, images, text, audio); PyTorch tends to be
  favored for research/experimentation, TensorFlow for large-scale
  production deployment, though both have converged in capability over
  time.
