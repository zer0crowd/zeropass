import os
from password_generator import generate_password
from file_organizer import organize_files
from web_scraper import scrape_website

def main():
    while True:
        print("\n🔧 HERRAMIENTAS ÚTILES 🔧")
        print("1. Generar contraseña segura")
        print("2. Organizar archivos en una carpeta")
        print("3. Extraer datos de una página web (scraping ético)")
        print("4. Salir")

        choice = input("\nSelecciona una opción: ")

        if choice == "1":
            length = int(input("Longitud de la contraseña: "))
            print(f"\n🔑 Contraseña generada: {generate_password(length)}")
        
        elif choice == "2":
            folder_path = input("Ruta de la carpeta a organizar: ")
            organize_files(folder_path)
            print("✅ ¡Archivos organizados!")
        
        elif choice == "3":
            url = input("URL de la página a analizar (ej: https://ejemplo.com): ")
            data = scrape_website(url)
            print(f"\n📊 Datos extraídos: {data}")
        
        elif choice == "4":
            print("👋 ¡Hasta luego!")
            break
        
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    main()