# Hàm đánh giá khoản vay
def evaluate_loan(age, income, credit_score, employment):
    
    # Kiểm tra ràng buộc đầu vào
    if type(age) is not int or type(credit_score) is not int:
        return "Invalid Input"
    if type(income) is not float and type(income) is not int:
        return "Invalid Input"
    if employment not in ["C", "F"]:
        return "Invalid Input"
        
    if age < 18 or age > 65:
        return "Invalid Input"
    if income < 5.0 or income > 500.0:
        return "Invalid Input"
    if credit_score < 300 or credit_score > 850:
        return "Invalid Input"

    # Làm tròn thu nhập đến 1 chữ số thập phân
    income = round(float(income), 1)

    # Phân loại rủi ro dựa trên credit score
    if 300 <= credit_score <= 500:
        risk = "High"
    elif 501 <= credit_score <= 700:
        risk = "Medium"
    else:
        risk = "Low"

    # Xử lý logic nghiệp vụ
    
    # Khách hàng có High Risk luôn bị reject
    if risk == "High":
        return "REJECT"

    # Quy tắc cho nhóm khách hàng có thu nhập dưới 15.0 triệu
    if income < 15.0:
        if employment == "F" or risk == "Medium":
            return "REJECT"
        if employment == "C" and risk == "Low":
            return "MANUAL REVIEW"

    # Quy tắc cho nhóm khách hàng có thu nhập từ 15.0 triệu trở lên
    if income >= 15.0:
        if employment == "C" and (risk == "Low" or risk == "Medium"):
            return "APPROVE"
        if employment == "F" and (risk == "Low" or risk == "Medium"):
            return "MANUAL REVIEW"
            
    return "REJECT"

# Thiết kế test cases
test_cases = [
    # Kiểm thử ràng buộc
    {
        "id": "TC01", "desc": "Tuổi nhỏ hơn biên dưới (17)",
        "inputs": (17, 20.0, 600, "C"), "expected": "Invalid Input"
    },
    {
        "id": "TC02", "desc": "Tuổi lớn hơn biên trên (66)",
        "inputs": (66, 20.0, 600, "C"), "expected": "Invalid Input"
    },
    {
        "id": "TC03", "desc": "Thu nhập nhỏ hơn biên dưới (4.9)",
        "inputs": (30, 4.9, 600, "C"), "expected": "Invalid Input"
    },
    {
        "id": "TC04", "desc": "Thu nhập lớn hơn biên trên (500.1)",
        "inputs": (30, 500.1, 600, "C"), "expected": "Invalid Input"
    },
    {
        "id": "TC05", "desc": "Credit score < biên dưới (299)",
        "inputs": (30, 20.0, 299, "C"), "expected": "Invalid Input"
    },
    {
        "id": "TC06", "desc": "Credit score > biên trên (851)",
        "inputs": (30, 20.0, 851, "C"), "expected": "Invalid Input"
    },
    {
        "id": "TC07", "desc": "Mã công việc sai quy định ('X')",
        "inputs": (30, 20.0, 600, "X"), "expected": "Invalid Input"
    },
    
    # Kiểm thử logic nghiệp vụ
    {
        "id": "TC08", "desc": "Rule 1: Risk High",
        "inputs": (18, 20.0, 300, "C"), "expected": "REJECT"
    },
    {
        "id": "TC09", "desc": "Rule 2: Risk Medium + Income < 15",
        "inputs": (30, 14.9, 600, "C"), "expected": "REJECT"
    },
    {
        "id": "TC10", "desc": "Rule 3: Risk Low + Income < 15 + Freelance",
        "inputs": (45, 10.0, 750, "F"), "expected": "REJECT"
    },
    {
        "id": "TC11", "desc": "Rule 4: Risk Low + Income < 15 + Contract",
        "inputs": (65, 5.0, 800, "C"), "expected": "MANUAL REVIEW"
    },
    {
        "id": "TC12", "desc": "Rule 5: Risk Medium + Income >= 15 + Contract",
        "inputs": (25, 15.0, 501, "C"), "expected": "APPROVE"
    },
    {
        "id": "TC13", "desc": "Rule 6: Risk Low + Income >= 15 + Freelance",
        "inputs": (65, 500.0, 850, "F"), "expected": "MANUAL REVIEW"
    }
]


# Thực hiện test cases
passed_count = 0
failed_count = 0

print(f"{'ID':<5} | {'MỤC ĐÍCH KIỂM THỬ':<45} | {'DỮ LIỆU ĐẦU VÀO':<22} | {'KẾT QUẢ MONG ĐỢI':<16} | {'TRẠNG THÁI':<10}")

for test in test_cases:
    age, income, score, emp = test["inputs"]
    
    actual_result = evaluate_loan(age, income, score, emp)
    
    if actual_result == test["expected"]:
        status = "PASSED"
        passed_count += 1
    else:
        status = "FAILED"
        failed_count += 1
        
    input_display = f"({age}, {income}, {score}, '{emp}')"
    print(f"{test['id']:<5} | {test['desc']:<45} | {input_display:<22} | {test['expected']:<16} | {status:<10}")


print(f"- Tổng số kịch bản kiểm thử đã thực thi : {len(test_cases)}")
print(f"- Số lượng kịch bản thành công (PASSED) : {passed_count}")
print(f"- Số lượng kịch bản thất bại   (FAILED) : {failed_count}")

if failed_count == 0 and passed_count == len(test_cases):
    print("Hệ thống vượt qua (PASSED) 100% tất cả các trường hợp kiểm thử thiết kế.")
else:
    print("Hệ thống lỗi chưa hoàn thiện")