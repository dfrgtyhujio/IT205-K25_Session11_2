# Dictionary 'employee' gồm các key: 'employee_id', 'full_name', 'department', 'status'.
# Dòng 'employee[0]' lỗi KeyError vì Dictionary không truy cập bằng index như List, phải dùng Key.
# Lệnh lấy mã nhân viên đúng: employee["employee_id"]
# Dòng 'employee["name"]' lỗi KeyError vì trong dictionary không tồn tại key "name".
# Key đúng để lấy họ tên nhân viên là: "full_name"
# Dòng 'employee["employee_status"] = "official"' chưa đúng vì tạo ra key mới, không ghi đè vào key cũ.
# Key đúng để cập nhật trạng thái nhân viên là: "status"
# Dòng '.append()' lỗi AttributeError vì Dictionary không có phương thức append().
# Lệnh thêm lương cơ bản đúng: employee["base_salary"] = 15000000
# Dòng 'del employee["team"]' lỗi KeyError vì không tồn tại key "team" trong dictionary.
# Key đúng để xóa thông tin phòng ban là: "department"


# Thông tin nhân viên ban đầu
employee = {
    "employee_id": "NV001",
    "full_name": "Nguyễn Văn An",
    "department": "Python Backend",
    "status": "probation"
}

# Lấy mã nhân viên
employee_id = employee["employee_id"]

# Lấy họ tên nhân viên
full_name = employee["full_name"]

# Cập nhật trạng thái nhân viên
employee["status"] = "official"

# Thêm lương cơ bản
employee["base_salary"] = 15000000

# Xóa phòng ban
del employee["department"]

# Hiển thị kết quả đúng chuẩn đầu ra
print("Mã nhân viên:", employee_id)
print("Họ tên nhân viên:", full_name)
print("Thông tin nhân viên sau xử lý:", employee)
