

from gensim.models import Word2Vec
import numpy as np
from scipy.spatial.distance import cosine
import re

# Dữ liệu hội thoại mẫu để huấn luyện
data = [
    "Xin chào",
    "Bạn có thể giúp gì?",
    "Tôi muốn tìm hiểu thêm về dịch vụ",
    "Dịch vụ của chúng tôi bao gồm rất nhiều tính năng hữu ích.",
    "Bạn có thể cho tôi biết thêm thông tin?",
    "Cảm ơn, tạm biệt!"
]

# Hàm tách từ đơn giản (tokenize) không sử dụng nltk
def simple_tokenize(sentence):
    # Chuyển tất cả về chữ thường và tách từ bằng các ký tự không phải chữ cái
    return re.findall(r'\b\w+\b', sentence.lower())

# Chuẩn bị dữ liệu đầu vào
tokenized_sentences = [simple_tokenize(sentence) for sentence in data]

# Huấn luyện mô hình Word2Vec
model = Word2Vec(tokenized_sentences, vector_size=100, window=5, min_count=1, sg=1)

# Hàm chuyển câu thành vector
def sentence_vector(sentence, model):
    words = simple_tokenize(sentence)
    vectors = [model.wv[word] for word in words if word in model.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(model.vector_size)

# Hàm tìm câu trả lời phù hợp nhất
def find_best_response(user_input, responses, model):
    user_vec = sentence_vector(user_input, model)
    best_response = None
    best_similarity = float('inf')

    for response in responses:
        response_vec = sentence_vector(response, model)
        similarity = cosine(user_vec, response_vec)
        if similarity < best_similarity:
            best_similarity = similarity
            best_response = response

    return best_response

# Danh sách các câu trả lời mẫu
responses = [
    "Chào bạn!",
    "Tôi có thể giúp gì?",
    "Dịch vụ của chúng tôi bao gồm rất nhiều tính năng hữu ích.",
    "Rất vui được hỗ trợ bạn!",
    "Cảm ơn bạn, hẹn gặp lại!"
]

# Hàm chính của chatbot
def chatbot():
    print("Chatbot sẵn sàng! Nhập 'thoát' hoặc 'exit' để kết thúc.")
    while True:
        user_input = input("Bạn: ")
        if user_input.lower() in ['thoát', 'exit']:
            print("Bot: Tạm biệt!")
            break
        response = find_best_response(user_input, responses, model)
        print("Bot:", response)

# Khởi chạy chatbot
if __name__ == "__main__":
    chatbot()
