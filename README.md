# MCN-group-8
khởi tạo instance work = binaryCompress(link ảnh, số lần nén)
  - mỗi instance có 1 mảng pixel - đại diện cho ảnh, sau khi decode encode đây vẫn là nơi lưu ảnh kết quả 
  - một mảng differences chứa các mảng lưu sự thay đổi khi thực thi encode

work.encode()
  - mảng pixel của ảnh được bỏ đi những điểm ảnh qua "số lần nén" bước
  - mảng differences được thêm vào 1 mảng lưu thay đổi, qua từng lần nén

work.decode()
  - mảng pixel của ảnh được khôi phục từ mảng differences + img cuối cùng

work.save_result_image() để lưu ảnh ra xem kết quả
