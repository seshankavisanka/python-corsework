# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1987581
# Date: 19.04.2023


def main():
    student_ids = []
    range_list = [0, 20, 40, 60, 80, 100, 120]
    countProgress = 0
    countTrailer = 0
    countRetriever = 0
    countExcluded = 0
    inputProgression = []
    dataStored = {}

    while True:
        studentId = get_id(student_ids)
        passCredits, deferCredit, failCredit = outcomes(range_list)
        countProgress, countTrailer, countRetriever, countExcluded, inputProgression, dataStored = validation(passCredits, deferCredit, failCredit, countProgress, countTrailer, countRetriever, countExcluded, inputProgression, dataStored, studentId)

        print("\nWould you like to enter another set of data?")
        multipleOutcomes = input("Enter 'y' for yes or 'q' to quit and view results: ")

        if multipleOutcomes.lower() == "y":
            print("")
        elif multipleOutcomes.lower() == "q":
            histogram(countProgress, countTrailer, countRetriever, countExcluded)
            part_2(inputProgression)
            part_3(inputProgression)
            part_4(dataStored)
            break
        else:
            print("Invalid entered")
            break


def get_id(student_id):
    # get valid student id number
    while True:
        get_student_id = input("Please enter student ID: ")
        if len(get_student_id) == 8 and get_student_id[0].lower() == "w" and get_student_id[1:].isdigit():
            if get_student_id not in student_id:
                student_id.append(get_student_id)
                return get_student_id
            else:
                print("Student ID is entered")
                continue
        else:
            print("Wrong student id")


def outcomes(rangers):
    # check entered credits in the range
    while True:
        try:
            pass_credits = int(input("Please enter your credits at pass: "))
            if pass_credits in rangers:
                while True:
                    try:
                        defer_credit = int(input("Please enter your credit at defer: "))
                        if defer_credit in rangers:
                            while True:
                                try:
                                    fail_credit = int(input("Please enter your credit at fail: "))
                                    if fail_credit in rangers:
                                        return pass_credits, defer_credit, fail_credit
                                    else:
                                        print("Out of range")
                                except ValueError:
                                    print("Integer required")
                        else:
                            print("Out of range")
                    except ValueError:
                        print("Integer required")
            else:
                print("Out of range")
        except ValueError:
            print("Integer required")


def validation(pass_credits, defer_credit, fail_credit, count_progress, count_trailer, count_retriever, count_excluded, input_progression, data_stored, student_id):
    total = pass_credits + defer_credit + fail_credit
    if total == 120:
        if pass_credits == 120:
            progression_outcome = "Progress"
            print(progression_outcome)
            count_progress += 1
            input_progression.extend([progression_outcome, pass_credits, defer_credit, fail_credit])
            data_stored[student_id] = progression_outcome + " - " + str(pass_credits) + ", " + str(defer_credit) + ", " + str(fail_credit)
        else:
            if pass_credits == 100 and defer_credit == 20 or pass_credits == 100 and fail_credit == 20:
                progression_outcome = "Progress (module trailer)"
                print(progression_outcome)
                count_trailer += 1
                input_progression.extend([progression_outcome, pass_credits, defer_credit, fail_credit])
                data_stored[student_id] = progression_outcome + " - " + str(pass_credits) + ", " + str(defer_credit) + ", " + str(fail_credit)
            else:
                if pass_credits + defer_credit >= fail_credit:
                    progression_outcome = "Module retriever"
                    print(progression_outcome)
                    count_retriever += 1
                    input_progression.extend([progression_outcome, pass_credits, defer_credit, fail_credit])
                    data_stored[student_id] = progression_outcome + " - " + str(pass_credits) + ", " + str(defer_credit) + ", " + str(fail_credit)
                else:
                    progression_outcome = "Exclude"
                    print(progression_outcome)
                    count_excluded += 1
                    input_progression.extend([progression_outcome, pass_credits, defer_credit, fail_credit])
                    data_stored[student_id] = progression_outcome + " - " + str(pass_credits) + ", " + str(defer_credit) + ", " + str(fail_credit)

    else:
        print("Total incorrect")

    return count_progress, count_trailer, count_retriever, count_excluded, input_progression, data_stored


def histogram(count_progress, count_trailer, count_retriever, count_excluded):
    print("\n" + "-" * 50, end="")
    print("\nHistogram")
    print("Progress " + str(count_progress) + "\t: " + "*" * count_progress)
    print("Trailer " + str(count_trailer) + "\t: " + "*" * count_trailer)
    print("Retriever " + str(count_retriever) + "\t: " + "*" * count_retriever)
    print("Excluded " + str(count_excluded) + "\t: " + "*" * count_excluded + "\n")
    print(str(count_progress + count_trailer + count_retriever + count_excluded) + " outcomes in total.")
    print("-" * 50)


def part_2(input_progression):
    print("\nPart 2: ")
    # get values in the list
    list_index = 0

    while list_index < len(input_progression):
        print(str(input_progression[list_index]) + " - " + str(input_progression[list_index + 1]) + ", " + str(input_progression[list_index + 2]) + ", " + str(input_progression[list_index + 3]))
        list_index += 4


def part_3(input_progression):
    # create text file
    text_file = open("w1987581.txt", "w+")
    text_file.write("Part 3:\n")
    list_index = 0

    while list_index < len(input_progression):
        text_file.write(str(input_progression[list_index]) + " - " + str(input_progression[list_index + 1]) + ", " + str(input_progression[list_index + 2]) + ", " + str(input_progression[list_index + 3]) + "\n")
        list_index += 4

    # read value in the text file
    text_file = open("w1987581.txt", "r")
    print("\n" + text_file.read())
    text_file.close()


def part_4(data_stored):
    # get values in the dictionary
    print("\nPart 4:")
    dic_index = 0
    for x in data_stored.items():
        print(x[dic_index] + " : " + x[dic_index + 1] + " ", end="")


main()