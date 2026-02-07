#Library Book Borrowing
#CReate the Dictionary
borrow_data = {
                 "gayana" : ["python","data science", "java"],
               "Bhavi" : ["Science","java"],
               "Pami"  : ["java","python"]
               }
print(borrow_data)
all_book= set()
for books in borrow_data.values():
    all_book.update(books)
print(all_book)    
max_user = None
max_books = 0

for user, books in borrow_data.items():
    if len(books) > max_books:
        max_books = len(books)
        max_user = user

print("User with max books:", max_user)
python_users = []

for user, books in borrow_data.items():
    if "python" in books:
        python_users.append(user)

print("Users who borrowed Python:", python_users)
borrow_set_data = {}

for user, books in borrow_data.items():
    borrow_set_data[user] = set(books)

print(borrow_set_data)