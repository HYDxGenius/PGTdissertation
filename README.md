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
1.**Start WebUI**


![Start webui](https://github.com/user-attachments/assets/80a557ba-7ce4-4f65-8a3a-d9aa750401df)


2.**Do fine tuning traning**

![traning1](https://github.com/user-attachments/assets/364552af-f1e3-4eff-ba7b-b248f3585208)
![traning2](https://github.com/user-attachments/assets/cc2120cc-fab2-4d0a-a40c-dbb8adf4821a)
![traning3](https://github.com/user-attachments/assets/ecd537f1-fde6-422c-9521-6a8ba12e9f67)


3.**Load checkpoint to evaulate, set max token to 1**

![eval1](https://github.com/user-attachments/assets/cb069660-71eb-4305-8e63-44d610e68a8c)
![eval2](https://github.com/user-attachments/assets/da3f9395-0cc9-49cc-9dbd-a2e6989cc55a)
![eval3](https://github.com/user-attachments/assets/10e33f86-72cc-46da-897b-21a90712bf8d)


4.**Test Chatbot**
![chat](https://github.com/user-attachments/assets/cd9b7941-c904-4ff9-8373-1a309a9aa9d5)



5.**Export Model**

![model](https://github.com/user-attachments/assets/13f9e096-cda0-48f1-8030-c74afec4daf5)



6.**Load Model and chat**
![chat2](https://github.com/user-attachments/assets/28983f9e-a3fb-40bf-8f17-1758348db6b7)


7.**Use the new model to evaluate Nazario dataset, it does good**
![eval_model](https://github.com/user-attachments/assets/fb01f32a-6e16-4789-b19b-e681c0d7d57b)


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
