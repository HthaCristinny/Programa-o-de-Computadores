powerup = input("Mario pegou qual item? (cogumelo/flor/estrela): ")

if powerup == "cogumelo":
    print("🍄 Mario ficou grande!")
elif powerup == "flor":
    print("🔥 Mario pode lançar fogo!")
elif powerup == "estrela":
    print("⭐ Mario ficou invencível!")
else:
    print("❓ Item desconhecido.")
