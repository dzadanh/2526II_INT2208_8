# Hàm kiểm tra và phân loại tam giác
def classify_triangle(a, b, c):
    # Kiểm tra kiểu dữ liệu và pham vi các cạnh
    if type(a) is not int or type(b) is not int or type(c) is not int:
        return "Invalid Input"
    if a < 1 or a > 100 or b < 1 or b > 100 or c < 1 or c > 100:
        return "Invalid Input"
    # Kiểm tra bất đẳng thức tam giác
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return "Not a Triangle"
    # Phân loại tam giác
    if a == b and b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

# Test case
test_cases = [
    {"id": "TC01", "name": "Biên dưới hợp lệ nhỏ nhất", "input": (1, 1, 1), "expected": "Equilateral"},
    {"id": "TC02", "name": "Biên trên hợp lệ lớn nhất", "input": (100, 100, 100), "expected": "Equilateral"},
    {"id": "TC03", "name": "Cạnh a vi phạm biên dưới", "input": (0, 50, 50), "expected": "Invalid Input"},
    {"id": "TC04", "name": "Cạnh b vi phạm biên dưới", "input": (50, 0, 50), "expected": "Invalid Input"},
    {"id": "TC05", "name": "Cạnh c vi phạm biên dưới", "input": (50, 50, 0), "expected": "Invalid Input"},
    {"id": "TC06", "name": "Cạnh a vi phạm biên trên", "input": (101, 50, 50), "expected": "Invalid Input"},
    {"id": "TC07", "name": "Cạnh b vi phạm biên trên", "input": (50, 101, 50), "expected": "Invalid Input"},
    {"id": "TC08", "name": "Cạnh c vi phạm biên trên", "input": (50, 50, 101), "expected": "Invalid Input"},
    {"id": "TC09", "name": "Không thỏa BĐT tam giác (a+b=c)", "input": (2, 3, 5), "expected": "Not a Triangle"},
    {"id": "TC10", "name": "Không thỏa BĐT tam giác (a+b<c)", "input": (2, 3, 10), "expected": "Not a Triangle"},
    {"id": "TC11", "name": "Tam giác cân tại C (a=b)", "input": (5, 5, 8), "expected": "Isosceles"},
    {"id": "TC12", "name": "Tam giác cân tại A (b=c)", "input": (8, 5, 5), "expected": "Isosceles"},
    {"id": "TC13", "name": "Tam giác cân tại B (a=c)", "input": (5, 8, 5), "expected": "Isosceles"},
    {"id": "TC14", "name": "Tam giác thường", "input": (3, 4, 5), "expected": "Scalene"}
]

# Thực thi kiểm thử và in kết quả
passed_count = 0
failed_count = 0

for test in test_cases:
    a, b, c = test["input"]
    
    actual_result = classify_triangle(a, b, c)
    
    if actual_result == test["expected"]:
        status = "PASSED"
        passed_count += 1
    else:
        status = "FAILED"
        failed_count += 1
        
    input_str = f"({a}, {b}, {c})"
    print(f"{test['id']:<6} | {test['name']:<32} | {input_str:<15} | {actual_result:<15} | {status:<10}")

print("Kết quả kiểm thử:")
print(f"- Tổng số ca kiểm thử đã chạy: {len(test_cases)}")
print(f"- Số ca ĐẠT (PASSED): {passed_count}")
print(f"- Số ca LỖI (FAILED): {failed_count}")