import re

def is_strong_password(password):
    """Checks if a password meets the strong password criteria."""
    if len(password) < 8:
        print("❌ Password must be at least 8 characters long.")
        return False
    if not re.search(r"[a-z]", password):
        print("❌ Password must contain at least one lowercase letter.")
        return False
    if not re.search(r"[A-Z]", password):
        print("❌ Password must contain at least one uppercase letter.")
        return False
    if not re.search(r"\d", password):
        print("❌ Password must contain at least one digit.")
        return False
    
    return True  # Password meets all criteria

while True:
    password = input("\nEnter a password to check its strength: ").strip()

    if is_strong_password(password):
        print("✅ Strong password! Your password meets all security criteria.")
    else:
        print("⚠️ Weak password! Try again.")

    # Ask if the user wants to check another password
    retry = input("\nWould you like to test another password? (y/n): ").strip().lower()
    if retry != 'y':
        print("Goodbye!")
        break
