# -----------------------------
# Admin Login
# -----------------------------
def admin_login(admins):
    aid = input('Enter Admin ID: ')
    pwd = input('Enter Password: ')
    return admins.get(aid) == pwd

# -----------------------------
# Admin Functions
# -----------------------------
def add_question(questions):
    tech = input('Enter technology (e.g., Python/MySQL): ')
    q = input('Enter question: ')
    a = input('Enter answer: ')
    if tech not in questions:
        questions[tech] = []
    questions[tech].append({'question': q, 'answer': a})

def modify_question(questions):
    tech = input('Enter technology: ')
    if tech in questions and questions[tech]:
        for i, q in enumerate(questions[tech]):
            print(f'{i+1}. {q['question']}')
        index = int(input('Enter question number to modify: ')) - 1
        nq = input('Enter new question: ')
        na = input('Enter new answer: ')
        questions[tech][index] = {'question': nq, 'answer': na}
    else:
        print('No questions available.')

def delete_question(questions):
    tech = input('Enter technology: ')
    if tech in questions and questions[tech]:
        for i, q in enumerate(questions[tech]):
            print(f'{i+1}. {q['question']}')
        index = int(input('Enter question number to delete: ')) - 1
        questions[tech].pop(index)
    else:
        print('No questions to delete.')

def view_questions(questions):
    for tech in questions:
        print(f'\n--- {tech} Questions ---')
        for i, q in enumerate(questions[tech]):
            print(f'{i+1}. {q['question']}')


#---------------------------
# Admin Menu
#---------------------------
def admin_menu(questions, user_scores, admins):
    while True:
        print('\n--- Admin Menu ---')
        print('1. Add Question')
        print('2. Modify Question')
        print('3. Delete Question')
        print('4. View All Questions')
        print('5. View User Scores')
        print('6. Logout')
        choice = input('Enter choice: ')
        if choice == '1':
            add_question(questions)
        elif choice == '2':
            modify_question(questions)
        elif choice == '3':
            delete_question(questions)
        elif choice == '4':
            view_questions(questions)
        elif choice == '5':
            for u in user_scores:
                print(u)
        elif choice == '6':
            break
        else:
            print("Invalid choice!")

# -----------------------------
# User Functions
# -----------------------------
def take_quiz(questions, user_name, mobile):
    tech = input('Enter technology: ')
    if tech not in questions or not questions[tech]:
        print('No questions available')
        return None

    import time
    score = 0
    start = time.time()
    for q in questions[tech]:
        print(q['question'])
        ans = input('Answer: ')
        if ans == q['answer']:
            score += 1
    end = time.time()
    duration = round(end - start, 2)
    return {'name': user_name, 'mobile': mobile, 'score': score, 'time': duration}

def show_top_scores(user_scores):
    sorted_scores = sorted(user_scores, key=lambda u: (-u['score'], u['time']))
    print('\n--- Top 3 Scores ---')
    for user in sorted_scores[:3]:
        print(f'{user['name']} | Score: {user['score']} | Time: {user['time']} sec')

#----------------------------------
# User Menu
#----------------------------------
def user_menu(questions, user_scores):
    name = input('Enter your Name: ')
    mobile = input('Enter your Mobile Number: ')
    while True:
        print('\n--- User Menu ---')
        print('1. Take Quiz')
        print('2. View Top 3 Scores')
        print('3. Logout')
        choice = input('Enter your choice: ')
        if choice == '1':
            result = take_quiz(questions, name, mobile)
            if result:
                user_scores.append(result)
                print(f'Your Score: {result['score']}, Time: {result['time']} sec')
        elif choice == '2':
            if user_scores:
                show_top_scores(user_scores)
            else:
                print('No scores available.')
        elif choice == "3":
            break
        else:
            print('Invalid choice')

# -----------------------------
# Main Program
# -----------------------------
def main():
    questions_db = {'Python': [], 'MySQL': []}
    user_scores = []
    admin_credentials = {'admin': 'admin123'}

    while True:
        print('\n====== Quiz System ======')
        print('1. Admin Login')
        print('2. User Login')
        print('3. Exit')
        option = input('Choose an option: ')
        if option == '1':
            if admin_login(admin_credentials):
                admin_menu(questions_db, user_scores, admin_credentials)
            else:
                print('Invalid Admin credentials')
        elif option == '2':
            user_menu(questions_db, user_scores)
        elif option == '3':
            print('Thank you for using the Quiz System')
            break
        else:
            print('Invalid option')


main()



