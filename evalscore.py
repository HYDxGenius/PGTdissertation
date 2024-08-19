import json
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def load_data_from_json(file_path):
    labels = []
    predictions = []
    invalid_predictions = []

    with open(file_path, 'r') as file:
        for line in file:
            data = json.loads(line)
            label = data['label']
            predict = data['predict']
            labels.append(label)
            if predict in ['spam', 'ham']:
                predictions.append(predict)
            else:
                predictions.append('invalid')  # 将无效预测标记为'invalid'
                invalid_predictions.append(data)
    
    return labels, predictions, invalid_predictions

def calculate_metrics(labels, predictions):
    # 去掉无效预测的样本
    valid_labels = [label for label, pred in zip(labels, predictions) if pred != 'invalid']
    valid_predictions = [pred for pred in predictions if pred != 'invalid']
    
    accuracy = accuracy_score(valid_labels, valid_predictions)
    precision = precision_score(valid_labels, valid_predictions, pos_label='spam')
    recall = recall_score(valid_labels, valid_predictions, pos_label='spam')
    f1 = f1_score(valid_labels, valid_predictions, pos_label='spam')
    
    return accuracy, precision, recall, f1

def main():
    file_path = 'C:\\Users\\76922\Desktop\\dissertation\\LLaMA-Factory\\src\\saves\\LLaMA3-8B-Chat\\lora\\eval_5e5_enron\generated_predictions.jsonl'  # 替换为你的JSON文件路径
    labels, predictions, invalid_predictions = load_data_from_json(file_path)
    
    accuracy, precision, recall, f1 = calculate_metrics(labels, predictions)
    
    print(f'Accuracy: {accuracy:.4f}')
    print(f'Precision: {precision:.4f}')
    print(f'Recall: {recall:.4f}')
    print(f'F1 Score: {f1:.4f}')
    
    if invalid_predictions:
        print(f'Invalid Predictions: {len(invalid_predictions)}')
        print(invalid_predictions)

if __name__ == '__main__':
    main()
