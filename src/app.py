import os

def main():
    api_key = os.getenv("API_KEY", "MISSING")
    print("API_KEY visible? ->", "YES" if api_key != "MISSING" else "NO")
    print("Recuerda: no subas .env ni credenciales a Git.")
if __name__ == "__main__":
    main()
