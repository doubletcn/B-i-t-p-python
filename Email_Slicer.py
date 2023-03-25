# tách email thành user_name và domain_name

    #tách 1 email
# def emailProcess(email):
#     user_name=email[0:email.index("@")]
#     domain_name=email[email.index("@")+1:]
#     return user_name, domain_name


    #tách 1 chuỗi email
def emailsProcess(emails):
    result=[]
    for email in emails:
        user_name=email[0:email.index("@")]
        domain_name=email[email.index("@")+1:]
        result.append([user_name,domain_name])
    return result

def printMsg(user_name, domain_name):
    print(f"username là: {user_name}; domain name là: {domain_name}")


def main():
    # email=input("Nhap email: ").strip()
    # user_name,domain_name=emailProcess(email)
    # printMsg(user_name, domain_name)
    emails=["ttceen@gmail.com","thanhtrungcn@gmail.com","thanhtrungbbox@gmail.com"]
    user_info=emailsProcess(emails)
    for user_name,domain_name in user_info:
        printMsg(user_name, domain_name)

if __name__=="__main__":
    main()