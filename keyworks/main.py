while True:
    print("LOGIN")

    DBuser_id = "user"
    DBuser_pw = 1123

    user_id = input("아이디를 입력하시오")
    user_pw = int(input("비밀번호를 입력하시오"))


    if user_pw == DBuser_pw:
        print(user_id,"님 환영합니다.")

        print("원한시는 기능을 선택하시오")
        Index = ["열차 조회", "역 정보 조회", "분신물 조회", "레일 페스 조회", "코레인 관광열차 조회", "고객센터"]
        print(Index)
        userMain = input("")
        if(userMain == Index[0]):
             print("열차 조회를 선택했습니다.") 
             TrainIndex = ["d"]

        break    
    else: 
            print("비밀번호가 틀렸습니다.")
            
    

    




