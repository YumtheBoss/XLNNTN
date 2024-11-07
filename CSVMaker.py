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
    ("Dịch vụ của công ty gồm các tính năng nào?",
     "Chúng tôi có các tính năng như tư vấn, hỗ trợ kỹ thuật và chăm sóc khách hàng."),
    ("Dịch vụ của công ty đáp ứng nhu cầu gì?", "Dịch vụ của chúng tôi phù hợp với nhu cầu đa dạng của khách hàng."),

    # Câu hỏi về thông tin công ty
    ("Công ty của bạn làm gì?", "Chúng tôi chuyên về phát triển phần mềm và giải pháp công nghệ."),
    ("Công ty cung cấp giải pháp gì?", "Chúng tôi cung cấp các giải pháp tối ưu cho doanh nghiệp và cá nhân."),

    # Câu hỏi về tính năng sản phẩm
    ("Sản phẩm của bạn có tính năng gì?", "Sản phẩm có AI chatbot, phân tích dữ liệu và quản lý khách hàng."),
    ("Các tính năng chính của sản phẩm là gì?",
     "Các tính năng chính gồm quản lý khách hàng, phân tích dữ liệu và báo cáo chi tiết."),

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
    ("Câu hỏi chưa rõ ràng.", "Mong bạn nói chi tiết hơn để tôi có thể hỗ trợ."),

    # Câu hỏi về bộ phim nổi tiếng
    ("Phim nào được yêu thích nhất trong năm 2023?",
     "Một trong những bộ phim được yêu thích nhất là 'Avatar: The Way of Water'."),
    ("Bộ phim nào thắng giải Oscar năm 2023?", "'Everything Everywhere All at Once' đã giành giải Oscar năm 2023."),
    ("Bạn có biết về bộ phim 'Oppenheimer' không?",
     "'Oppenheimer' là bộ phim do Christopher Nolan đạo diễn, ra mắt năm 2023."),
    ("Phim 'Barbie' nói về cái gì?",
     "'Barbie' là bộ phim hài hước của Greta Gerwig, kể về cuộc phiêu lưu của Barbie trong thế giới thực."),
    ("Bộ phim nào có doanh thu cao nhất năm 2023?", "Bộ phim có doanh thu cao nhất năm 2023 là 'Barbie'."),
    ("Phim hành động nào bạn khuyên xem trong năm qua?",
     "'John Wick: Chapter 4' là một bộ phim hành động hấp dẫn trong năm 2023."),

    # Câu hỏi về bài hát nổi tiếng
    ("Bài hát nào nổi bật trong năm 2023?",
     "Bài hát 'Flowers' của Miley Cyrus là một trong những ca khúc nổi bật nhất năm 2023."),
    ("Ai là ca sĩ hát bài 'Shivers'?", "'Shivers' là bài hát của ca sĩ Ed Sheeran."),
    ("Bạn biết bài hát nào của Taylor Swift?",
     "Taylor Swift đã phát hành nhiều bài hát nổi tiếng, một trong số đó là 'Anti-Hero' vào năm 2023."),
    ("Bài hát nào của The Weeknd được yêu thích nhất?",
     "'Blinding Lights' của The Weeknd là một trong những bài hát nổi tiếng và được yêu thích nhất."),
    ("Bài hát nào nổi bật trong thể loại pop?",
     "'As It Was' của Harry Styles là một trong những bài hát pop nổi bật trong năm qua."),
    ("Bài hát nào đạt được nhiều lượt nghe nhất trên Spotify?",
     "'Blinding Lights' của The Weeknd là bài hát đạt được nhiều lượt nghe nhất trên Spotify."),
    ("Bài hát nào của BTS bạn biết?", "BTS có rất nhiều bài hát nổi tiếng, một trong số đó là 'Dynamite'."),

    # Câu hỏi về anime nổi tiếng
    ("Anime nào nổi bật nhất trong những năm gần đây?",
     "'Demon Slayer: Kimetsu no Yaiba' là một trong những anime nổi bật trong 6 năm qua."),
    ("'Attack on Titan' kết thúc khi nào?",
     "'Attack on Titan' đã kết thúc vào năm 2023 với phần cuối cùng của câu chuyện."),
    ("Anime nào về đề tài siêu anh hùng nổi bật gần đây?",
     "'My Hero Academia' là một anime siêu anh hùng rất được yêu thích trong những năm gần đây."),
    ("Câu chuyện của 'Jujutsu Kaisen' là gì?",
     "'Jujutsu Kaisen' là một anime về các pháp sư chiến đấu chống lại những linh hồn tà ác."),
    ("Anime nào được chuyển thể từ manga nổi tiếng trong 2023?",
     "'Tokyo Revengers' là một anime được chuyển thể từ manga nổi tiếng, đã thu hút sự chú ý trong năm 2023."),
    ("Anime nào được xem nhiều nhất trên Crunchyroll năm 2022?",
     "'Demon Slayer' tiếp tục là một trong những anime được xem nhiều nhất trên Crunchyroll trong năm 2022."),

    # Câu hỏi về tiểu thuyết và sách về chính trị
    ("Cuốn sách '1984' của George Orwell nói về điều gì?",
     "'1984' của George Orwell là một tác phẩm nói về xã hội kiểm soát toàn diện và những ảnh hưởng của chính phủ độc tài."),
    ("Sách 'The Prince' của Machiavelli nói về gì?",
     "'The Prince' là cuốn sách nổi tiếng của Niccolò Machiavelli, bàn về chiến lược chính trị và cách thức duy trì quyền lực."),
    ("Ai là tác giả của cuốn sách 'The Communist Manifesto'?",
     "'The Communist Manifesto' được viết bởi Karl Marx và Friedrich Engels."),
    ("Cuốn sách nào của Thomas Hobbes bàn về quyền lực?",
     "'Leviathan' của Thomas Hobbes là một tác phẩm nổi tiếng, bàn về quyền lực và lý thuyết chính trị."),
    ("Ai là tác giả của cuốn sách 'Capital in the Twenty-First Century'?",
     "'Capital in the Twenty-First Century' là cuốn sách của Thomas Piketty, bàn về sự bất bình đẳng kinh tế."),

    # Câu hỏi về sách học máy và công nghệ IT
    ("Sách 'Deep Learning' của Ian Goodfellow nói về gì?",
     "'Deep Learning' của Ian Goodfellow là cuốn sách nổi tiếng trong lĩnh vực học sâu (deep learning), với các lý thuyết và ứng dụng của mạng nơ-ron."),
    ("Cuốn sách 'Machine Learning Yearning' của Andrew Ng nói về điều gì?",
     "'Machine Learning Yearning' là cuốn sách của Andrew Ng, hướng dẫn cách xây dựng các hệ thống học máy thành công."),
    ("Sách nào là tài liệu tham khảo nổi tiếng trong học máy?",
     "'Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow' là một cuốn sách phổ biến trong việc học và ứng dụng học máy."),
    ("Cuốn sách 'Clean Code' của Robert C. Martin nói về điều gì?",
     "'Clean Code' là cuốn sách nổi tiếng của Robert C. Martin, bàn về việc viết mã nguồn sạch và dễ bảo trì."),
    ("Cuốn sách 'Artificial Intelligence: A Modern Approach' là của tác giả nào?",
     "'Artificial Intelligence: A Modern Approach' là cuốn sách nổi tiếng của Stuart Russell và Peter Norvig, đề cập đến các lý thuyết và ứng dụng của trí tuệ nhân tạo."),

