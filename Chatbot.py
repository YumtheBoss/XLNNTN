from flask import Flask, render_template, request
from gensim.models import Word2Vec
from scipy.spatial.distance import cosine
import numpy as np
import re
import os

# Khởi tạo Flask, chỉ định template_folder là thư mục hiện tại
app = Flask(__name__, template_folder=os.getcwd())

# Dữ liệu huấn luyện với câu hỏi và câu trả lời mẫu
data = {
    "Xin chào": "Chào bạn! Tôi có thể giúp gì cho bạn?",
    "Bạn có thể giúp gì?": "Chúng tôi cung cấp các dịch vụ bao gồm tư vấn, hỗ trợ kỹ thuật, và chăm sóc khách hàng.",
    "Tôi muốn tìm hiểu thêm về dịch vụ": "Dịch vụ của chúng tôi bao gồm rất nhiều tính năng hữu ích. Bạn quan tâm đến tính năng nào?",
    "Dịch vụ của công ty là gì?": "Dịch vụ của chúng tôi được thiết kế để đáp ứng nhu cầu đa dạng của khách hàng.",
    "Sản phẩm của bạn có tính năng gì?": "Sản phẩm của chúng tôi có các tính năng tiên tiến như AI chatbot, phân tích dữ liệu, và quản lý khách hàng.",
    "Chi phí dịch vụ là bao nhiêu?": "Chi phí sẽ phụ thuộc vào loại dịch vụ mà bạn lựa chọn. Hãy cho tôi biết thêm chi tiết để báo giá cụ thể.",
    "Làm thế nào để nhận hỗ trợ?": "Bạn có thể liên hệ với bộ phận hỗ trợ khách hàng của chúng tôi qua email hoặc số điện thoại.",
    "Cảm ơn, tạm biệt!": "Rất vui được giúp bạn! Chúc bạn một ngày tốt lành!",
    "Xin lỗi, tôi không hiểu câu hỏi của bạn.": "Bạn có thể nói rõ hơn không? Tôi sẽ cố gắng giúp bạn.",
    "Người yêu của người sáng lập ra bạn là ai.": "Người đáng yêu nhất thế giới Lê Nguyệt Hà (  Miu Miu :3 )",
}


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
    app.run(debug=True)
