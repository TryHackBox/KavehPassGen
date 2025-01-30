import itertools

# بنر اختصاصی
BANNER = """
 _____           _   _            _    ____            
|_   _| __ _   _| | | | __ _  ___| | _| __ )  _____  __
  | || '__| | | | |_| |/ _` |/ __| |/ /  _ \ / _ \ \/ /
  | || |  | |_| |  _  | (_| | (__|   <| |_) | (_) >  < 
  |_||_|   \__, |_| |_|\__,_|\___|_|\_\____/ \___/_/\_\
           |___/                                       
  
Password List Generator - Created by KAVEH
"""

def generate_password_list(info_list, min_length, max_length, output_file):
    passwords = set()  # برای جلوگیری از تکرار پسوردها
    
    # ایجاد ترکیبات ممکن از اطلاعات
    for length in range(min_length, max_length ):
        for combination in itertools.permutations(info_list, length):
            password = ''.join(combination)
            passwords.add(password)
    
    # ذخیره پسوردها در فایل
    if output_file:
        try:
            with open(output_file, 'w') as file:
                for password in passwords:
                    file.write(password + '\n')
            print(f"[+] Passwords saved to {output_file}")
        except Exception as e:
            print(f"[-] Error saving passwords to file: {e}")
    else:
        # نمایش پسوردها در کنسول
        print("[+] Generated Passwords:")
        for password in passwords:
            print(password)

def main():
    # نمایش بنر
    print(BANNER)

    # دریافت اطلاعات از کاربر
    print("[+] Enter target information:")
    phone_number = input("    Phone number: ").strip()
    birth_date = input("    Birth date: ").strip()
    city = input("    City: ").strip()
    pet_name = input("    Pet name: ").strip()
    first_name = input("    First name: ").strip()
    last_name = input("    Last name: ").strip()
    family_members = input("    Family members (separate by space): ").strip().split()
    school = input("    School or university: ").strip()
    national_id = input("    National ID: ").strip()
    street = input("    Street or neighborhood: ").strip()
    postal_code = input("    Postal code: ").strip()
    favorite_team = input("    Favorite sports team: ").strip()
    favorite_athlete = input("    Favorite athlete: ").strip()
    favorite_movie = input("    Favorite movie or series: ").strip()
    favorite_book = input("    Favorite book or author: ").strip()
    favorite_game = input("    Favorite video game: ").strip()
    company = input("    Company or organization: ").strip()
    job_title = input("    Job title: ").strip()
    field_of_study = input("    Field of study: ").strip()
    student_id = input("    Student or employee ID: ").strip()
    simple_numbers = input("    Simple numbers (separate by space): ").strip().split()
    keyboard_sequences = input("    Keyboard sequences (separate by space): ").strip().split()
    marriage_date = input("    Marriage date: ").strip()
    symbols = input("    Symbols to use (e.g., @, #, !): ").strip()

    # ایجاد لیست اطلاعات
    info_list = [
        phone_number, birth_date, city, pet_name, first_name, last_name,
        *family_members, school, national_id, street, postal_code,
        favorite_team, favorite_athlete, favorite_movie, favorite_book,
        favorite_game, company, job_title, field_of_study, student_id,
        *simple_numbers, *keyboard_sequences, marriage_date, *symbols
    ]

    # دریافت محدوده طول پسورد
    min_length = int(input("[+] Enter minimum password length: "))
    max_length = int(input("[+] Enter maximum password length: "))

    # دریافت نام فایل خروجی
    output_file = input("[+] Enter output file name (leave blank to print to console): ").strip()

    # تولید پسورد لیست
    generate_password_list(info_list, min_length, max_length, output_file)

if __name__ == "__main__":
    main()
