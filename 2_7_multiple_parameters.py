def say_hello(user_name, user_age):
  print("hello", user_name)
  print("you are", user_age, "years old")

# user_name은 함수 안에서만 유효함
# print(user_name) # 오류 발생

say_hello("nico", 12)
