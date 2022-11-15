try:
    grade = int(input("what is your grade ?"))
    markings = print(f"you have achieved a {int(grade / 10)}")
except:
    if ValueError:
        print ("I'm sorry, I cannot grade a string ")

#In this code i made a grading system that doesnt use a millions Elifs or a billion lines of code. I couldve effectively 
#used 2 lines of code without the try and except statements 