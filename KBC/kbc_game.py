

questions =[
    [
        "Which language was used ti Create FB???" , "Python" ,"French","Javascript","PHP" ,"None",4
    ],
    [
        "Which programming language is commonly used for Android app development?",
        "Java",
        "C++",
        "Python",
        "Swift",
        "None",
        1
    ],
    [
        "What does HTML stand for?",
        "Hyperlinks and Text Markup Language",
        "Home Tool Markup Language",
        "Hypertext Markup Language",
        "Hyper Transfer Markup Language",
        "None",
        3
    ],
    [
        "Which company developed the Python programming language?",
        "Microsoft",
        "Apple",
        "Google",
        "Facebook",
        "None",
        4
    ],
    [
        "Which scripting language is often used for web development?",
        "Java",
        "C++",
        "JavaScript",
        "Ruby",
        "None",
        3
    ],

    [
        "Which programming language is used for machine learning and data analysis?",
        "Java",
        "Python",
        "C#",
        "Ruby",
        "None",
        2
    ],
    [
        "What is the main purpose of CSS in web development?",
        "Data storage",
        "Layout and presentation",
        "Server-side processing",
        "Database management",
        "None",
        2
    ],
    [
        "Which protocol is used for secure communication over the internet?",
        "HTTP",
        "FTP",
        "TCP",
        "HTTPS",
        "None",
        4
    ],
    [
        "Which company developed the JavaScript programming language?",
        "Microsoft",
        "Apple",
        "Google",
        "Netscape",
        "None",
        4
    ]
]

levels =[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money =0


for i in range(0,len(questions)):
    question = questions[i]
    print(f"Question for Rs.{levels[i]}")
    print(question[0])
    print(f"1. {question[1]}           2. {question[2]}")
    print(f"3. {question[3]}           4. {question[4]}")
    reply = int(input("Enter your answer (1-4) -->"))
    if reply == question[-1]:
        print("Correct answer!!")
        print(f"you won {levels[i]} Rs/-")
        if i==4:
            money = 10000
        elif i==9:
            money = 320000
    else:
        print("Wrong Answer")
        break