# Câu hỏi về công thức nấu ăn
    ("Công thức nấu canh rau muống?", "Để nấu canh rau muống, bạn cần có rau muống, tỏi, gia vị như muối, đường, nước mắm. Đun nước sôi, cho tỏi vào phi thơm, sau đó cho rau muống vào nấu chín."),
    ("Cách làm món trứng chiên?", "Để làm trứng chiên, bạn cần trứng, dầu ăn và gia vị như muối, tiêu. Đánh trứng với gia vị rồi chiên trên chảo nóng cho đến khi chín vàng."),
    ("Món gỏi cuốn làm như thế nào?", "Để làm gỏi cuốn, bạn cần bánh tráng, tôm, bún, rau sống, gia vị và nước mắm chua ngọt. Cuốn tất cả nguyên liệu lại và ăn kèm với nước mắm."),
    ("Công thức làm bánh mì đơn giản?", "Để làm bánh mì, bạn cần bột mì, men nở, nước ấm, đường, muối. Trộn nguyên liệu, ủ bột, rồi nướng trong lò."),
    ("Cách làm sinh tố dưa hấu?", "Để làm sinh tố dưa hấu, bạn cần dưa hấu, sữa tươi và đá viên. Cho tất cả vào máy xay sinh tố và xay nhuyễn."),
]

# Chuyển dữ liệu thành DataFrame
df = pd.DataFrame(data, columns=["question", "answer"])

# Lưu DataFrame vào file CSV
df.to_csv("data.csv", index=False, encoding="utf-8-sig")

print("File CSV đã được tạo thành công.")
