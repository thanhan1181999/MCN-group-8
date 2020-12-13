# MCN-group-8

XỬ LÝ VỚI ẢNH MÀU XÁM
1. code : binary.py
2. nội dung
khởi tạo instance work = binaryCompress(link ảnh, số lần nén)
  - mỗi instance có 1 mảng pixel - đại diện cho ảnh, sau khi decode encode đây vẫn là nơi lưu ảnh kết quả 
  - một mảng differences chứa các mảng lưu sự thay đổi khi thực thi encode
work.encode()
  - mảng pixel của ảnh được bỏ đi những điểm ảnh qua "số lần nén" bước
  - mảng differences được thêm vào 1 mảng lưu thay đổi, qua từng lần nén
work.decode()
  - mảng pixel của ảnh được khôi phục từ mảng differences + img cuối cùng
work.save_result_image() để lưu ảnh ra xem kết quả

XỬ LÝ VỚI ẢNH MÀU (với 3 điểm ảnh rgb)
  - binary1.py : dịnh nghĩa class xử lý 1 loại điểm ảnh
  - main.py : cập nhật LINK_IMGAE = 'img1.jpg'
                      COMPRESSION_TIMES = 1
              để xem ảnh được nén, và ảnh sau khi khôi phục

RUN

py binary.py
  - trả về ảnh màu xám, sau khi nén 4 lần, và ảnh sau khi giải nén lại  
py main.py
  - trả về ảnh màu, sau khi nén 2 lần, và ảnh sau khi giải nén lại
