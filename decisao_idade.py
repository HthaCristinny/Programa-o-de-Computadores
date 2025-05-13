idade = int(input("Qual a sua idade? "))

if idade > 10:
    print("✅ Você pode jogar a Fase do Castelo!")
elif idade == 10:
    print("⚠️ Você está na idade mínima. Jogue com cuidado!")
else:
    print("🚫 Fase muito difícil. Escolha uma fase mais fácil.")
