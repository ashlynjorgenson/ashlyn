#1. Git vs. GitHub
	# git tracks changes
	# git hub is an online opensource repository hub that saves your repositories remotely and allows for collaboration
#2. Terminal vs. Command Line
	# the terminal is a interface like a GUI but instead it's text-based
	# the command line is how you interact with the terminal and where you call commands
#3. Local vs. Remote Repository
	# a local repository is saved to your computer
	# a remote repository is saved to the internet or server
#4. Version Control
	# a way of tracking and managing changes to your code over time
#5. Staging Area
	# tells git that you're going to be making changes and to begin tracking them
#6. git add
	# adds your file or repository to the staging area
#7. git commit
	# commits your file to a version history
#8. git push
	# pushes your file to the remote repository
#9. git status
	# checks the status of your repository
#10. git pull
	# to grab the newest changes from a remote repository
#11. pwd
	# print working directory
#12. ls
	# list what's in the repository you are in
#13. cd
	# change directories
#14. nano
	# creates a new file and takes you into it
#15. touch
	# creates a new file without putting you into it
#16. mv
	# moves a file or directory
#17. rm
	# deletes files
#18. cat
	# displays everything in a file


#Questions:
#• You have been plopped into Judy’s directory system. What command will tell you what your
#current working directory is?
	# pwd
#• The terminal responds by saying you are in ∼/python decal/judy decal. What comman will list all the files in your current working directory?
	# ls

#• Oh no! Brianna just sent out an announcement saying that there was a typo in homework.py.You will need to pull the brianna repo repository to find the updated file. What command(s)
#will let you move to the correct repository and pull the latest changes?
	# cd ../brianna_repo
	# git pull
	
#• How would you move this new homework.py to the homework/ folder in your personal repository?
	# cp ~/python_decal/brianna_repo/homework.py ~/python_decal/judy_decal/homework/

#• How would you move yourself to the same repository as homework.py?
	 # cd python_decal/judy_decal/homework/

#• You want to see the contents of homework.py in your terminal, how would you do this?
	# cat homework.py
#• Great job! You just finished the homework for this week. What command(s) allow you to save the changes and push from your local repository to your remote repository?
	# git add .
	# git push -m "done with hw"
	# git commit origin main

#• Oh no! Git gave you the following error. What commands should you call to resolve this error and push your homework properly? What does the error mean? (i.e. what did “Judy”
#do wrong when trying to push?)
	# your local branch is behind the remote main branch
	#git pull --rebase origin main
	#git push origin main

#! [rejected] main -> main (fetch first)
#error: failed to push some refs to ’https://github.com
#/judy/judy_decal.git’
#hint: Updates were rejected because the remote contains
#work that you do
#hint: not have locally. This is usually caused by another
#repository pushing
#hint: to the same ref. You may want to first integrate
#the remote changes
#hint: (e.g., ’git pull ...’) before pushing again.
#hint: See the ’Note about fast-forwards’ in ’git push
#--help’ for details.

#• What absolute path will allow you to move to Recents/?
	# cd ~/Recent


# 4.1 Data Types
def input_to_datatype(input):
    return type(input)
print(input_to_datatype(4.2))

# 4.2 Conditionals
def even_or_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
print(even_or_odd(3)) 

# 5 Loops
numbers=[1,2,3,4,5]
def sum_with_loop(numbers):
    sum=0
    for num in numbers:
        sum+=num
    return sum
print(sum_with_loop(numbers))

# 6.1 Lists
list= ['a','b', 'c']
def duplicate_list(list):
    result=[]
    for item in list:
          result.append(item)
          result.append(item)
    return result
print(duplicate_list(list))

#6.2 Debugging
# it should be return num ** 2. there also is no colon after the definition
def square(num):
    return num**2
print(square(3))





print(even_or_odd(5))
   

