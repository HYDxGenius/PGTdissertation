# Phishing Email Detection using Llama3 8B

## Overview

This project explores the application of the Llama3 8B model, a state-of-the-art large language model (LLM), for phishing email detection. By leveraging advanced NLP techniques and fine-tuning processes, the project aims to enhance the accuracy and reliability of detecting phishing emails across various datasets.

## Features

- **Fine-Tuning**: The Llama3 8B model is fine-tuned using the UCI SMS Spam Collection, Enron Email, and Nazario datasets.
- **Phishing Detection**: The model is trained to distinguish between spam and legitimate (ham) emails.
- **Evaluation Metrics**: The model’s performance is evaluated using metrics such as ROUGE, Accuracy, Precision, Recall, and F1 Score.
- **Ethical Considerations**: The project includes a comprehensive analysis of ethical issues, such as data privacy and bias in machine learning models.

## Datasets

- **UCI SMS Spam Collection Dataset**: A collection of SMS messages labeled as spam or ham.
- **Enron Email Dataset**: A large collection of emails from the Enron Corporation, labeled for spam detection tasks.
- **Nazario Dataset**: A dataset composed entirely of phishing emails, used primarily for testing the model's ability to detect phishing content.

## Installation

To get started with this project, follow these steps:

1. **Clone the repository from llama-factory and follow its steps to set environment**:
    ```bash
    https://github.com/hiyouga/LLaMA-Factory
    ```

2. **Set up a virtual environment or Server** (optional but recommended, in this project mainly on AutoDL):
    ```bash
    [AutoDL](https://www.autodl.com/home)
    ```

4. **Download the Llama3 8B model**:

## Usage



## Results

The fine-tuned Llama3 8B model achieved the following performance metrics:

- **Nazario Dataset**:
  - ROUGE: 89.77%
  - Accuracy: 89.77%
  - Precision: 1.0000
  - Recall: 89.77%
  - F1 Score: 94.61%

- **UCI Dataset**:
  - ROUGE: 99.40%
  - Accuracy: 99.40%
  - Precision: 98.64%
  - Recall: 96.89%
  - F1 Score: 97.76%

- **Enron Dataset**:
  - ROUGE: 99.40%
  - Accuracy: 99.40%
  - Precision: 99.20%
  - Recall: 99.59%
  - F1 Score: 99.39%

## Ethical Considerations

This project carefully considers the ethical implications of using LLMs for phishing detection. It addresses issues such as data privacy, bias in machine learning models, and the societal impact of deploying such technologies.

## Future Work

Potential areas for further exploration include:

- **Advanced Data Preprocessing**: Incorporating more sophisticated data preprocessing techniques to improve model accuracy.
- **Cross-Dataset Fine-Tuning**: Expanding the model's training to include datasets in different languages or domains.
- **Real-World Deployment**: Integrating the model into real-time email filtering systems or browser plugins.
- **Parameter Optimization**: Further refining the model’s training parameters for enhanced performance.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes or improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

Special thanks to the developers of Llama3, the creators of the datasets used, and the open-source community for providing the tools and resources that made this project possible.
