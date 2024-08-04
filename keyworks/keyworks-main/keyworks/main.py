print("발급을 원하시는 증명서를 선택하십시오")
print("----------------------------------")
number = ['주민등록' , '지잭,토치,건축' , '차량' , '보건복지' ,'농지대장,농협경영체' , '병적증명서', '지방세', '어선원부', '교육재증명 대학교(원) 제외', '국세증명', '건강보험', '고용, 상재보험(근로복지공단)','여권','국민연금']
print(number)
user = input(" 원하시는 증명서를 선택하십시오 ")

if number[0] == user:
    number01 = ["주민등록표(초본)" , "주민등록표(등본)"]
    print(number01)
    user01 = input("원하시는 증명서를 선택하시오 ")

    if number01[1] == user01:
        number02 = ["주민등로 번호 지문"]
        print(number02)
        user02 = input("원하시는 증명서를 선택하시오")
        
        if number02[0] == user02:
            number03 = ["number1", "number2", "number3", "number4", "number5"]
            print(number03)
            user03 = input("원하시는 기능을 선택하시오")

            if number03[0] == user03:
                number04 = ["수수료 면제 대상자","수수료 면제 대상자 아님"]
                print(number04)
                user04 = input("원하시는 기능을 선택하시오")

                if number04[1] == user04:
                    print("신청증명서 주민등록표")
                    print("수수로면제 일반 (면제 아님)")
                    number05 = ['1','2','3','4','5','6','7','8','9']
                    
                    print(number05)
                    user05 = input("인쇄를 원하는 장수를 선택하시오")
                    
                    if number05[0] == user05: print("1장 인쇄합니다.")

else:
    print("죄송합니다. 지금은 점검중 입니다.")    
