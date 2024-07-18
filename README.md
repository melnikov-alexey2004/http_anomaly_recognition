This repa was built using [Lukashab]([https://pages.github.com/](https://github.com/Lukashab/http_anomaly_detection)).

# **HTTP Anomaly Detection Classifier**
## Introduction
> The classifier uses HTTP DATASET CSIC 2010 to train the model for detection of malicious HTTP requests. For this purpose, the One Class SVM model is used with "rbf" kernel and appropriate feature extraction methods in order to obtain sufficient results.

### Feature extraction **CSIC2010**
> I got inspired by [1] and [2] and chose some of the feature extraction methods mentioned in these papers in order to obtain the best results.

# Conclusion
## Results
> Given HTTP DATASET CSIC 2010, classifier was evaluated as follows:

The background color is `#ffffff` for light mode and `#000000` for dark mode.

Test Anomalous dataset: precision 94.45%
Test Normal dataset: precision 82.71%
## Possible improvements
With correctly chosen parameters, classifier showed sufficient results for anomaly detection, however, there is still a lot to improve.
With growing amount of data, SVM model grows with amount of support vectors, which also causes problems in performance. To reduce the time of computation, multilayer perceptron models (ANN) seems like a good option (since their "trained" weights are of fixed size and do not grow with data).

# Literature
Althubiti, Sara A.. “Analyzing HTTP requests for web intrusion detection.” (2017).
Epp, Nico & Funk, Ralf & Cappo, Cristian. (2017). Anomaly-based Web Application Firewall using HTTP-specific features and One-Class SVM.

- [x] #739
- [ ] https://github.com/octo-org/octo-repo/issues/740
- [ ] Add delight to the experience when all tasks are complete :tada:
- [ ] \(Optional) Open a followup issue

Here is a simple footnote[^1].

A footnote can also have multiple lines[^2].

[^1]: My reference.
[^2]: To add line breaks within a footnote, prefix new lines with 2 spaces.
  This is a second line.




> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.


<!-- This content will not appear in the rendered Markdown -->
Let's rename \*our-new-project\* to \*our-old-project\*.
