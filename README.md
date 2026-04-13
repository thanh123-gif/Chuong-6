📘 XÂY DỰNG MINI SEARCH ENGINE SỬ DỤNG INVERTED INDEX
I. TÓM TẮT YÊU CẦU ĐỀ BÀI
Bài toán
Xây dựng một chương trình tìm kiếm tài liệu sử dụng Inverted Index.
(a) CreateIndex(Dir, StopList)
Input:
- Dir: thư mục chứa các file document 
- StopList: file chứa stopwords 
Output:
- DocTable: danh sách document (id → tên file) 
- TermTable (Inverted Index): 
term → {doc_id: frequency}
Điều kiện:
❌ Bỏ file stoplist 
❌ Bỏ stopwords 
✅ Chỉ lấy từ bắt đầu bằng chữ C/c 
(b) Find(Word, Weight, N)
Input:
- 1 từ (word) 
- trọng số (weight) 
- số lượng kết quả (N) 
Output:
- Top N document liên quan 
Công thức:
score = frequency × weight
(c) Find(WordFile, N)
Input:
- file chứa nhiều dòng: 
word weight
Output:
- Top N document 
Công thức:
score = tổng(freq × weight) của tất cả từ
1. Giới thiệu
Trong các hệ thống tìm kiếm hiện đại, việc truy xuất thông tin nhanh và chính xác là rất quan trọng. Một trong những kỹ thuật cốt lõi được sử dụng là Inverted Index (chỉ mục đảo), giúp tìm kiếm tài liệu nhanh chóng mà không cần duyệt toàn bộ dữ liệu.
Đề tài này xây dựng một hệ thống tìm kiếm đơn giản dựa trên inverted index, hỗ trợ tìm kiếm theo từ khóa và xếp hạng kết quả.
2. Mục tiêu
Xây dựng Inverted Index từ tập tài liệu
Loại bỏ từ không cần thiết bằng StopList
Chỉ lấy các từ bắt đầu bằng chữ C
Cài đặt các hàm:
Tìm kiếm 1 từ
Tìm kiếm nhiều từ có trọng số
Xếp hạng tài liệu theo mức độ liên quan
3. Phương pháp
3.1 Tiền xử lý dữ liệu
Mỗi tài liệu được xử lý qua các bước:
Tách từ (Tokenization)
Chia văn bản thành các từ riêng lẻ
Loại bỏ Stopwords
Ví dụ: "is", "the", "and",...
Lọc từ
Chỉ giữ các từ bắt đầu bằng chữ C/c
3.2 Xây dựng Inverted Index
Inverted Index có dạng:
từ → {doc_id: số lần xuất hiện}
Ví dụ:
coffee → {2:1, 3:1}
cats → {1:1, 3:1}
Ý nghĩa:
"coffee" xuất hiện ở doc2 và doc3
"cats" xuất hiện ở doc1 và doc3
3.3 Cấu trúc dữ liệu
DocTable: ánh xạ ID → tên file
{1: doc1.txt, 2: doc2.txt, 3: doc3.txt}
TermTable (Inverted Index):
lưu thông tin từ khóa và các document chứa nó
4. Thuật toán tìm kiếm
4.1 Find(Word, Weight, N)
Đầu vào:
Từ khóa (Word)
Trọng số (Weight)
Số kết quả cần lấy (N)
Công thức:
score = frequency × weight
Kết quả được sắp xếp theo score giảm dần.
4.2 Find(WordFile, N)
File đầu vào có dạng:
word weight
Ví dụ:
computer 2
cats 3
coffee 1
Công thức:
score = tổng (frequency × weight)
4.3 TF-IDF (mở rộng)
Trong demo web, sử dụng công thức:
score = tf × log(N / df)
Trong đó:
tf: số lần từ xuất hiện
df: số document chứa từ
N: tổng số document
→ Giúp xếp hạng chính xác hơn
5. Quy trình hoạt động
Tài liệu
   ↓
Tách từ
   ↓
Loại stopwords
   ↓
Lọc chữ C
   ↓
Tạo inverted index
   ↓
Nhận truy vấn
   ↓
Tính score
   ↓
Sắp xếp kết quả

6. Kết quả thực nghiệm
Ví dụ Inverted Index
cats → {1:1, 3:1}
coffee → {2:1, 3:1}
coding → {2:1, 3:1}
Ví dụ truy vấn
Query:
cats coffee
Kết quả:
Document	Score
doc3	2
doc1	1
doc2	1

7. Ưu điểm
Tìm kiếm nhanh nhờ inverted index
Loại bỏ nhiễu bằng stoplist
Có xếp hạng kết quả (score)
Dễ mở rộng
8. Hạn chế
Chỉ hỗ trợ từ bắt đầu bằng chữ C (theo đề bài)
Chưa xử lý ngữ nghĩa (semantic)
Cần rebuild index khi dữ liệu thay đổi
9. Hướng phát triển
Bỏ giới hạn chữ C
Tìm kiếm gần đúng (fuzzy search)
Gợi ý từ khóa (autocomplete)
Dùng database (MongoDB, Elasticsearch)
Ứng dụng AI để hiểu ngữ nghĩa
10. Kết luận
Hệ thống đã xây dựng thành công inverted index và áp dụng vào tìm kiếm tài liệu. Nhờ đó, việc truy xuất dữ liệu trở nên nhanh chóng và hiệu quả hơn so với phương pháp duyệt tuần tự.
11. Tổng kết
Inverted Index → Tìm nhanh
Stoplist → Lọc nhiễu
Score → Xếp hạng
