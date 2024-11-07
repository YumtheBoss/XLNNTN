from flask import Flask, render_template, request
from gensim.models import Word2Vec
from scipy.spatial.distance import cosine
import numpy as np
import pandas as pd
import re
import os

# Khởi tạo Flask
app = Flask(__name__, template_folder=os.getcwd())

# Đọc dữ liệu từ file CSV
def load_data_from_csv(file_path):
    df = pd.read_csv(file_path)
    local_data = dict(zip(df['question'], df['answer']))  # Đổi tên thành local_data
    return local_data


# Đường dẫn đến file CSV chứa dữ liệu câu hỏi và câu trả lời
DATA_FILE = r"C:\Users\Admin\PycharmProjects\XLNNTN\data.csv"
data = load_data_from_csv(DATA_FILE)


# Tách từ đơn giản (tokenize)
def simple_tokenize(sentence):
    return re.findall(r'\b\w+\b', sentence.lower())

# Huấn luyện mô hình Word2Vec
tokenized_sentences = [simple_tokenize(sentence) for sentence in data.keys()]
model = Word2Vec(sentences=tokenized_sentences, vector_size=100, window=5, min_count=1, workers=4)

# Hàm chuyển câu hỏi thành vector
def sentence_to_vector(sentence):
    words = simple_tokenize(sentence)
    word_vectors = [model.wv[word] for word in words if word in model.wv]
    if not word_vectors:
        return np.zeros(model.vector_size)
    return np.mean(word_vectors, axis=0)

# Hàm tìm câu trả lời dựa trên câu hỏi
def get_response(user_input):
    input_vector = sentence_to_vector(user_input)
    min_distance = float('inf')
    best_response = "Xin lỗi, tôi không hiểu câu hỏi của bạn."

    for question, answer in data.items():
        question_vector = sentence_to_vector(question)
        distance = cosine(input_vector, question_vector)
        if distance < min_distance:
            min_distance = distance
            best_response = answer

    return best_response

# Tạo giao diện web
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_input = request.form["msg"]
    response = get_response(user_input)
    return response

if __name__ == "__main__":
    # Tải lại dữ liệu mỗi khi khởi động
    data = load_data_from_csv(DATA_FILE)
    app.run(debug=True)
