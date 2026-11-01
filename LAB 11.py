hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Toplam dakikayı hesapla ve saat/dakika cinsine çevir
total_mins = mins + dura
extra_hours = total_mins // 60
final_mins = total_mins % 60
final_hour = (hour + extra_hours) % 24

# Sonucu istenen formatta yazdır
print(final_hour, ":", final_mins, sep="")
