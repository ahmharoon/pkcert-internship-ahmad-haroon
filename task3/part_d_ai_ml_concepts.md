# Part D – Introduction to AI & Machine Learning

## 1. Define Artificial Intelligence
Artificial Intelligence (AI) is the branch of computer science concerned
with building systems that can perform tasks that normally require human
intelligence — reasoning, learning, perception, language understanding, and
decision-making. AI is the broadest umbrella term; it includes everything
from simple rule-based expert systems to modern neural networks.

## 2. AI vs Machine Learning vs Deep Learning
These three terms are often used interchangeably but describe nested
concepts:

```
Artificial Intelligence (AI)
  └── Machine Learning (ML)
        └── Deep Learning (DL)
```

- **AI** — the overall goal: making machines behave intelligently. Can be
  achieved with hand-coded rules (no learning involved at all), e.g. a
  chess engine using pre-programmed heuristics.
- **Machine Learning (ML)** — a subset of AI where systems *learn patterns
  from data* instead of following explicit rules, and improve with
  experience. Example: a spam filter that learns from labeled emails.
- **Deep Learning (DL)** — a subset of ML that uses multi-layered artificial
  neural networks to automatically learn hierarchical feature
  representations from large amounts of data. Example: image recognition
  using a Convolutional Neural Network (CNN).

| | AI | ML | DL |
|---|---|---|---|
| Scope | Broadest | Subset of AI | Subset of ML |
| Approach | Rules or learning | Learns from data | Learns via layered neural nets |
| Data need | Varies | Moderate | Very large |
| Example | Chess engine | Spam filter | Face recognition |

## 3. Supervised, Unsupervised, and Reinforcement Learning

- **Supervised Learning:** The model learns from *labeled* data — each
  training example has a known input and correct output. The goal is to
  learn a mapping from input to output.
  - Example: predicting house prices from features like size and location,
    given historical sales data with known prices (regression); or
    classifying emails as "spam"/"not spam" given labeled examples
    (classification).

- **Unsupervised Learning:** The model learns from *unlabeled* data and
  tries to find hidden structure or patterns on its own.
  - Example: customer segmentation — grouping customers into clusters based
    on purchasing behavior without predefined categories (clustering, e.g.
    K-Means).

- **Reinforcement Learning:** An *agent* learns by interacting with an
  *environment*, taking actions and receiving *rewards* or *penalties*. The
  goal is to learn a policy that maximizes cumulative reward over time.
  - Example: an AI agent learning to play a video game or a robot learning
    to walk, improving its strategy through trial and error.

## 4. The Machine Learning Pipeline
A typical ML project follows these stages:

1. **Problem Definition** — clarify the business/research question and
   what "success" looks like.
2. **Data Collection** — gather raw data from databases, APIs, sensors, etc.
3. **Data Cleaning & Preprocessing** — handle missing values, remove
   duplicates/outliers, encode categorical variables, normalize/scale
   numeric features.
4. **Exploratory Data Analysis (EDA)** — visualize and summarize the data to
   understand distributions, correlations, and potential issues.
5. **Feature Engineering** — create or select the most informative input
   features for the model.
6. **Train/Test Split** — divide data into training and testing (and often
   validation) sets to evaluate generalization.
7. **Model Selection & Training** — choose an algorithm (e.g. linear
   regression, decision tree, neural network) and fit it on the training
   data.
8. **Evaluation** — measure performance on the test set using metrics such
   as accuracy, precision/recall, RMSE, etc.
9. **Hyperparameter Tuning** — adjust model settings (e.g. learning rate,
   tree depth) to improve performance, often via cross-validation.
10. **Deployment** — integrate the trained model into a real application or
    service.
11. **Monitoring & Maintenance** — track the model's performance over time
    and retrain as new data arrives ("model drift").
