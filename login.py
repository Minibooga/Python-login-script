def login():
  global usrname
  global cfp
  usrname=input("Please input your username: ")
  pwd=input("Please input your password: ")
  cfp=inpuut("Reenter your password: ")
  if cfp==pwd:
    print("Thank you.")
  else:
    print(PASSWORDS DO NOT MATCH)
    login()
