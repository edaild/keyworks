Passwoudcount = 5

while True:
    print("LOGIN")
    print("---------------------")

    DBuser_id = "user"
    DBuser_pw = 1123


    user_id = input("아이디를 입력하시요 ")
    user_pw = int(input("비밀번호를 입력하시요 "))
    print("---------------------")

    if user_pw == DBuser_pw:
        print(DBuser_id+"님 환영합니다.")

        print("원한시는 기능을 선택하시요")
        print("---------------------")
        Index = ["열차 조회", "역 정보 조회", "분신물 조회", "레일 페스 조회", "코레일 관광열차 조회", "고객센터"]
        print(Index)
        userMain = input("")

        if(userMain == Index[0]):
             print("열차 조회를 선택했습니다.") 
             TrainIndex = ["열차 시간", "행성지", "열차 정보"]
             print(TrainIndex)
             userTrain = input("")

        break    
    else: 
            print("비밀번호가 틀렸습니다.")
            Passwoudcount -= 1
            print("남은 회수는",Passwoudcount," 입니다.")

            if Passwoudcount == 0:    
                 break
            
    

    




