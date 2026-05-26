shop_name =""
product_category = ""
keyword_list = ""
product_description = ""
product_name = ""
hastag = ""
while True:
    check_decision = input("+================================================================+\n"
                      "|              HỆ THỐNG QUẢN LÝ NỘI DUNG SẢN PHẨM SHOPEE         |\n"
                      "+================================================================+\n"
                      "|        1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê        |\n"
                      "|        2. Chuẩn hóa tên shop                                   |\n"
                      "|        3. Kiểm tra mã giảm giá hợp lệ                          |\n"
                      "|        4. Tìm kiếm và thay thế từ khóa trong mô tả sản phẩm    |\n"
                      "|        5. Thoát chương trình                                   |\n"
                      "+================================================================+\n"
                      "> Mời bạn chọn chức năng(1-5): "
                      )
    if check_decision == "" or check_decision.isalpha():
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
    else:
        decision = int(check_decision)
        match decision:
            case 1:
                count = 0
                while True:
                    shop_name = input("Nhập vào tên shop: ").strip()
                    if shop_name == "":
                        print("Tên shop không được để trống")
                    else:
                        break
                while True:
                    product_name = input ("Nhập vào tên sản phẩm: ").strip().title()
                    if product_name!="":
                        count+=1
                        break
                    else:
                        print("Đang không có sản phẩm nào")
                        break
                if count > 0:
                    while True:
                        product_description = input("Nhập vào mô tả sản phẩm: ").strip()
                        if product_description =="":
                            print("Mô tả sản phẩm không được trống")
                        else:
                            break
                    product_category = input("Danh mục sản phẩm: ").strip().lower()
                    keyword_list  = input("Danh sách từ khóa tìm kiếm(cách nhau bởi dấu phẩy): ").strip()
                    print("====     Báo cáo thống kê    ====\n"
                        f"Tên shop sau khi loại bỏ khoảng trắng đầu và cuối: {shop_name}\n"
                        f"Tên sản phẩm sau khi loại bỏ khoảng trắng đầu và cuối, viết hoa chữ cái đầu mỗi từ: {product_name}\n"
                        f"Mô tả sản phẩm sau khi loại bỏ khoảng trắng đầu và cuối: {product_description}\n"
                        f"Độ dài mô tả sản phẩm: {len(product_description)}\n"
                        f"Danh mục sản phẩm sau khi chuẩn hóa khoảng trắng, chuyển hoá thành chữ thường: {product_category}\n"
                        f"Danh sách từ khóa sau khi chuẩn hóa khoảng trắng: {keyword_list}\n"
                        f"Số lượng từ khóa tìm kiếm: {len(keyword_list.split(","))}\n"
                        f"Mô tả sản phẩm được chuyển toàn bộ sang chữ thường: {product_description.lower()}\n"
                        f"Mô tả sản phẩm được chuyển toàn bộ sang chữ hoa: {product_description.upper()}\n"
                        )
            case 2:
                print(f"Tên shop ban đầu: {shop_name}")
                print(f"Tên shop sau khi được chuẩn hóa: {"shop-"+shop_name.lower().replace(" ","-")}")
            case 3:
                while True:
                    discount_code = input("Nhập vào một mã giảm giá: ").strip().upper()
                    if discount_code == "":
                        print("Mã giảm giá không được rỗng")
                    elif " " in discount_code:
                        print("Mã giảm giá không được chứa khoảng trắng")
                    elif not discount_code.startswith("SALE"):
                        print("Mã giảm giá phải bắt đầu bằng chuỗi SALE")
                    elif len(discount_code) < 6 or len(discount_code) > 12:
                        print("Mã giảm giá phải có độ dài từ 6 đến 12 ký tự")
                    elif not discount_code.isalnum():
                        print("Mã giảm giá chỉ được chứa chữ cái và chữ số")
                    else:
                        print("Mã giảm giá hợp lệ")
                        hastag += f"{discount_code}\n"
                        print("Danh sách mã giảm giá hiện tại\n"
                            f"{hastag}"
                            )
                        break
            case 4:
                count = 0
                find_keyword = input("Nhập vào từ khóa cần tìm trong mô tả sản phẩm: ")
                replace_keyword = input("Nhập vào từ kháo thay thế: ")
                count = product_description.count(find_keyword)
                if count ==0:
                    print("Không tìm thấy từ khóa cần tìm")
                else:
                    print(f"Mô tả sản phẩm hiện tại: {product_description}")
                    product_description = product_description.replace(find_keyword,replace_keyword)
                    print(f"Mô tả sau khi thay thế: {product_description}")
                    print(f"Số lần xuất hiện của từ khóa: {count}")
            case 5:
                print("Thoát chương trình")
                break
            case _:
                print("Lựa chọn không hợp lệ")

'''
Các vấn đề và cách giải quyết:
    Bẫy 1 — Tên Shop rỗng
        sau khi dung strip cho biến lưu trữ tên shop. dùng if-else để so biến với "" nếu rỗng thì cho người dùng nhập lại
    Bẫy 2 — Nhập mô tả sản phẩm rỗng hoặc chỉ chứa khoảng trắng
        sau khi dung strip cho biến lưu trữ mô tả sản phẩm. dùng if-else để so biến với "" nếu rỗng thì cho người dùng nhập lại
        chỉ cho nhập mô tả sản phẩm khi đã nhập sản phẩm nếu sản phẩm trống thì in ra sản phảm trống và kết thúc nhập liệu
    Bẫy 3 — Nhập lựa chọn menu không hợp lệ
        sử dụng trường hợp case _ trong case- when để giải quyết vấn đề này
    Bẫy 4 — Nhập lựa chọn menu không phải là số
        Sử dụng isalpha kết hợp if-else 
'''