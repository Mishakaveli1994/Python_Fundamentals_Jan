exam_results = {}
submissions = {}

while True:
    command = input()
    if command == 'exam finished':
        break
    else:
        command_split = command.split('-')

        if command_split[1] == 'banned':
            name = command_split[0]
            if name in exam_results:
                del exam_results[name]
        else:
            name, lang, score = command_split[0], command_split[1], int(command_split[2])
            if lang not in submissions:
                submissions[lang] = 1
            else:
                submissions[lang] += 1

            if name not in exam_results:
                exam_results[name] = [score]
            else:
                exam_results[name] += [score]

for i in exam_results:
    exam_results[i] = max(exam_results[i])

print('Results:')
sorted_exam_results = {print(f"{k} | {v}") for k, v in sorted(exam_results.items(), key=lambda x: (-x[1], x[0]))}

print('Submissions:')
sorted_submission_results = {print(f"{k} - {v}") for k, v in sorted(submissions.items(), key=lambda x: (-x[1], x[0]))}

