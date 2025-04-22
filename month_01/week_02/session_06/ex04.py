total_purchase = float(input("Худалдан авалтын дүн: "))
is_member = input("Та гишүүн үү? (Тийм/Үгүй): ").lower() == "тийм"
# indentation - нэг TAB хоосон зай
if total_purchase >= 100:
    if is_member:
        discount = 0.2  # 20% хөнгөлөлт
    else:
        discount = 0.1  # 10% хөнгөлөлт
elif total_purchase >= 50:
    if is_member:
        discount = 0.1  # 10% хөнгөлөлт
    else:
        discount = 0.05  # 5% хөнгөлөлт
else:
    if is_member:
        discount = 0.05  # 5% хөнгөлөлт
    else:
        discount = 0  # Хөнгөлөлтгүй

final_price = total_purchase * (1 - discount)
print(f"Таны төлөх дүн: {final_price:.2f}")