# Nhập số giờ làm mỗi tuần
so_gio_lam = float(input("Nhập số giờ làm mỗi tuần: "))

# Nhập thù lao trên mỗi giờ làm tiêu chuẩn
luong_gio = float(input("Nhập thù lao trên mỗi giờ làm tiêu chuẩn: "))

gio_tieu_chuan = 44  # Số giờ làm chuẩn mỗi tuần

# Tính số giờ làm vượt chuẩn mỗi tuần, đảm bảo không âm
gio_vuot_chuan = max(0, so_gio_lam - gio_tieu_chuan)

# Tính tổng thu nhập, với giờ vượt chuẩn được tính gấp 1.5 lần
thuc_linh = gio_tieu_chuan * luong_gio + gio_vuot_chuan * luong_gio * 1.5

# In tổng tiền thực lĩnh của nhân viên
print(f"Số tiền thực lĩnh của nhân viên: {thuc_linh}")