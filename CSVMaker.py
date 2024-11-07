import pandas as pd

# Dữ liệu câu hỏi và câu trả lời
data = [
    # Câu chào hỏi
    ("Xin chào", "Chào bạn! Tôi có thể giúp gì cho bạn?"),
    ("Chào bạn! Tôi có thể giúp gì cho bạn?", "Xin chào! Bạn cần hỗ trợ gì không?"),
    ("Rất vui được gặp bạn! Bạn cần hỗ trợ gì không?", "Xin chào! Rất vui được hỗ trợ bạn."),

    # Câu hỏi về dịch vụ
    ("Bạn có thể giúp gì?", "Tôi có thể hỗ trợ bạn về các dịch vụ, sản phẩm và thông tin khác của công ty."),
    ("Tôi muốn tìm hiểu thêm về dịch vụ", "Chúng tôi cung cấp tư vấn, hỗ trợ kỹ thuật, và chăm sóc khách hàng."),
    ("Dịch vụ của bạn bao gồm những gì?", "Chúng tôi có nhiều dịch vụ hữu ích. Bạn quan tâm đến dịch vụ nào?"),
    ("Dịch vụ của công ty gồm các tính năng nào?", "Chúng tôi có các tính năng như tư vấn, hỗ trợ kỹ thuật và chăm sóc khách hàng."),
    ("Dịch vụ của công ty đáp ứng nhu cầu gì?", "Dịch vụ của chúng tôi phù hợp với nhu cầu đa dạng của khách hàng."),

    # Câu hỏi về thông tin công ty
    ("Công ty của bạn làm gì?", "Chúng tôi chuyên về phát triển phần mềm và giải pháp công nghệ."),
    ("Công ty cung cấp giải pháp gì?", "Chúng tôi cung cấp các giải pháp tối ưu cho doanh nghiệp và cá nhân."),

    # Câu hỏi về tính năng sản phẩm
    ("Sản phẩm của bạn có tính năng gì?", "Sản phẩm có AI chatbot, phân tích dữ liệu và quản lý khách hàng."),
    ("Các tính năng chính của sản phẩm là gì?", "Các tính năng chính gồm quản lý khách hàng, phân tích dữ liệu và báo cáo chi tiết."),

    # Câu hỏi về giá cả
    ("Chi phí dịch vụ là bao nhiêu?", "Chi phí phụ thuộc vào dịch vụ bạn chọn. Bạn có thể cho tôi biết thêm chi tiết."),
    ("Dịch vụ có mức giá nào?", "Chúng tôi có các mức giá khác nhau. Bạn quan tâm đến gói nào?"),

    # Câu hỏi về hỗ trợ
    ("Làm thế nào để nhận hỗ trợ?", "Bạn có thể liên hệ với bộ phận hỗ trợ qua email hoặc điện thoại."),
    ("Bộ phận hỗ trợ làm việc như thế nào?", "Chúng tôi có đội ngũ hỗ trợ 24/7 qua nhiều kênh liên hệ."),

    # Câu hỏi cảm ơn và tạm biệt
    ("Cảm ơn, tạm biệt!", "Rất vui được giúp bạn! Chúc bạn một ngày tốt lành!"),
    ("Cảm ơn bạn đã liên hệ!", "Hẹn gặp lại bạn lần sau!"),

    # Câu hỏi không rõ nghĩa
    ("Xin lỗi, tôi không hiểu câu hỏi của bạn.", "Bạn có thể nói rõ hơn không? Tôi sẽ cố gắng giúp bạn."),
    ("Câu hỏi chưa rõ ràng.", "Mong bạn nói chi tiết hơn để tôi có thể hỗ trợ.")
]

# Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(data, columns=["question", "answer"])

# Lưu DataFrame vào file CSV
df.to_csv("data.csv", index=False, encoding="utf-8-sig")

print("File CSV đã được tạo thành công.")
