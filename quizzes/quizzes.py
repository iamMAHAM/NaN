questions = [{
    "question": "qui est le premier président de la CI ?",
    "choix_possibles": ["HKB", "LG", "KKB", "ADO", "FHB"],
    "response": 5,
    "points": 1,
},
    {
        "question": "quelle est la superficie de la CI ?",
    "choix_possibles": [422362, 322462, 500000],
    "response": 5,
    "points": 1,
},
    {
    "question": "qui paiera gage jusqu'a la sortie ?",
    "choix_possibles": ['yasmine', 'diallo', 'issouf', 'moise', 'josias'],
    "response": 2,
    "points": 4
}
]


def quizzes(questions=[]):
    if (isinstance(questions, list) and all(isinstance(q, dict) for q in questions)):
        score = 0
        for question in questions:
            print(question['question'])
            for i_choix in range(len(question["choix_possibles"])):
                print(
                    f'{i_choix + 1} - {question["choix_possibles"][i_choix]}', end=' ')

            choix = int(input(' : >'))

            if choix == question['response']:
                score += question["points"]
        print(
            f'Vous avez obtenu : {score} points sur {sum(list(map(lambda x : x["points"],questions)))}')

    else:
        print('Format de données invalides .')


quizzes(questions)
